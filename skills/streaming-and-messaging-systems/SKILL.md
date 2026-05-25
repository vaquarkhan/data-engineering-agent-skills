---
name: streaming-and-messaging-systems
description: Guides agents through event streaming and real-time data pipeline design. Use when working with Kafka, Kinesis, Flink, stream processing, windowing, stateful consumers, or near-real-time publish flows.
---

# Streaming And Messaging Systems

## Overview

Use this skill for continuous data movement and real-time processing. It helps agents design safe event pipelines around brokers and stream processors such as `Kafka`, `Kinesis`, and `Flink`, with attention to ordering, state, replay, schema evolution, and delivery guarantees.

## When to Use

- designing or modifying `Kafka` topics, consumers, or stream processors
- using `Kinesis` for event ingestion or streaming delivery
- implementing `Flink` jobs or stateful stream transformations
- defining near-real-time pipelines, windows, watermarks, and replay behavior
- handling schemas and contracts for event-driven systems

Do not use this when the workload is purely batch and does not require streaming semantics.

## Workflow

1. Define the event contract.
   Include:
   - event key
   - schema and versioning
   - ordering expectations
   - delivery guarantees
   - retention and replay policy

2. Choose the right platform role.
   - `Kafka`: durable event backbone and broad ecosystem
   - `Kinesis`: AWS-native streaming ingestion and transport
   - `Flink`: stateful stream processing and event-time logic

3. Design for state and late data.
   Account for:
   - watermarks
   - windows
   - deduplication
   - exactly-once or at-least-once semantics
   - checkpointing and recovery

4. Make consumer behavior observable.
   Lag, failed checkpoints, poison messages, schema drift, and dead-letter handling should be planned, not discovered in production.

5. Treat replay as a first-class operation.
   Reprocessing events should not depend on manual guesswork.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Streaming just means faster batch." | Streaming introduces ordering, state, replay, and time semantics that batch systems do not have. |
| "We can ignore schema evolution because events are small." | Event size does not reduce contract risk; schema drift can break many downstream consumers. |
| "Exactly-once is automatic." | Delivery semantics depend on end-to-end design, state handling, sinks, and replay behavior. |

## Red Flags

- no explicit event contract or key strategy
- replay and retention are undefined
- time semantics are assumed instead of specified
- consumer lag and dead-letter strategy are missing
- stateful processing has no checkpoint or recovery plan

## Verification

- [ ] Event schema, keys, retention, and replay rules are defined
- [ ] Platform responsibilities are clear across broker and processor layers
- [ ] Time semantics, state, and recovery design are explicit
- [ ] Operational visibility exists for lag, failures, and bad records
