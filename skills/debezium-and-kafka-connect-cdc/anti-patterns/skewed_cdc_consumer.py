#!/usr/bin/env python3
"""
ANTI-PATTERN: Hot-Key Skew in CDC Consumer Partitioning
========================================================

Problem:
    This consumer partitions CDC events by customer_id for parallel processing.
    However, approximately 40% of all CDC events originate from a single
    customer: 'BULK_IMPORT'. This creates a severe hot-key skew where one
    consumer instance processes 40% of all traffic while other instances
    sit idle.

Symptoms:
    - One consumer group member has 10-50x higher lag than peers
    - Processing latency spikes despite available consumer capacity
    - Kafka consumer rebalances triggered by slow member timeouts
    - Uneven partition assignment shows one partition with 40% of messages

Expected Diagnosis:
    The agent should flag: "consumer groups by customer_id but 40% of events
    are from customer 'BULK_IMPORT'" and recommend:
    1. Use a composite partition key (customer_id + entity_id) to spread load
    2. Route BULK_IMPORT events to a dedicated consumer group
    3. Apply sub-partitioning or salting for known hot keys
    4. Monitor partition lag distribution, not just aggregate lag

Root Cause:
    Choosing customer_id as the partition key without analyzing the key
    distribution in the CDC stream. Business processes like bulk imports,
    system migrations, or automated reconciliation generate disproportionate
    event volumes under a single key.

Fix Pattern:
    - Analyze key cardinality and distribution before choosing partition keys
    - Use composite keys or hash-based sub-partitioning for even distribution
    - Isolate known bulk producers into separate topics or consumer groups
    - Add monitoring for per-partition lag and throughput skew
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CDCEvent:
    """Represents a Debezium CDC change event."""
    event_id: str
    customer_id: str
    entity_id: str
    operation: str  # c=create, u=update, d=delete
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp_ms: int = 0


class SkewedCDCConsumer:
    """A CDC consumer that partitions by customer_id — exhibiting hot-key skew.

    This consumer assigns events to processing slots based solely on
    customer_id. When a single customer generates a disproportionate
    share of events, the assigned slot becomes a bottleneck.
    """

    def __init__(self, num_partitions: int = 8):
        self.num_partitions = num_partitions
        self.partition_counts: dict[int, int] = {i: 0 for i in range(num_partitions)}
        self.processed_events: list[CDCEvent] = []
        self.processing_times_ms: dict[int, float] = {i: 0.0 for i in range(num_partitions)}

    def assign_partition(self, event: CDCEvent) -> int:
        """Assign event to a partition based on customer_id only.

        BUG: This causes hot-key skew because BULK_IMPORT events
        all route to the same partition.
        """
        # Deterministic hash-based assignment by customer_id
        key_hash = hashlib.md5(event.customer_id.encode()).hexdigest()
        return int(key_hash, 16) % self.num_partitions

    def process_event(self, event: CDCEvent) -> None:
        """Process a single CDC event through the skewed consumer."""
        partition = self.assign_partition(event)
        self.partition_counts[partition] += 1

        # Simulate processing time (bulk events are same cost per event)
        processing_time_ms = 5.0  # 5ms per event
        self.processing_times_ms[partition] += processing_time_ms
        self.processed_events.append(event)

    def get_skew_report(self) -> dict[str, Any]:
        """Report partition distribution showing the skew problem."""
        total_events = sum(self.partition_counts.values())
        if total_events == 0:
            return {"total_events": 0, "partitions": {}}

        max_partition = max(self.partition_counts, key=self.partition_counts.get)  # type: ignore[arg-type]
        max_count = self.partition_counts[max_partition]
        ideal_count = total_events / self.num_partitions
        skew_ratio = max_count / ideal_count if ideal_count > 0 else 0

        return {
            "total_events": total_events,
            "num_partitions": self.num_partitions,
            "partition_distribution": dict(self.partition_counts),
            "hottest_partition": max_partition,
            "hottest_partition_count": max_count,
            "hottest_partition_pct": round(max_count / total_events * 100, 1),
            "ideal_per_partition": round(ideal_count, 1),
            "skew_ratio": round(skew_ratio, 2),
            "diagnosis": (
                f"Partition {max_partition} handles {max_count}/{total_events} events "
                f"({round(max_count / total_events * 100, 1)}%). "
                f"Skew ratio: {round(skew_ratio, 2)}x ideal."
            ),
        }


def generate_realistic_workload(num_events: int = 1000) -> list[CDCEvent]:
    """Generate a CDC event stream with realistic hot-key skew.

    ~40% of events come from 'BULK_IMPORT' customer — a system account
    that handles automated data loads, migrations, and reconciliation.
    """
    import random

    random.seed(42)

    # Distribution: 40% BULK_IMPORT, 60% spread across 200 normal customers
    normal_customers = [f"customer_{i:04d}" for i in range(200)]
    events: list[CDCEvent] = []

    for i in range(num_events):
        if random.random() < 0.40:
            customer_id = "BULK_IMPORT"
        else:
            customer_id = random.choice(normal_customers)

        events.append(CDCEvent(
            event_id=f"evt_{i:06d}",
            customer_id=customer_id,
            entity_id=f"entity_{random.randint(1, 50000):05d}",
            operation=random.choice(["c", "u", "u", "u", "d"]),
            payload={"amount": round(random.uniform(10, 10000), 2)},
            timestamp_ms=int(time.time() * 1000) + i,
        ))

    return events


def main() -> int:
    """Demonstrate the hot-key skew anti-pattern."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: Hot-Key Skew in CDC Consumer")
    print("=" * 70)
    print()

    consumer = SkewedCDCConsumer(num_partitions=8)
    events = generate_realistic_workload(num_events=1000)

    # Process all events
    for event in events:
        consumer.process_event(event)

    # Report the skew
    report = consumer.get_skew_report()
    print(json.dumps(report, indent=2))
    print()
    print("DIAGNOSIS: Consumer groups by customer_id but 40% of events")
    print("are from customer 'BULK_IMPORT', creating a hot partition.")
    print()
    print("FIX: Use composite key (customer_id + entity_id) or route")
    print("BULK_IMPORT to a dedicated consumer group.")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
