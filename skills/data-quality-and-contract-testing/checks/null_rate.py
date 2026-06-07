#!/usr/bin/env python3
"""Check null rate per column against contract-defined thresholds.

Data contracts often specify maximum acceptable null rates for each column.
A non-nullable column that starts accumulating nulls indicates upstream
breakage (e.g., a schema change dropped a field to default NULL, or a
source system changed behavior).

This check reads the data, computes per-column null rates, and compares
them against thresholds from the contract YAML or a default threshold.

Usage:
    python checks/null_rate.py --source data.csv --contract contract.yaml
    python checks/null_rate.py --source data.parquet --threshold 0.05
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check null rate per column against thresholds."
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to data file (parquet, csv, or jsonl).",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        help="Path to dataset contract YAML with per-column null thresholds.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="Default max null rate if contract does not specify per-column. Default: 0.0",
    )
    return parser.parse_args()


def load_dataframe(path: Path) -> "Any":
    """Load a file into a pandas DataFrame based on extension."""
    import pandas as pd

    suffix = path.suffix.lower()
    if suffix == ".parquet":
        return pd.read_parquet(path)
    elif suffix == ".csv":
        return pd.read_csv(path)
    elif suffix in {".jsonl", ".ndjson"}:
        return pd.read_json(path, lines=True)
    else:
        raise SystemExit(f"Unsupported file format: {suffix}. Use .parquet, .csv, or .jsonl")


def load_null_thresholds(contract_path: Path) -> dict[str, float]:
    """Extract per-column null rate thresholds from contract YAML."""
    import yaml

    payload = yaml.safe_load(contract_path.read_text(encoding="utf-8")) or {}
    contract = payload.get("dataset_contract", payload)
    columns = contract.get("schema", {}).get("columns", [])

    thresholds: dict[str, float] = {}
    for col in columns:
        name = col.get("name")
        if not name:
            continue
        # nullable: false means threshold = 0.0
        if col.get("nullable") is False:
            thresholds[name] = 0.0
        elif "max_null_rate" in col:
            thresholds[name] = float(col["max_null_rate"])
    return thresholds


def check_null_rate(
    source: Path,
    contract_path: Path | None = None,
    default_threshold: float = 0.0,
) -> dict[str, Any]:
    """Run null rate check and return structured evidence."""
    import pandas as pd

    df = load_dataframe(source)
    total_rows = len(df)

    if total_rows == 0:
        return {
            "check": "null_rate",
            "status": "pass",
            "source": str(source),
            "total_rows": 0,
            "columns_checked": 0,
            "violations": [],
        }

    # Load per-column thresholds from contract
    col_thresholds: dict[str, float] = {}
    if contract_path and contract_path.exists():
        col_thresholds = load_null_thresholds(contract_path)

    violations: list[dict[str, Any]] = []
    column_results: list[dict[str, Any]] = []

    for col in df.columns:
        null_count = int(df[col].isna().sum())
        null_rate = null_count / total_rows
        threshold = col_thresholds.get(col, default_threshold)

        col_result = {
            "column": col,
            "null_count": null_count,
            "null_rate": round(null_rate, 6),
            "threshold": threshold,
            "passed": null_rate <= threshold,
        }
        column_results.append(col_result)

        if null_rate > threshold:
            violations.append({
                "column": col,
                "null_rate": round(null_rate, 6),
                "threshold": threshold,
                "null_count": null_count,
                "excess": round(null_rate - threshold, 6),
            })

    status = "fail" if violations else "pass"

    return {
        "check": "null_rate",
        "status": status,
        "source": str(source),
        "contract": str(contract_path) if contract_path else None,
        "total_rows": total_rows,
        "columns_checked": len(column_results),
        "columns_passing": len([c for c in column_results if c["passed"]]),
        "violations": violations,
        "column_details": column_results,
    }


def main() -> int:
    args = parse_args()
    result = check_null_rate(args.source, args.contract, args.threshold)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
