#!/usr/bin/env python3
"""
ANTI-PATTERN: CDC Consumer Without Deduplication
=================================================

Problem:
    This consumer processes CDC events from Debezium without any deduplication
    logic.  Debezium provides at-least-once delivery semantics, meaning the
    same event can be delivered multiple times during:
    - Consumer rebalances
    - Connector restarts
    - Kafka broker failovers
    - Network partitions and retries
    - Re-snapshots after slot/binlog loss

    Without deduplication, replayed events cause double-counting in aggregates,
    duplicate inserts in downstream tables, and incorrect state in materialized
    views.

Symptoms:
    - Aggregate metrics (revenue, counts) are inflated after connector restarts
    - Downstream tables contain duplicate rows with identical business keys
    - Event counts in the target exceed source database row counts
    - Periodic spikes in processed event counts without corresponding source activity

Expected Diagnosis:
    The agent should identify:
    1. No dedup/idempotency mechanism in the consumer
    2. Replayed events are processed as if they are new
    3. Aggregates accumulate without checking for prior processing

Expected Fix:
    - Maintain a processed event log (event_id or LSN/offset dedup table)
    - Use upsert/merge semantics instead of blind inserts
    - Track consumer offsets atomically with processing (exactly-once pattern)
    - For aggregates, use idempotent operations (SET instead of INCREMENT)

Root Cause:
    Assuming Kafka provides exactly-once delivery to consumers. In reality,
    Debezium + Kafka provides at-least-once. The consumer must handle
    deduplication or use idempotent processing patterns.
"""
from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CDCEvent:
    """Represents a Debezium CDC change event."""
    event_id: str
    table: str
    operation: str  # c=create, u=update, d=delete
    key: dict[str, Any] = field(default_factory=dict)
    before: dict[str, Any] | None = None
    after: dict[str, Any] | None = None
    source_lsn: int = 0
    timestamp_ms: int = 0


class NoDedupConsumer:
    """A CDC consumer that processes every event without deduplication.

    BUG: When events are replayed (due to rebalance, restart, or re-snapshot),
    this consumer processes them again, causing double-counting and duplicate
    inserts.
    """

    def __init__(self):
        self.revenue_total: float = 0.0
        self.order_count: int = 0
        self.processed_events: int = 0
        self.inserted_rows: list[dict[str, Any]] = []

    def process_event(self, event: CDCEvent) -> None:
        """Process a CDC event WITHOUT checking for duplicates.

        BUG: No dedup check. If this event was already processed (replay),
        we will double-count the revenue and insert a duplicate row.
        """
        self.processed_events += 1

        if event.operation == "c" and event.after:
            # Blind insert — no upsert, no dedup check
            self.inserted_rows.append(event.after)

            # Blind accumulate — no idempotency
            amount = event.after.get("amount", 0)
            self.revenue_total += amount
            self.order_count += 1

        elif event.operation == "u" and event.after:
            # Blind insert of update (should be upsert by key)
            self.inserted_rows.append(event.after)

            # Bug: also accumulates on updates if they have amount
            amount = event.after.get("amount", 0)
            self.revenue_total += amount

    def get_state(self) -> dict[str, Any]:
        """Return current consumer state for inspection."""
        return {
            "processed_events": self.processed_events,
            "order_count": self.order_count,
            "revenue_total": round(self.revenue_total, 2),
            "inserted_rows": len(self.inserted_rows),
        }


def simulate_at_least_once_delivery(events: list[CDCEvent], replay_pct: float = 0.1) -> list[CDCEvent]:
    """Simulate at-least-once delivery by replaying a percentage of events.

    This models what happens during a consumer rebalance or connector restart:
    some events that were already delivered get delivered again.
    """
    import random

    random.seed(42)
    delivered: list[CDCEvent] = []

    for event in events:
        delivered.append(event)
        # Simulate replay: ~10% of events get delivered twice
        if random.random() < replay_pct:
            delivered.append(event)  # Duplicate delivery

    return delivered


def generate_order_events(num_orders: int = 100) -> list[CDCEvent]:
    """Generate a stream of order creation CDC events."""
    import random

    random.seed(42)
    events: list[CDCEvent] = []

    for i in range(num_orders):
        order_id = f"ORD-{i + 1:05d}"
        amount = round(random.uniform(25.0, 500.0), 2)

        events.append(CDCEvent(
            event_id=f"evt_{i:06d}",
            table="orders",
            operation="c",
            key={"order_id": order_id},
            after={
                "order_id": order_id,
                "customer_id": f"cust_{random.randint(1, 50):04d}",
                "amount": amount,
                "status": "created",
                "created_at": "2024-01-15T10:00:00Z",
            },
            source_lsn=1000 + i,
            timestamp_ms=int(time.time() * 1000) + i,
        ))

    return events


def main() -> int:
    """Demonstrate the no-dedup anti-pattern with at-least-once delivery."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: CDC Consumer Without Deduplication")
    print("=" * 70)
    print()

    # Generate source events
    source_events = generate_order_events(num_orders=100)
    print(f"Source events generated: {len(source_events)}")

    # Simulate at-least-once delivery (some events replayed)
    delivered_events = simulate_at_least_once_delivery(source_events, replay_pct=0.10)
    replayed_count = len(delivered_events) - len(source_events)
    print(f"Events delivered (with replays): {len(delivered_events)}")
    print(f"Replayed events: {replayed_count}")
    print()

    # Process through the broken consumer
    consumer = NoDedupConsumer()
    for event in delivered_events:
        consumer.process_event(event)

    state = consumer.get_state()

    # Calculate what correct values should be
    correct_revenue = sum(e.after["amount"] for e in source_events if e.after)
    correct_count = len(source_events)

    result = {
        "anti_pattern": "no_dedup_consumer",
        "source_events": len(source_events),
        "delivered_events": len(delivered_events),
        "replayed_events": replayed_count,
        "consumer_state": state,
        "correct_values": {
            "order_count": correct_count,
            "revenue_total": round(correct_revenue, 2),
        },
        "errors": {
            "order_count_inflation": state["order_count"] - correct_count,
            "revenue_inflation": round(state["revenue_total"] - correct_revenue, 2),
            "duplicate_rows": state["inserted_rows"] - correct_count,
        },
        "diagnosis": (
            f"Consumer processed {state['processed_events']} events but only "
            f"{len(source_events)} were unique. Revenue is inflated by "
            f"${round(state['revenue_total'] - correct_revenue, 2)} due to "
            f"replayed events being double-counted."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Implement deduplication using one of:")
    print("  1. Event ID / LSN dedup table (check before processing)")
    print("  2. Upsert/merge by business key (idempotent writes)")
    print("  3. Exactly-once consumer semantics (offset + processing atomic)")
    print("  4. Idempotent aggregates (SET total = X, not total += X)")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
