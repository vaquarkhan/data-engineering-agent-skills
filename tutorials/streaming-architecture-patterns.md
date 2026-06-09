# Tutorial: Applying Streaming Architecture Patterns

This tutorial explains how to choose and apply common streaming patterns for durable, replay-safe, and operationally sane data platforms.

## Goal

By the end of this tutorial, you should be able to:

- distinguish event backbone, CDC, enrichment, and serving responsibilities
- choose the right streaming pattern for durability, replay, and low-latency needs
- validate duplicate handling, DLQ behavior, late data, and state recovery
- connect the streaming design to contracts, observability, and incident recovery

## Step 1: Decide What The Stream Represents

Before choosing the processing pattern, define whether the stream is:

- a canonical business-event backbone
- a CDC feed from an operational database
- a derived enrichment stream
- a low-latency serving input

This matters because replay, ownership, and contract requirements differ for each.

Use `references/streaming-architecture-patterns.md` as the primary guide.

## Step 2: Choose The Right Pattern

### Event Backbone Versus Derived Streams

Choose this pattern when:

- multiple consumers need the same durable event source
- enrichment should not mutate the original event history
- replay depends on a stable source-of-record topic

### CDC Or Outbox To Streaming

Choose this pattern when:

- operational database changes must become events
- ordering and transaction boundaries matter
- dual writes from request handlers would be unsafe

### Idempotent Consumer And Replay-Safe Sink

Choose this pattern when:

- stream consumers write to warehouses, indexes, or serving tables
- retry and replay are expected parts of operations
- duplicate prevention is a hard requirement

### Dead-Letter And Poison Message Isolation

Choose this pattern when:

- malformed or incompatible records are realistic
- operators need visibility into permanent versus transient failure
- bad input should not disappear silently

### Event-Time Windows And Late Data

Choose this pattern when:

- arrival order differs from event order
- metrics must remain stable under correction
- lateness policy changes consumer expectations

### Savepoints, Checkpoints, And Progressive Promotion

Choose this pattern when:

- stateful processors evolve over time
- release and rollback must preserve recoverability
- checkpoint compatibility matters as much as code compatibility

## Step 3: Match The Platform

Use the matching preset and stack references:

- `presets/apache-kafka-streaming/PRESET.md`
- `presets/apache-flink-stream-processing/PRESET.md`
- `skills/debezium-and-kafka-connect-cdc/SKILL.md`
- `skills/data-contract-testing-with-schema-registry/SKILL.md`

Use cloud presets as needed when the broker, lakehouse, or serving layer is cloud-specific.

## Step 4: Design For Replay Before Production

Every streaming design should answer:

- what is the canonical event or source of truth?
- how does duplicate delivery get handled?
- how are late events treated?
- where does state live and how does it recover?
- what happens when downstream publish is blocked?

If replay safety is unclear, the streaming architecture is unfinished.

## Step 5: Pair The Pattern With Validation

Use:

- `skills/streaming-and-messaging-systems/SKILL.md`
- `skills/kafka-resilience-and-schema-evolution/SKILL.md`
- `skills/mcp-data-observability-integration/SKILL.md`
- `skills/data-observability-and-sla-management/SKILL.md`
- `skills/incident-triage-and-pipeline-recovery/SKILL.md`
- `references/kafka-production-guardrails.md`
- `references/data-resiliency-testing-patterns.md`

That combination keeps the design grounded in observability and recovery, not only throughput.

## Step 6: Review The Red Flags

Stop and rework the design if:

- derived streams are treated like the source of record
- no durable event identifier exists
- DLQ records are never reviewed or replayed
- event-time semantics are assumed instead of defined
- checkpoint, savepoint, or state evolution is left undocumented

## Recommended Reading

- `references/streaming-architecture-patterns.md`
- `references/data-resiliency-testing-patterns.md`
- `skills/streaming-and-messaging-systems/SKILL.md`
- `skills/debezium-and-kafka-connect-cdc/SKILL.md`
