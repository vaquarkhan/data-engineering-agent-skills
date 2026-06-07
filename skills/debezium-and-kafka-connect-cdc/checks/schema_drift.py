#!/usr/bin/env python3
"""Detect schema drift between a captured CDC schema and a dataset contract.

This check compares the actual schema of CDC-consumed data against the expected
contract definition.  It detects:
- Missing columns (present in contract but absent in data)
- Type mismatches (column type differs from contract)
- Unexpected columns (present in data but not in contract)
- Nullable changes (contract says non-nullable but data schema says nullable)

This is critical for CDC pipelines because Debezium propagates upstream DDL
changes into the event stream.  Without drift detection, breaking schema
changes silently corrupt downstream consumers.

Usage:
    python checks/schema_drift.py --contract contract.yaml --schema schema.json
    python checks/schema_drift.py --contract contract.yaml --source data.parquet
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect schema drift between CDC data and a dataset contract."
    )
    parser.add_argument(
        "--contract",
        required=True,
        type=Path,
        help="Path to the dataset contract YAML.",
    )
    schema_source = parser.add_mutually_exclusive_group(required=True)
    schema_source.add_argument(
        "--schema",
        type=Path,
        help="Path to a JSON schema file describing actual columns.",
    )
    schema_source.add_argument(
        "--source",
        type=Path,
        help="Path to a parquet/csv file to infer schema from.",
    )
    return parser.parse_args()


def load_contract_schema(contract_path: Path) -> list[dict[str, Any]]:
    """Load column definitions from a dataset contract YAML."""
    import yaml

    payload = yaml.safe_load(contract_path.read_text(encoding="utf-8")) or {}
    contract = payload.get("dataset_contract", payload)
    columns = contract.get("schema", {}).get("columns", [])
    if not columns:
        raise SystemExit(f"No schema.columns found in contract: {contract_path}")
    return columns


def load_actual_schema_from_json(schema_path: Path) -> list[dict[str, Any]]:
    """Load actual schema from a JSON file.

    Expected format:
    [
        {"name": "col1", "type": "string", "nullable": true},
        ...
    ]
    """
    data = json.loads(schema_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "columns" in data:
        return data["columns"]
    raise SystemExit(f"Unsupported schema JSON structure in {schema_path}")


def load_actual_schema_from_source(source_path: Path) -> list[dict[str, Any]]:
    """Infer schema from a data file (parquet or csv)."""
    import pandas as pd

    suffix = source_path.suffix.lower()
    if suffix == ".parquet":
        import pyarrow.parquet as pq

        parquet_schema = pq.read_schema(source_path)
        columns = []
        for field in parquet_schema:
            columns.append({
                "name": field.name,
                "type": _arrow_type_to_contract_type(str(field.type)),
                "nullable": field.nullable,
            })
        return columns
    elif suffix == ".csv":
        df = pd.read_csv(source_path, nrows=100)
        columns = []
        for col_name, dtype in df.dtypes.items():
            columns.append({
                "name": str(col_name),
                "type": _pandas_dtype_to_contract_type(str(dtype)),
                "nullable": bool(df[col_name].isna().any()),
            })
        return columns
    else:
        raise SystemExit(f"Cannot infer schema from {suffix} files. Use .parquet or .csv")


def _arrow_type_to_contract_type(arrow_type: str) -> str:
    """Map Arrow type strings to contract type names."""
    arrow_type = arrow_type.lower()
    if "int" in arrow_type:
        return "integer"
    if "float" in arrow_type or "double" in arrow_type:
        return "float"
    if "decimal" in arrow_type:
        return "decimal"
    if "bool" in arrow_type:
        return "boolean"
    if "timestamp" in arrow_type:
        return "timestamp"
    if "date" in arrow_type:
        return "date"
    if "string" in arrow_type or "utf8" in arrow_type:
        return "string"
    return arrow_type


def _pandas_dtype_to_contract_type(dtype: str) -> str:
    """Map pandas dtype strings to contract type names."""
    dtype = dtype.lower()
    if "int" in dtype:
        return "integer"
    if "float" in dtype:
        return "float"
    if "bool" in dtype:
        return "boolean"
    if "datetime" in dtype:
        return "timestamp"
    if "object" in dtype or "string" in dtype:
        return "string"
    return dtype


def _normalize_type(type_str: str) -> str:
    """Normalize type strings for comparison."""
    t = type_str.lower().strip()
    # Strip precision from decimal
    if t.startswith("decimal"):
        return "decimal"
    if t in {"int", "integer", "bigint", "int64", "int32"}:
        return "integer"
    if t in {"float", "double", "float64", "float32"}:
        return "float"
    if t in {"str", "string", "varchar", "text"}:
        return "string"
    if t in {"bool", "boolean"}:
        return "boolean"
    if t.startswith("timestamp"):
        return "timestamp"
    if t == "date":
        return "date"
    return t


def check_schema_drift(
    contract_columns: list[dict[str, Any]],
    actual_columns: list[dict[str, Any]],
    contract_path: str,
) -> dict[str, Any]:
    """Compare contract schema against actual schema and report drift."""
    contract_map = {col["name"]: col for col in contract_columns}
    actual_map = {col["name"]: col for col in actual_columns}

    missing_columns: list[str] = []
    type_mismatches: list[dict[str, str]] = []
    nullable_changes: list[dict[str, Any]] = []
    unexpected_columns: list[str] = []

    # Check for missing columns and type/nullable drift
    for col_name, contract_col in contract_map.items():
        if col_name not in actual_map:
            missing_columns.append(col_name)
            continue

        actual_col = actual_map[col_name]
        contract_type = _normalize_type(str(contract_col.get("type", "string")))
        actual_type = _normalize_type(str(actual_col.get("type", "string")))

        if contract_type != actual_type:
            type_mismatches.append({
                "column": col_name,
                "expected": contract_type,
                "actual": actual_type,
            })

        contract_nullable = contract_col.get("nullable", True)
        actual_nullable = actual_col.get("nullable", True)
        if contract_nullable != actual_nullable:
            nullable_changes.append({
                "column": col_name,
                "expected_nullable": contract_nullable,
                "actual_nullable": actual_nullable,
            })

    # Check for unexpected columns
    for col_name in actual_map:
        if col_name not in contract_map:
            unexpected_columns.append(col_name)

    # Classify changes
    breaking_changes: list[str] = []
    additive_changes: list[str] = []

    for col in missing_columns:
        breaking_changes.append(f"column '{col}' missing from data")
    for mismatch in type_mismatches:
        breaking_changes.append(
            f"column '{mismatch['column']}' type changed: "
            f"expected {mismatch['expected']}, got {mismatch['actual']}"
        )
    for change in nullable_changes:
        if not change["expected_nullable"] and change["actual_nullable"]:
            breaking_changes.append(
                f"column '{change['column']}' became nullable (contract requires non-nullable)"
            )
        else:
            additive_changes.append(
                f"column '{change['column']}' nullable changed: "
                f"expected={change['expected_nullable']}, actual={change['actual_nullable']}"
            )
    for col in unexpected_columns:
        additive_changes.append(f"unexpected column '{col}' in data (not in contract)")

    has_breaking = len(breaking_changes) > 0
    status = "fail" if has_breaking else "pass"

    return {
        "check": "schema_drift",
        "status": status,
        "contract": contract_path,
        "drift_details": {
            "missing_columns": missing_columns,
            "type_mismatches": type_mismatches,
            "nullable_changes": nullable_changes,
            "unexpected_columns": unexpected_columns,
        },
        "breaking_changes": breaking_changes,
        "additive_changes": additive_changes,
    }


def main() -> int:
    args = parse_args()
    contract_columns = load_contract_schema(args.contract)

    if args.schema:
        actual_columns = load_actual_schema_from_json(args.schema)
    else:
        actual_columns = load_actual_schema_from_source(args.source)

    result = check_schema_drift(contract_columns, actual_columns, str(args.contract))
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
