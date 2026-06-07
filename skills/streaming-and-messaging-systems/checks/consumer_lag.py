#!/usr/bin/env python3
"""Check consumer group lag against a threshold.

Consumer lag measures how far behind a consumer group is from the latest
produced offset.  High lag indicates consumers cannot keep up with the
production rate, leading to stale data, delayed processing, and eventual
broker storage pressure.

This check reads a lag metrics file (JSON) and asserts that per-partition
lag is below a configurable threshold.

Usage:
    python checks/consumer_lag.py --metrics lag.json --threshold 10000
    python checks/consumer_lag.py --metrics lag.json --threshold 5000 --topic orders
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check consumer group lag against threshold."
    )
    parser.add_argument(
        "--metrics",
        required=True,
        type=Path,
        help="Path to lag metrics JSON file.",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=10000,
        help="Maximum acceptable lag per partition. Default: 10000",
    )
    parser.add_argument(
        "--topic",
        help="Filter to a specific topic. Default: check all topics.",
    )
    parser.add_argument(
        "--consumer-group",
        help="Filter to a specific consumer group. Default: check all groups.",
    )
    return parser.parse_args()


def load_lag_metrics(metrics_path: Path) -> dict[str, Any]:
    """Load lag metrics from JSON file.

    Expected format:
    {
        "consumer_groups": [
            {
                "group": "my-group",
                "topic": "orders",
                "partitions": [
                    {"partition": 0, "current_offset": 1000, "end_offset": 1050, "lag": 50},
                    {"partition": 1, "current_offset": 2000, "end_offset": 2200, "lag": 200}
                ]
            }
        ]
    }
    """
    if not metrics_path.exists():
        raise SystemExit(f"Metrics file not found: {metrics_path}")
    data = json.loads(metrics_path.read_text(encoding="utf-8"))
    return data


def check_consumer_lag(
    metrics_path: Path,
    threshold: int = 10000,
    topic_filter: str | None = None,
    group_filter: str | None = None,
) -> dict[str, Any]:
    """Run consumer lag check and return structured evidence."""
    data = load_lag_metrics(metrics_path)
    groups = data.get("consumer_groups", [])

    if not groups:
        return {
            "check": "consumer_lag",
            "status": "error",
            "metrics_file": str(metrics_path),
            "error": "No consumer_groups found in metrics file.",
        }

    # Apply filters
    if topic_filter:
        groups = [g for g in groups if g.get("topic") == topic_filter]
    if group_filter:
        groups = [g for g in groups if g.get("group") == group_filter]

    if not groups:
        return {
            "check": "consumer_lag",
            "status": "error",
            "metrics_file": str(metrics_path),
            "error": f"No matching groups after filter (topic={topic_filter}, group={group_filter}).",
        }

    violations: list[dict[str, Any]] = []
    total_partitions = 0
    total_lag = 0
    max_lag = 0
    max_lag_detail: dict[str, Any] = {}

    for group_info in groups:
        group_name = group_info.get("group", "unknown")
        topic_name = group_info.get("topic", "unknown")
        partitions = group_info.get("partitions", [])

        for part in partitions:
            total_partitions += 1
            lag = part.get("lag", 0)
            total_lag += lag

            if lag > max_lag:
                max_lag = lag
                max_lag_detail = {
                    "group": group_name,
                    "topic": topic_name,
                    "partition": part.get("partition"),
                    "lag": lag,
                }

            if lag > threshold:
                violations.append({
                    "group": group_name,
                    "topic": topic_name,
                    "partition": part.get("partition"),
                    "lag": lag,
                    "threshold": threshold,
                    "excess": lag - threshold,
                })

    status = "fail" if violations else "pass"
    avg_lag = total_lag / total_partitions if total_partitions > 0 else 0

    return {
        "check": "consumer_lag",
        "status": status,
        "metrics_file": str(metrics_path),
        "threshold": threshold,
        "topic_filter": topic_filter,
        "group_filter": group_filter,
        "total_partitions_checked": total_partitions,
        "total_lag": total_lag,
        "average_lag": round(avg_lag, 1),
        "max_lag": max_lag,
        "max_lag_detail": max_lag_detail,
        "violations": violations,
        "partitions_over_threshold": len(violations),
    }


def main() -> int:
    args = parse_args()
    result = check_consumer_lag(
        metrics_path=args.metrics,
        threshold=args.threshold,
        topic_filter=args.topic,
        group_filter=args.consumer_group,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
