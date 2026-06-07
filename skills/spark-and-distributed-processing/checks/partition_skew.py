#!/usr/bin/env python3
"""Analyze partition statistics and flag skewed partitions.

Partition skew occurs when some partitions hold significantly more data than
others.  This leads to stragglers that dominate stage execution time while
most executors sit idle.  Skew is a top cause of slow Spark jobs and is often
caused by hot keys, time-based partitioning with uneven traffic, or poorly
chosen partition columns.

This check reads a partition stats file and flags any partition whose row
count exceeds a configurable ratio above the median.

Usage:
    python checks/partition_skew.py --stats partition_stats.json --ratio 3.0
    python checks/partition_skew.py --stats stats.csv --ratio 5.0
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze partition stats and flag skewed partitions."
    )
    parser.add_argument(
        "--stats",
        required=True,
        type=Path,
        help="Path to partition stats file (JSON or CSV).",
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=3.0,
        help="Skew ratio threshold (partition_size / median_size). Default: 3.0",
    )
    parser.add_argument(
        "--size-column",
        default="row_count",
        help="Column name containing partition size metric. Default: row_count",
    )
    parser.add_argument(
        "--partition-column",
        default="partition_id",
        help="Column name identifying the partition. Default: partition_id",
    )
    return parser.parse_args()


def load_partition_stats(stats_path: Path) -> list[dict[str, Any]]:
    """Load partition stats from JSON or CSV file."""
    if not stats_path.exists():
        raise SystemExit(f"Stats file not found: {stats_path}")

    suffix = stats_path.suffix.lower()
    if suffix == ".json":
        data = json.loads(stats_path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "partitions" in data:
            return data["partitions"]
        if isinstance(data, list):
            return data
        raise SystemExit(f"Unexpected JSON structure in {stats_path}")
    elif suffix == ".csv":
        import pandas as pd
        df = pd.read_csv(stats_path)
        return df.to_dict(orient="records")
    else:
        raise SystemExit(f"Unsupported format: {suffix}. Use .json or .csv")


def check_partition_skew(
    stats_path: Path,
    ratio_threshold: float = 3.0,
    size_column: str = "row_count",
    partition_column: str = "partition_id",
) -> dict[str, Any]:
    """Analyze partition stats and return structured skew evidence."""
    partitions = load_partition_stats(stats_path)

    if not partitions:
        return {
            "check": "partition_skew",
            "status": "error",
            "stats_file": str(stats_path),
            "error": "No partition data found.",
        }

    # Extract sizes
    sizes: list[int] = []
    for part in partitions:
        if size_column not in part:
            return {
                "check": "partition_skew",
                "status": "error",
                "stats_file": str(stats_path),
                "error": f"Column '{size_column}' not found. Available: {list(partitions[0].keys())}",
            }
        sizes.append(int(part[size_column]))

    # Compute statistics
    sorted_sizes = sorted(sizes)
    n = len(sorted_sizes)
    median_size = sorted_sizes[n // 2] if n % 2 == 1 else (sorted_sizes[n // 2 - 1] + sorted_sizes[n // 2]) / 2
    avg_size = sum(sizes) / n
    min_size = min(sizes)
    max_size = max(sizes)
    total_size = sum(sizes)

    if median_size == 0:
        median_size = 1  # Avoid division by zero

    # Identify skewed partitions
    skewed: list[dict[str, Any]] = []
    for part in partitions:
        size = int(part[size_column])
        ratio = size / median_size
        if ratio > ratio_threshold:
            skewed.append({
                "partition": part.get(partition_column, "unknown"),
                "size": size,
                "ratio_to_median": round(ratio, 2),
                "pct_of_total": round(size / total_size * 100, 2),
            })

    # Sort skewed partitions by ratio descending
    skewed.sort(key=lambda x: x["ratio_to_median"], reverse=True)

    status = "fail" if skewed else "pass"

    # Compute Gini coefficient (inequality measure)
    gini = _gini_coefficient(sizes)

    return {
        "check": "partition_skew",
        "status": status,
        "stats_file": str(stats_path),
        "ratio_threshold": ratio_threshold,
        "total_partitions": n,
        "total_rows": total_size,
        "statistics": {
            "min": min_size,
            "max": max_size,
            "median": median_size,
            "average": round(avg_size, 1),
            "max_to_median_ratio": round(max_size / median_size, 2),
            "gini_coefficient": round(gini, 4),
        },
        "skewed_partitions": skewed,
        "skewed_partition_count": len(skewed),
        "data_in_skewed_pct": round(
            sum(s["size"] for s in skewed) / total_size * 100, 2
        ) if skewed else 0.0,
    }


def _gini_coefficient(values: list[int]) -> float:
    """Compute the Gini coefficient (0=perfect equality, 1=max inequality)."""
    n = len(values)
    if n == 0:
        return 0.0
    sorted_vals = sorted(values)
    cumulative = 0.0
    total = sum(sorted_vals)
    if total == 0:
        return 0.0
    for i, val in enumerate(sorted_vals):
        cumulative += val
    # Gini formula
    numerator = sum((2 * (i + 1) - n - 1) * v for i, v in enumerate(sorted_vals))
    return numerator / (n * total)


def main() -> int:
    args = parse_args()
    result = check_partition_skew(
        stats_path=args.stats,
        ratio_threshold=args.ratio,
        size_column=args.size_column,
        partition_column=args.partition_column,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
