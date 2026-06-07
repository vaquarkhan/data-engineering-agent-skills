#!/usr/bin/env python3
"""Estimate the blast radius of a backfill plan.

Before executing a backfill, operators need to understand the scope of impact:
how many partitions will be reprocessed, approximately how much data will be
touched, and which downstream tables will be affected.  This check reads a
backfill plan YAML and computes these estimates to support informed go/no-go
decisions.

Usage:
    python checks/blast_radius.py --plan backfill-plan.yaml
    python checks/blast_radius.py --plan backfill-plan.yaml --max-partitions 100
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate blast radius of a backfill plan."
    )
    parser.add_argument(
        "--plan",
        required=True,
        type=Path,
        help="Path to backfill plan YAML.",
    )
    parser.add_argument(
        "--max-partitions",
        type=int,
        default=500,
        help="Maximum acceptable partitions to reprocess. Default: 500",
    )
    parser.add_argument(
        "--max-downstream",
        type=int,
        default=20,
        help="Maximum acceptable downstream tables impacted. Default: 20",
    )
    return parser.parse_args()


def load_backfill_plan(plan_path: Path) -> dict[str, Any]:
    """Load and validate a backfill plan YAML."""
    import yaml

    if not plan_path.exists():
        raise SystemExit(f"Backfill plan not found: {plan_path}")
    data = yaml.safe_load(plan_path.read_text(encoding="utf-8")) or {}
    return data.get("backfill_plan", data)


def estimate_partitions(plan: dict[str, Any]) -> int:
    """Estimate the number of partitions affected by the backfill."""
    # Check explicit partition list
    if "partitions" in plan:
        partitions = plan["partitions"]
        if isinstance(partitions, list):
            return len(partitions)

    # Estimate from date range + partition granularity
    start_date = plan.get("start_date") or plan.get("from_date")
    end_date = plan.get("end_date") or plan.get("to_date")
    granularity = plan.get("partition_granularity", plan.get("granularity", "daily"))

    if start_date and end_date:
        start = _parse_date(str(start_date))
        end = _parse_date(str(end_date))
        if start and end:
            days = (end - start).days + 1
            if granularity == "hourly":
                return days * 24
            elif granularity == "daily":
                return days
            elif granularity == "weekly":
                return max(1, days // 7)
            elif granularity == "monthly":
                return max(1, days // 30)
            return days

    # Fallback: check partition_count field
    return plan.get("partition_count", plan.get("estimated_partitions", 0))


def estimate_data_size(plan: dict[str, Any], partition_count: int) -> dict[str, Any]:
    """Estimate total data size from partition count and per-partition estimate."""
    size_per_partition_mb = plan.get("size_per_partition_mb", plan.get("avg_partition_size_mb", 100))
    total_mb = partition_count * size_per_partition_mb
    total_gb = total_mb / 1024

    return {
        "size_per_partition_mb": size_per_partition_mb,
        "total_estimated_mb": round(total_mb, 1),
        "total_estimated_gb": round(total_gb, 2),
    }


def identify_downstream(plan: dict[str, Any]) -> list[str]:
    """Identify downstream tables that will be impacted."""
    downstream = plan.get("downstream_tables", plan.get("downstream", []))
    if isinstance(downstream, list):
        return downstream
    return []


def _parse_date(date_str: str) -> datetime | None:
    """Parse a date string in common formats."""
    for fmt in ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y/%m/%d", "%Y%m%d"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def check_blast_radius(
    plan_path: Path,
    max_partitions: int = 500,
    max_downstream: int = 20,
) -> dict[str, Any]:
    """Analyze backfill plan blast radius and return structured evidence."""
    plan = load_backfill_plan(plan_path)

    target_table = plan.get("target_table", plan.get("table", "unknown"))
    partition_count = estimate_partitions(plan)
    size_estimate = estimate_data_size(plan, partition_count)
    downstream_tables = identify_downstream(plan)

    # Risk assessment
    violations: list[str] = []
    if partition_count > max_partitions:
        violations.append(
            f"Partition count ({partition_count}) exceeds maximum ({max_partitions})"
        )
    if len(downstream_tables) > max_downstream:
        violations.append(
            f"Downstream tables ({len(downstream_tables)}) exceeds maximum ({max_downstream})"
        )

    # Risk level
    if partition_count > max_partitions * 2 or len(downstream_tables) > max_downstream * 2:
        risk_level = "critical"
    elif violations:
        risk_level = "high"
    elif partition_count > max_partitions * 0.7:
        risk_level = "medium"
    else:
        risk_level = "low"

    status = "fail" if violations else "pass"

    return {
        "check": "blast_radius",
        "status": status,
        "plan_file": str(plan_path),
        "target_table": target_table,
        "partition_estimate": partition_count,
        "max_partitions_allowed": max_partitions,
        "data_size_estimate": size_estimate,
        "downstream_tables": downstream_tables,
        "downstream_count": len(downstream_tables),
        "max_downstream_allowed": max_downstream,
        "risk_level": risk_level,
        "violations": violations,
        "recommendation": (
            "Consider breaking into smaller batches"
            if violations
            else "Blast radius within acceptable bounds"
        ),
    }


def main() -> int:
    args = parse_args()
    result = check_blast_radius(
        plan_path=args.plan,
        max_partitions=args.max_partitions,
        max_downstream=args.max_downstream,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
