#!/usr/bin/env python3
"""
ANTI-PATTERN: Calling .collect() on a Large Distributed Dataset
================================================================

Problem:
    This Spark job calls .collect() to pull an entire distributed dataset
    back to the driver node's memory.  The driver has limited heap compared
    to the aggregate memory of the cluster.  When the dataset exceeds driver
    memory, the job crashes with OutOfMemoryError.

    Even when it doesn't crash, .collect() serializes all partitions,
    sends them over the network to a single node, and deserializes them
    into a Python list—destroying all parallelism and negating the purpose
    of distributed processing.

Symptoms:
    - java.lang.OutOfMemoryError: Java heap space on the driver
    - Driver GC thrashing (>50% time in GC) before crash
    - Job succeeds on small data but fails on production volumes
    - Network saturation between executors and driver
    - Spark UI shows all data flowing to a single stage with 1 task

Expected Diagnosis:
    The agent should identify:
    1. .collect() called on a DataFrame/RDD with unbounded or large row count
    2. No pre-filter, limit, or aggregation before collect
    3. Driver memory is orders of magnitude smaller than data size

Expected Fix:
    - Replace .collect() with .write (save results to storage)
    - If sampling is needed, use .take(n) or .limit(n).collect()
    - If aggregating, push aggregation to executors: df.groupBy().agg()
    - For debugging, use .show(n) or .head(n)
    - Set spark.driver.maxResultSize to fail fast instead of OOM

Root Cause:
    Treating a distributed DataFrame as if it were a local collection.
    The developer's mental model is a single-machine pandas workflow
    where all data fits in memory.  In distributed systems, computation
    must go to the data, not data to the computation.
"""
from __future__ import annotations

import json
import sys
import random
from typing import Any


class SimulatedPartition:
    """Simulates a Spark partition with row data."""

    def __init__(self, partition_id: int, rows: list[dict[str, Any]]):
        self.partition_id = partition_id
        self.rows = rows
        self.size_bytes = sum(self._estimate_row_size(r) for r in rows)

    def _estimate_row_size(self, row: dict[str, Any]) -> int:
        """Estimate serialized size of a single row."""
        return sum(len(str(v)) + len(str(k)) + 16 for k, v in row.items())


class SimulatedDataFrame:
    """Simulates a distributed Spark DataFrame for demonstration."""

    def __init__(self, partitions: list[SimulatedPartition]):
        self.partitions = partitions
        self.total_rows = sum(len(p.rows) for p in partitions)
        self.total_bytes = sum(p.size_bytes for p in partitions)

    def collect(self) -> list[dict[str, Any]]:
        """Simulate .collect() — pulls ALL data to the driver.

        BUG: This transfers all partition data to a single node.
        In production, this causes OOM on datasets > driver memory.
        """
        collected: list[dict[str, Any]] = []
        bytes_transferred = 0

        for partition in self.partitions:
            collected.extend(partition.rows)
            bytes_transferred += partition.size_bytes

        return collected

    @property
    def num_partitions(self) -> int:
        return len(self.partitions)


def generate_large_dataset(
    num_partitions: int = 200,
    rows_per_partition: int = 50000,
) -> SimulatedDataFrame:
    """Generate a simulated large distributed dataset."""
    random.seed(42)
    partitions: list[SimulatedPartition] = []

    for pid in range(num_partitions):
        rows: list[dict[str, Any]] = []
        for rid in range(rows_per_partition):
            row_id = pid * rows_per_partition + rid
            rows.append({
                "id": row_id,
                "user_id": f"user-{random.randint(1, 100000):06d}",
                "event_type": random.choice(["click", "view", "purchase", "search"]),
                "amount": round(random.uniform(0.01, 999.99), 2),
                "session_id": f"sess-{random.randint(1, 500000):08d}",
                "timestamp": f"2024-03-{random.randint(1,31):02d}T{random.randint(0,23):02d}:00:00Z",
                "metadata": f"payload-{'x' * random.randint(50, 200)}",
            })
        partitions.append(SimulatedPartition(pid, rows))

    return SimulatedDataFrame(partitions)


