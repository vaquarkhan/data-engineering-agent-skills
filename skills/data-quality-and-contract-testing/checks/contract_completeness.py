#!/usr/bin/env python3
"""Validate that a dataset contract YAML has all required fields.

A complete dataset contract must define ownership, description, schema with
typed columns, freshness SLA, and quality rules.  Incomplete contracts lead
to ambiguous expectations between producers and consumers, making it
impossible to enforce quality gates or alert on SLA breaches.

Usage:
    python checks/contract_completeness.py --contract contract.yaml
    python checks/contract_completeness.py --contract contracts/orders.yaml --strict
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = ["owner", "description", "schema", "freshness_sla"]
REQUIRED_SCHEMA_FIELDS = ["columns"]
REQUIRED_COLUMN_FIELDS = ["name", "type"]
OPTIONAL_BUT_RECOMMENDED = ["quality_rules", "retention", "classification"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate dataset contract YAML completeness."
    )
    parser.add_argument(
        "--contract",
        required=True,
        type=Path,
        help="Path to the dataset contract YAML.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help="Require optional-but-recommended fields (quality_rules, retention).",
    )
    return parser.parse_args()


def load_contract(contract_path: Path) -> dict[str, Any]:
    """Load and return the contract dict from YAML."""
    import yaml

    if not contract_path.exists():
        raise SystemExit(f"Contract file not found: {contract_path}")
    payload = yaml.safe_load(contract_path.read_text(encoding="utf-8")) or {}
    return payload.get("dataset_contract", payload)


def check_contract_completeness(contract_path: Path, strict: bool = False) -> dict[str, Any]:
    """Validate contract completeness and return structured evidence."""
    contract = load_contract(contract_path)

    missing_fields: list[str] = []
    warnings: list[str] = []
    column_issues: list[dict[str, Any]] = []

    # Check required top-level fields
    for field in REQUIRED_TOP_LEVEL:
        if field not in contract or contract[field] is None:
            missing_fields.append(field)

    # Check schema structure
    schema = contract.get("schema", {})
    if isinstance(schema, dict):
        columns = schema.get("columns", [])
        if not columns:
            missing_fields.append("schema.columns")
        else:
            for idx, col in enumerate(columns):
                col_missing = [f for f in REQUIRED_COLUMN_FIELDS if f not in col]
                if col_missing:
                    column_issues.append({
                        "index": idx,
                        "column": col.get("name", f"<unnamed-{idx}>"),
                        "missing_fields": col_missing,
                    })
    else:
        missing_fields.append("schema (must be a mapping)")

    # Check quality_rules
    quality_rules = contract.get("quality_rules", [])
    if not quality_rules:
        if strict:
            missing_fields.append("quality_rules")
        else:
            warnings.append("quality_rules not defined (recommended)")

    # Check optional-but-recommended in strict mode
    if strict:
        for field in OPTIONAL_BUT_RECOMMENDED:
            if field not in contract or not contract[field]:
                if field not in missing_fields:
                    missing_fields.append(field)

    # Determine status
    has_critical_missing = any(
        f in missing_fields for f in REQUIRED_TOP_LEVEL + ["schema.columns"]
    )
    status = "fail" if has_critical_missing or column_issues else "pass"

    return {
        "check": "contract_completeness",
        "status": status,
        "contract": str(contract_path),
        "strict_mode": strict,
        "missing_fields": missing_fields,
        "column_issues": column_issues,
        "warnings": warnings,
        "fields_present": [f for f in REQUIRED_TOP_LEVEL if f not in missing_fields],
        "total_columns": len(contract.get("schema", {}).get("columns", [])),
    }


def main() -> int:
    args = parse_args()
    result = check_contract_completeness(args.contract, strict=args.strict)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
