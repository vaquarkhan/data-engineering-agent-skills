#!/usr/bin/env python3
"""Estimate the cost of a backfill operation.

Before approving a backfill, teams need a cost estimate to avoid surprise
bills.  This check takes a backfill plan YAML and multiplies partitions by
a cost-per-partition parameter to produce an estimated total cost.  It can
also factor in compute duration and data scan costs.

Usage:
    python checks/cost_estimate.py --plan backfill-plan.yaml --cost-per-partition 0.50
    python checks/cost_estimate.py --plan backfill-plan.yaml --cost-per-partition 1.20 --max-cost 500
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate cost of a backfill plan."
    )
    parser.add_argument(
        "--plan",
        required=True,
        type=Path,
        help="Path to backfill plan YAML.",
    )
    parser.add_argument(
        "--cost-per-partition",
        type=float,
        default=0.50,
        help="Cost per partition in dollars (compute + storage). Default: $0.50",
    )
    parser.add_argument(
        "--cost-per-gb-scanned",
        type=float,
        default=0.005,
        help="Cost per GB of data scanned. Default: $0.005",
    )
    parser.add_argument(
        "--max-cost",
        type=float,
        default=1000.0,
        help="Maximum acceptable cost before requiring approval. Default: $1000",
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
    """Estimate the number of partitions from the plan."""
    if "partitions" in plan and isinstance(plan["partitions"], list):
        return len(plan["partitions"])

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

    return plan.get("partition_count", plan.get("estimated_partitions", 0))


def _parse_date(date_str: str) -> datetime | None:
    """Parse a date string."""
    for fmt in ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y/%m/%d", "%Y%m%d"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def check_cost_estimate(
    plan_path: Path,
    cost_per_partition: float = 0.50,
    cost_per_gb_scanned: float = 0.005,
    max_cost: float = 1000.0,
) -> dict[str, Any]:
    """Estimate backfill cost and return structured evidence."""
    plan = load_backfill_plan(plan_path)

    target_table = plan.get("target_table", plan.get("table", "unknown"))
    partition_count = estimate_partitions(plan)
    size_per_partition_mb = plan.get("size_per_partition_mb", plan.get("avg_partition_size_mb", 100))

    # Cost calculations
    compute_cost = partition_count * cost_per_partition
    total_data_gb = (partition_count * size_per_partition_mb) / 1024
    scan_cost = total_data_gb * cost_per_gb_scanned
    total_cost = compute_cost + scan_cost

    # Estimate duration (rough: 2 minutes per partition with parallelism of 10)
    parallelism = plan.get("parallelism", plan.get("concurrency", 10))
    minutes_per_partition = plan.get("minutes_per_partition", 2)
    estimated_duration_minutes = (partition_count * minutes_per_partition) / parallelism

    # Status
    exceeds_budget = total_cost > max_cost
    status = "fail" if exceeds_budget else "pass"

    return {
        "check": "cost_estimate",
        "status": status,
        "plan_file": str(plan_path),
        "target_table": target_table,
        "partition_count": partition_count,
        "cost_breakdown": {
            "cost_per_partition": cost_per_partition,
            "compute_cost": round(compute_cost, 2),
            "cost_per_gb_scanned": cost_per_gb_scanned,
            "data_scanned_gb": round(total_data_gb, 2),
            "scan_cost": round(scan_cost, 2),
            "total_estimated_cost": round(total_cost, 2),
        },
        "max_cost_allowed": max_cost,
        "exceeds_budget": exceeds_budget,
        "over_budget_by": round(total_cost - max_cost, 2) if exceeds_budget else 0,
        "duration_estimate": {
            "parallelism": parallelism,
            "minutes_per_partition": minutes_per_partition,
            "estimated_minutes": round(estimated_duration_minutes, 1),
            "estimated_hours": round(estimated_duration_minutes / 60, 2),
        },
        "recommendation": (
            f"Estimated cost ${total_cost:.2f} exceeds budget ${max_cost:.2f}. "
            f"Consider reducing partition range or requesting budget approval."
            if exceeds_budget
            else f"Estimated cost ${total_cost:.2f} is within budget ${max_cost:.2f}."
        ),
    }


def main() -> int:
    args = parse_args()
    result = check_cost_estimate(
        plan_path=args.plan,
        cost_per_partition=args.cost_per_partition,
        cost_per_gb_scanned=args.cost_per_gb_scanned,
        max_cost=args.max_cost,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
