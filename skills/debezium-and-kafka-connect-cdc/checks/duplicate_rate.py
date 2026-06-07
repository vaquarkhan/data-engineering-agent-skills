#!/usr/bin/env python3
"""Check for duplicate records by business key in a CDC dataset.

This check validates that a CDC-consumed dataset does not contain duplicate
records beyond an acceptable threshold.  Debezium provides at-least-once
delivery semantics, so downstream consumers must deduplicate.  This script
provides evidence that deduplication is working correctly (or flags when it
is not).

Usage:
    python checks/duplicate_rate.py --source data.parquet --key order_id --threshold 0.001
    python checks/duplicate_rate.py --source data.csv --key customer_id,order_id
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check duplicate rate by business key in a CDC dataset."
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to data file (parquet, csv, or jsonl).",
    )
    parser.add_argument(
        "--key",
        required=True,
        help="Comma-separated business key column(s).",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="Acceptable duplicate rate (0.0 = no duplicates allowed). Default: 0.0",
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


def check_duplicates(source: Path, key_columns: list[str], threshold: float) -> dict[str, Any]:
    """Run duplicate rate check and return structured evidence."""
    import pandas as pd

    df = load_dataframe(source)
    total_rows = len(df)

    if total_rows == 0:
        return {
            "check": "duplicate_rate",
            "status": "pass",
            "source": str(source),
            "key_columns": key_columns,
            "threshold": threshold,
            "total_rows": 0,
            "duplicate_count": 0,
            "duplicate_rate": 0.0,
            "sample_duplicates": [],
        }

    # Validate that key columns exist
    missing_columns = [col for col in key_columns if col not in df.columns]
    if missing_columns:
        return {
            "check": "duplicate_rate",
            "status": "error",
            "source": str(source),
            "key_columns": key_columns,
            "threshold": threshold,
            "total_rows": total_rows,
            "error": f"Key columns not found in data: {missing_columns}",
            "available_columns": list(df.columns),
        }

    # Find duplicates
    duplicated_mask = df.duplicated(subset=key_columns, keep=False)
    duplicate_rows = df[duplicated_mask]
    # Count unique duplicate keys (each group counted once minus one row)
    duplicate_count = int(df.duplicated(subset=key_columns, keep="first").sum())
    duplicate_rate = duplicate_count / total_rows if total_rows > 0 else 0.0

    # Sample duplicates for evidence
    sample_duplicates: list[dict[str, Any]] = []
    if duplicate_count > 0:
        # Get up to 5 sample duplicate groups
        sample_keys = (
            duplicate_rows.drop_duplicates(subset=key_columns)
            .head(5)[key_columns]
        )
        for _, key_row in sample_keys.iterrows():
            key_filter = pd.Series([True] * len(df))
            for col in key_columns:
                key_filter = key_filter & (df[col] == key_row[col])
            group = df[key_filter]
            sample_duplicates.append({
                "key": {col: _serialize(key_row[col]) for col in key_columns},
                "occurrences": len(group),
            })

    status = "pass" if duplicate_rate <= threshold else "fail"

    return {
        "check": "duplicate_rate",
        "status": status,
        "source": str(source),
        "key_columns": key_columns,
        "threshold": threshold,
        "total_rows": total_rows,
        "duplicate_count": duplicate_count,
        "duplicate_rate": round(duplicate_rate, 6),
        "sample_duplicates": sample_duplicates,
    }


def _serialize(value: Any) -> Any:
    """Make a value JSON-serializable."""
    import numpy as np

    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, (np.bool_,)):
        return bool(value)
    return value


def main() -> int:
    args = parse_args()
    key_columns = [k.strip() for k in args.key.split(",")]
    result = check_duplicates(args.source, key_columns, args.threshold)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