def simulate_driver_oom(df: SimulatedDataFrame, driver_memory_mb: int = 4096) -> dict[str, Any]:
    """Simulate what happens when .collect() is called on a large DataFrame."""
    driver_memory_bytes = driver_memory_mb * 1024 * 1024

    # Calculate what would happen
    total_data_mb = df.total_bytes / (1024 * 1024)
    fits_in_driver = df.total_bytes < driver_memory_bytes

    # Simulate partial collection to show growth
    collected_bytes = 0
    partitions_collected = 0
    memory_snapshots: list[dict[str, Any]] = []

    for partition in df.partitions:
        collected_bytes += partition.size_bytes
        partitions_collected += 1

        if partitions_collected % 20 == 0:
            pct_driver_used = (collected_bytes / driver_memory_bytes) * 100
            memory_snapshots.append({
                "partitions_collected": partitions_collected,
                "data_collected_mb": round(collected_bytes / (1024 * 1024), 1),
                "driver_memory_pct": round(pct_driver_used, 1),
            })

        if collected_bytes >= driver_memory_bytes:
            break

    return {
        "would_oom": not fits_in_driver,
        "total_data_mb": round(total_data_mb, 1),
        "driver_memory_mb": driver_memory_mb,
        "data_to_memory_ratio": round(total_data_mb / driver_memory_mb, 2),
        "partitions_before_oom": partitions_collected,
        "total_partitions": df.num_partitions,
        "memory_growth": memory_snapshots,
    }


def main() -> int:
    """Demonstrate the .collect() on large dataset anti-pattern."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: .collect() on Large Distributed Dataset")
    print("=" * 70)
    print()

    # Generate a realistic large dataset
    num_partitions = 200
    rows_per_partition = 50000
    total_rows = num_partitions * rows_per_partition

    print(f"Dataset: {total_rows:,} rows across {num_partitions} partitions")
    print(f"Simulating Spark cluster with 50 executors (8GB each = 400GB total)")
    print(f"Driver memory: 4GB")
    print()

    # Note: we generate a smaller sample to keep demo fast
    df = generate_large_dataset(num_partitions=40, rows_per_partition=5000)
    print(f"Demo dataset: {df.total_rows:,} rows, ~{df.total_bytes / (1024*1024):.1f}MB")
    print()

    # Simulate the OOM scenario
    oom_result = simulate_driver_oom(df, driver_memory_mb=4096)

    print("Memory growth during .collect():")
    for snap in oom_result["memory_growth"]:
        bar_len = int(snap["driver_memory_pct"] / 2)
        bar = "#" * bar_len
        print(f"  Partition {snap['partitions_collected']:3d}: "
              f"{snap['data_collected_mb']:6.1f}MB "
              f"[{bar}] {snap['driver_memory_pct']:.1f}%")
    print()

    # Scale up to production scenario
    production_scale_factor = (num_partitions * rows_per_partition) / df.total_rows
    production_data_mb = (df.total_bytes / (1024 * 1024)) * production_scale_factor

    result = {
        "anti_pattern": "collect_on_driver",
        "demo_results": {
            "rows": df.total_rows,
            "partitions": df.num_partitions,
            "data_size_mb": round(df.total_bytes / (1024 * 1024), 1),
        },
        "production_projection": {
            "rows": total_rows,
            "partitions": num_partitions,
            "data_size_mb": round(production_data_mb, 1),
            "driver_memory_mb": 4096,
            "would_oom": production_data_mb > 4096,
            "overflow_mb": round(production_data_mb - 4096, 1),
        },
        "oom_simulation": oom_result,
        "diagnosis": (
            f".collect() attempts to pull {production_data_mb:.0f}MB into a 4GB driver. "
            f"This is {production_data_mb/4096:.1f}x the available memory. "
            f"The job will OOM after collecting ~{oom_result['partitions_before_oom']} "
            f"of {num_partitions} partitions."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Never use .collect() on unbounded datasets:")
    print("  1. df.write.parquet('output/') - write to distributed storage")
    print("  2. df.limit(1000).collect() - sample safely for debugging")
    print("  3. df.groupBy('key').agg(sum('value')) - aggregate on executors")
    print("  4. df.show(20) - display sample without collecting all")
    print("  5. Set spark.driver.maxResultSize=2g to fail fast")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
