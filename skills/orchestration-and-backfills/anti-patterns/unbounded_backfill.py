#!/usr/bin/env python3
"""
ANTI-PATTERN: Unbounded Backfill Without Partition Bounds
==========================================================

Problem:
    This backfill job runs without any partition bounds (no start_date,
    no end_date, no WHERE clause).  It reprocesses the ENTIRE history of
    the source table — potentially years of data — in a single execution.

    This causes extreme resource consumption, blocks production slots,
    overwhelms downstream systems with sudden massive writes, and creates
    a blast radius that makes rollback nearly impossible.  If the job fails
    midway, there is no clean way to resume because there are no checkpoints.

Symptoms:
    - Backfill job runs for hours/days, consuming all cluster resources
    - Production pipelines are starved of compute during the backfill
    - Downstream tables receive years of data in one write, causing compaction storms
    - Job fails after hours with no way to resume from the failure point
    - Storage costs spike due to rewriting all historical data
    - Monitoring alerts fire across all downstream consumers

Expected Diagnosis:
    The agent should identify:
    1. No partition bounds (date range) in the backfill query
    2. Full table scan without WHERE clause
    3. No batch/chunk mechanism for incremental processing
    4. No checkpoint/resume capability

Expected Fix:
    - Always specify explicit partition bounds (start_date, end_date)
    - Break large backfills into daily/weekly batches
    - Process batches sequentially with checkpoint after each
    - Implement resume capability (skip already-completed partitions)
    - Set resource quotas separate from production workloads
    - Validate blast radius before execution (partition count, data size)

Root Cause:
    Treating a backfill as "just re-running the pipeline" without
    acknowledging that historical data volume is orders of magnitude larger
    than a daily incremental run.  The developer's mental model is a
    single-day pipeline, but the execution covers months or years.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Any


class SourceTable:
    """Simulates a source table with years of historical partitions."""

    def __init__(self, start_date: datetime, end_date: datetime, rows_per_day: int = 50000):
        self.start_date = start_date
        self.end_date = end_date
        self.rows_per_day = rows_per_day
        days = (end_date - start_date).days
        self.total_partitions = days
        self.total_rows = days * rows_per_day
        self.size_per_partition_mb = 150  # Avg 150MB per daily partition
        self.total_size_gb = (days * self.size_per_partition_mb) / 1024


class UnboundedBackfillJob:
    """A backfill job that processes the entire table without bounds.

    BUG: No partition bounds, no batching, no checkpointing.
    Processes all history in one shot.
    """

    def __init__(self, source: SourceTable):
        self.source = source
        self.partitions_processed = 0
        self.rows_processed = 0
        self.elapsed_minutes = 0.0
        self.cost_accumulated = 0.0
        self.cost_per_partition = 1.20  # $1.20 per partition (compute + I/O)

    def execute_unbounded(self) -> dict[str, Any]:
        """Execute backfill with NO bounds — full table scan.

        BUG: Processes ALL partitions from the beginning of time.
        """
        # Simulate processing (we don't actually process, just calculate)
        minutes_per_partition = 3.0  # 3 minutes per daily partition
        parallelism = 10  # 10 parallel slots

        self.partitions_processed = self.source.total_partitions
        self.rows_processed = self.source.total_rows
        self.elapsed_minutes = (self.source.total_partitions * minutes_per_partition) / parallelism
        self.cost_accumulated = self.source.total_partitions * self.cost_per_partition

        return {
            "partitions_processed": self.partitions_processed,
            "rows_processed": self.rows_processed,
            "elapsed_hours": round(self.elapsed_minutes / 60, 1),
            "cost_usd": round(self.cost_accumulated, 2),
        }

    def compare_with_bounded(self, days_needed: int = 7) -> dict[str, Any]:
        """Compare unbounded vs. properly bounded backfill."""
        bounded_partitions = days_needed
        bounded_rows = days_needed * self.source.rows_per_day
        bounded_minutes = (days_needed * 3.0) / 10
        bounded_cost = days_needed * self.cost_per_partition

        return {
            "unbounded": {
                "partitions": self.source.total_partitions,
                "rows": self.source.total_rows,
                "hours": round(self.elapsed_minutes / 60, 1),
                "cost_usd": round(self.cost_accumulated, 2),
                "data_size_gb": round(self.source.total_size_gb, 1),
            },
            "bounded_7_days": {
                "partitions": bounded_partitions,
                "rows": bounded_rows,
                "hours": round(bounded_minutes / 60, 2),
                "cost_usd": round(bounded_cost, 2),
                "data_size_gb": round((days_needed * self.source.size_per_partition_mb) / 1024, 2),
            },
            "waste_factor": {
                "partitions": f"{self.source.total_partitions / bounded_partitions:.0f}x",
                "cost": f"{self.cost_accumulated / bounded_cost:.0f}x",
                "time": f"{self.elapsed_minutes / bounded_minutes:.0f}x",
            },
        }


def main() -> int:
    """Demonstrate the unbounded backfill anti-pattern."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: Unbounded Backfill (No Partition Bounds)")
    print("=" * 70)
    print()

    # Simulate a source table with 3 years of history
    source = SourceTable(
        start_date=datetime(2021, 1, 1, tzinfo=timezone.utc),
        end_date=datetime(2024, 3, 15, tzinfo=timezone.utc),
        rows_per_day=50000,
    )

    print(f"Source table history: {source.start_date.date()} to {source.end_date.date()}")
    print(f"Total partitions: {source.total_partitions:,}")
    print(f"Total rows: {source.total_rows:,}")
    print(f"Total size: {source.total_size_gb:.1f} GB")
    print()

    # Execute unbounded backfill
    job = UnboundedBackfillJob(source)
    execution = job.execute_unbounded()

    print("UNBOUNDED BACKFILL EXECUTION (no date bounds):")
    print(f"  Partitions reprocessed: {execution['partitions_processed']:,}")
    print(f"  Rows reprocessed: {execution['rows_processed']:,}")
    print(f"  Estimated duration: {execution['elapsed_hours']} hours")
    print(f"  Estimated cost: ${execution['cost_usd']:,.2f}")
    print()

    # Compare with proper bounded backfill
    comparison = job.compare_with_bounded(days_needed=7)
    print("COMPARISON (unbounded vs. bounded 7-day backfill):")
    print(f"  Partitions: {comparison['unbounded']['partitions']:,} vs {comparison['bounded_7_days']['partitions']}")
    print(f"  Cost: ${comparison['unbounded']['cost_usd']:,.2f} vs ${comparison['bounded_7_days']['cost_usd']:.2f}")
    print(f"  Time: {comparison['unbounded']['hours']}h vs {comparison['bounded_7_days']['hours']}h")
    print(f"  Waste factor: {comparison['waste_factor']['cost']} cost, {comparison['waste_factor']['time']} time")
    print()

    result = {
        "anti_pattern": "unbounded_backfill",
        "source_table": {
            "history_start": str(source.start_date.date()),
            "history_end": str(source.end_date.date()),
            "total_partitions": source.total_partitions,
            "total_rows": source.total_rows,
            "total_size_gb": round(source.total_size_gb, 1),
        },
        "unbounded_execution": execution,
        "comparison": comparison,
        "risks": [
            "Cluster resource starvation for production workloads",
            "No checkpoint — failure at 80% means starting over",
            "Downstream compaction storm from massive write volume",
            "No rollback strategy for partially-completed backfill",
            "Budget overrun without approval",
        ],
        "diagnosis": (
            f"Backfill processes ALL {source.total_partitions:,} partitions "
            f"({source.total_size_gb:.0f}GB) when only 7 days were needed. "
            f"This wastes {comparison['waste_factor']['cost']} in compute cost "
            f"and takes {comparison['waste_factor']['time']} longer than necessary."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Always bound backfills with explicit partition ranges:")
    print("  1. Specify --start-date and --end-date (never omit both)")
    print("  2. Break into daily/weekly batches with checkpoint per batch")
    print("  3. Validate blast radius before execution (partitions, cost, duration)")
    print("  4. Run on dedicated resource pool (not production cluster)")
    print("  5. Implement resume: skip partitions already successfully processed")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
