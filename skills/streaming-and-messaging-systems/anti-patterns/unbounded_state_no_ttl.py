#!/usr/bin/env python3
"""
ANTI-PATTERN: Unbounded State Without TTL in Stream Processor
==============================================================

Problem:
    This stateful stream processor maintains a lookup/dedup state store that
    grows without bound.  No TTL (time-to-live) is configured, no eviction
    policy exists, and no size cap is enforced.  Over time, the state store
    accumulates every key ever seen, leading to memory exhaustion, GC pressure,
    checkpoint bloat, and eventual OOM crashes.

    This is extremely common in Flink, Kafka Streams, and Spark Structured
    Streaming applications that perform deduplication, session windowing, or
    keyed aggregation without configuring state retention.

Symptoms:
    - Steady memory growth over hours/days without stabilization
    - Increasing GC pause times and checkpoint duration
    - OOM kills during peak traffic or after restarts (state restore)
    - Checkpoint sizes growing linearly with runtime duration
    - Recovery time increasing as state grows

Expected Diagnosis:
    The agent should identify:
    1. State store has no TTL or eviction policy
    2. Memory usage grows monotonically with input volume
    3. No mechanism to expire or compact old state entries

Expected Fix:
    - Configure state TTL (e.g., Flink's StateTtlConfig, Kafka Streams store retention)
    - Use windowed state with bounded retention
    - Implement periodic state compaction/eviction
    - Set max entries or max memory caps on state stores
    - Monitor state size as an operational metric with alerts

Root Cause:
    Assuming the key space is bounded when it is not.  For dedup use cases,
    every unique event ID is stored forever.  For session windows, inactive
    sessions are never expired.  The developer focuses on correctness without
    considering operational sustainability over time.
"""
from __future__ import annotations

import json
import sys
import time
from typing import Any


class UnboundedStateProcessor:
    """A stream processor that accumulates state without TTL.

    BUG: The dedup_store and session_store grow without bound.  No eviction,
    no TTL, no size limit.  After processing millions of events, memory
    usage will exceed available heap and crash the process.
    """

    def __init__(self):
        # State stores with NO TTL
        self.dedup_store: dict[str, float] = {}  # event_id -> timestamp
        self.session_store: dict[str, dict[str, Any]] = {}  # user_id -> session
        self.events_processed: int = 0
        self.duplicates_filtered: int = 0
        self.memory_snapshots: list[dict[str, Any]] = []

    def process_event(self, event: dict[str, Any]) -> bool:
        """Process an event with deduplication.

        BUG: Stores every event_id forever. No TTL expiry.
        """
        self.events_processed += 1
        event_id = event["event_id"]

        # Dedup check — stores key FOREVER
        if event_id in self.dedup_store:
            self.duplicates_filtered += 1
            return False  # Duplicate

        # Store in dedup state — NEVER expires
        self.dedup_store[event_id] = event["timestamp"]

        # Update session state — NEVER expires
        user_id = event.get("user_id", "unknown")
        if user_id not in self.session_store:
            self.session_store[user_id] = {
                "first_event": event["timestamp"],
                "last_event": event["timestamp"],
                "event_count": 0,
            }
        session = self.session_store[user_id]
        session["last_event"] = event["timestamp"]
        session["event_count"] += 1

        return True  # Processed

    def snapshot_memory(self, label: str) -> dict[str, Any]:
        """Capture a memory usage snapshot."""
        snapshot = {
            "label": label,
            "dedup_store_keys": len(self.dedup_store),
            "session_store_keys": len(self.session_store),
            "estimated_memory_mb": self._estimate_memory_mb(),
            "events_processed": self.events_processed,
        }
        self.memory_snapshots.append(snapshot)
        return snapshot

    def _estimate_memory_mb(self) -> float:
        """Estimate memory used by state stores (conservative)."""
        # ~100 bytes per dedup entry (key + timestamp + dict overhead)
        dedup_bytes = len(self.dedup_store) * 100
        # ~200 bytes per session entry
        session_bytes = len(self.session_store) * 200
        total_bytes = dedup_bytes + session_bytes
        return round(total_bytes / (1024 * 1024), 2)


def generate_event_stream(num_events: int, num_users: int = 1000) -> list[dict[str, Any]]:
    """Generate a stream of events with unique IDs (simulating real traffic)."""
    import random
    random.seed(42)
    events: list[dict[str, Any]] = []
    base_ts = time.time()

    for i in range(num_events):
        events.append({
            "event_id": f"evt-{i:08d}",
            "user_id": f"user-{random.randint(1, num_users):05d}",
            "action": random.choice(["click", "view", "purchase", "scroll"]),
            "timestamp": base_ts + i * 0.1,
        })

    return events


def main() -> int:
    """Demonstrate unbounded state growth without TTL."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: Unbounded State Without TTL")
    print("=" * 70)
    print()

    processor = UnboundedStateProcessor()

    # Simulate processing events in batches to show growth
    batch_size = 50000
    total_events = 200000
    events = generate_event_stream(total_events, num_users=5000)

    print(f"Simulating {total_events} events across {5000} users...")
    print()

    for batch_start in range(0, total_events, batch_size):
        batch_end = min(batch_start + batch_size, total_events)
        batch = events[batch_start:batch_end]

        for event in batch:
            processor.process_event(event)

        snapshot = processor.snapshot_memory(f"After {batch_end} events")
        print(
            f"  [{snapshot['label']}] "
            f"dedup_keys={snapshot['dedup_store_keys']:,} "
            f"sessions={snapshot['session_store_keys']:,} "
            f"memory~{snapshot['estimated_memory_mb']:.1f}MB"
        )

    print()

    # Show the problem: linear growth, no plateau
    first_snap = processor.memory_snapshots[0]
    last_snap = processor.memory_snapshots[-1]
    growth_rate = (
        (last_snap["estimated_memory_mb"] - first_snap["estimated_memory_mb"])
        / len(processor.memory_snapshots)
    )

    result = {
        "anti_pattern": "unbounded_state_no_ttl",
        "events_processed": processor.events_processed,
        "duplicates_filtered": processor.duplicates_filtered,
        "final_state": {
            "dedup_store_keys": len(processor.dedup_store),
            "session_store_keys": len(processor.session_store),
            "estimated_memory_mb": processor._estimate_memory_mb(),
        },
        "growth_trajectory": processor.memory_snapshots,
        "growth_rate_mb_per_batch": round(growth_rate, 2),
        "projection_24h": {
            "events_per_day": total_events * 12,  # extrapolate
            "estimated_memory_gb": round(processor._estimate_memory_mb() * 12 / 1024, 2),
            "note": "Linear growth - will OOM within hours in production",
        },
        "diagnosis": (
            f"State stores grew linearly to {len(processor.dedup_store):,} dedup keys "
            f"and {len(processor.session_store):,} sessions with no eviction. "
            f"Memory at {processor._estimate_memory_mb():.1f}MB after {total_events:,} events. "
            f"In production with 10x traffic, OOM is inevitable within hours."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Configure TTL on state stores:")
    print("  1. Flink: StateTtlConfig.newBuilder(Time.hours(24)).build()")
    print("  2. Kafka Streams: Stores.persistentWindowStore(..., retentionPeriod)")
    print("  3. Spark: withWatermark() + state timeout")
    print("  4. Monitor state size metrics and alert on growth rate")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
