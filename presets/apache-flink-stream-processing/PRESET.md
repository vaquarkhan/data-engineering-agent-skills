---
name: apache-flink-stream-processing
description: Adapts the core skills for Apache Flink-centered stream processing. Use when the primary engine is Apache Flink for event-time processing, stateful streaming, checkpoints, and replay-aware data pipelines.
---

# Apache Flink Stream Processing

## Overview

Use this preset when `Apache Flink` is the core stream-processing engine. It maps shared workflows to event-time semantics, checkpoints, state management, replay safety, and sink correctness.

## Use When

- building stateful stream processing jobs with `Apache Flink`
- managing windows, watermarks, and event-time logic
- implementing checkpoint-aware real-time pipelines
- writing to analytical or operational sinks from Flink jobs

## Preferred Platform Services

- processing: `Apache Flink`
- messaging: `Apache Kafka` or compatible stream brokers
- state and recovery: Flink checkpoints and savepoints
- orchestration: external job scheduling and deployment control
- monitoring: Flink runtime metrics and centralized observability

## Design Rules

- Treat time semantics and replay behavior as core architecture.
- Make checkpointing, savepoints, and state recovery explicit.
- Design sink behavior for idempotency or controlled exactly-once semantics.
- Keep schema evolution and event contract management visible to consumers.

## Verification

- [ ] Watermarks, windows, and state behavior are defined
- [ ] Checkpoint and recovery strategy is documented
- [ ] Sink guarantees and replay behavior are explicit
- [ ] Monitoring covers lag, failures, and checkpoint health
