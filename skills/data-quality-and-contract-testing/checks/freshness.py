#!/usr/bin/env python3
"""Check data freshness against an SLA threshold.

Data freshness is the gap between the most recent record timestamp in a
dataset and the current wall-clock time.  Stale data indicates upstream
pipeline failures, scheduling issues, or source system outages.

This check finds the maximum timestamp in a specified column and compares
the staleness against the SLA (in minutes) from a contract or CLI param.

Usage:
    python checks/freshness.py --source data.csv --timestamp-column updated_at --sla-minutes 60
    python checks/freshness.py --source data.parquet --contract contract.yaml
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check data freshness against SLA threshold."
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to data file (parquet, csv, or jsonl).",
    )
    parser.add_argument(
        "--timestamp-column",
        help="Column containing the event/update timestamp. Auto-detected if not set.",
    )
    parser.add_argument(
        "--sla-minutes",
        type=float,
        help="Maximum allowed staleness in minutes. Overrides contract value.",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        help="Path to dataset contract YAML with freshness_sla defined.",
    )
    parser.add_argument(
        "--now",
        help="Override current time (ISO format) for testing. Default: UTC now.",
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


def load_freshness_sla(contract_path: Path) -> tuple[float | None, str | None]:
    """Extract freshness SLA (minutes) and timestamp column from contract."""
    import yaml

    payload = yaml.safe_load(contract_path.read_text(encoding="utf-8")) or {}
    contract = payload.get("dataset_contract", payload)

    sla = contract.get("freshness_sla", {})
    sla_minutes = None
    ts_column = None

    if isinstance(sla, dict):
        if "max_delay_minutes" in sla:
            sla_minutes = float(sla["max_delay_minutes"])
        elif "max_delay_hours" in sla:
            sla_minutes = float(sla["max_delay_hours"]) * 60
        ts_column = sla.get("timestamp_column")
    elif isinstance(sla, (int, float)):
        sla_minutes = float(sla)

    return sla_minutes, ts_column


def detect_timestamp_column(df: "Any") -> str | None:
    """Auto-detect the most likely timestamp column."""
    import pandas as pd

    candidates = ["updated_at", "created_at", "event_time", "timestamp", "ts", "load_ts"]
    for col in candidates:
        if col in df.columns:
            return col
    # Fall back to first datetime column
    datetime_cols = df.select_dtypes(include=["datetime64", "datetimetz"]).columns
    if len(datetime_cols) > 0:
        return str(datetime_cols[0])
    return None


def check_freshness(
    source: Path,
    timestamp_column: str | None = None,
    sla_minutes: float | None = None,
    contract_path: Path | None = None,
    now_override: str | None = None,
) -> dict[str, Any]:
    """Run freshness check and return structured evidence."""
    import pandas as pd

    df = load_dataframe(source)
    total_rows = len(df)

    if total_rows == 0:
        return {
            "check": "freshness",
            "status": "error",
            "source": str(source),
            "error": "Dataset is empty — cannot determine freshness.",
        }

    # Resolve SLA from contract if not provided
    if contract_path and contract_path.exists() and sla_minutes is None:
        contract_sla, contract_ts_col = load_freshness_sla(contract_path)
        if contract_sla is not None:
            sla_minutes = contract_sla
        if contract_ts_col and not timestamp_column:
            timestamp_column = contract_ts_col

    if sla_minutes is None:
        sla_minutes = 60.0  # default 1 hour

    # Detect timestamp column
    if not timestamp_column:
        timestamp_column = detect_timestamp_column(df)
    if not timestamp_column or timestamp_column not in df.columns:
        return {
            "check": "freshness",
            "status": "error",
            "source": str(source),
            "error": f"Timestamp column '{timestamp_column}' not found. Available: {list(df.columns)}",
        }

    # Parse timestamps
    ts_series = pd.to_datetime(df[timestamp_column], errors="coerce", utc=True)
    valid_count = int(ts_series.notna().sum())
    if valid_count == 0:
        return {
            "check": "freshness",
            "status": "error",
            "source": str(source),
            "error": f"No valid timestamps in column '{timestamp_column}'.",
        }

    max_ts = ts_series.max()

    # Current time
    if now_override:
        now = pd.Timestamp(now_override, tz="UTC")
    else:
        now = pd.Timestamp.now(tz="UTC")

    staleness_minutes = (now - max_ts).total_seconds() / 60.0
    status = "pass" if staleness_minutes <= sla_minutes else "fail"

    return {
        "check": "freshness",
        "status": status,
        "source": str(source),
        "timestamp_column": timestamp_column,
        "sla_minutes": sla_minutes,
        "staleness_minutes": round(staleness_minutes, 2),
        "max_timestamp": str(max_ts),
        "check_time": str(now),
        "total_rows": total_rows,
        "valid_timestamps": valid_count,
        "headroom_minutes": round(sla_minutes - staleness_minutes, 2),
    }


def main() -> int:
    args = parse_args()
    result = check_freshness(
        source=args.source,
        timestamp_column=args.timestamp_column,
        sla_minutes=args.sla_minutes,
        contract_path=args.contract,
        now_override=args.now,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
