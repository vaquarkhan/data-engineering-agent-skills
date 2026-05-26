# Streaming Architecture Patterns

Use this reference when a streaming system needs more than generic broker and consumer guidance. It covers the recurring architecture choices that determine whether a real-time platform stays reliable under replay, scale, and schema change.

## Event Backbone Versus Derived Streams

Separate durable source-of-truth topics from derived or enriched streams.

Use this pattern when:

- multiple downstream consumers depend on the same canonical event feed
- enrichment or denormalization should not rewrite the original business event
- replay needs a stable input stream

Watch for:

- derived topics being treated like the original source of record
- backfills writing directly into publish topics without lineage or replay notes

## CDC Or Outbox To Streaming

Prefer explicit `CDC` or outbox patterns when operational databases feed a stream.

Use this pattern when:

- database changes must become events
- ordering and transaction boundaries matter
- services should not publish business events directly from request handlers

Watch for:

- dual writes to database and broker with no consistency model
- update/delete semantics being lost during capture
- event contracts mirroring raw table shapes without business meaning

## Idempotent Consumer And Replay-Safe Sink

Assume retries and reprocessing will happen.

Use this pattern when:

- consumers write to warehouses, search indexes, or serving tables
- sink writes can be repeated during replay or failover
- exactly-once guarantees are claimed

Watch for:

- replay causing duplicate publish rows
- sink deduplication relying only on arrival time
- no durable event identifier or merge key

## Dead-Letter And Poison Message Isolation

Bad records should be isolated without silently disappearing.

Use this pattern when:

- consumers parse external events
- schema drift or corrupt payloads can occur
- operations teams need a clear recovery path

Watch for:

- failed records being dropped with only log output
- `DLQ` topics that are never reviewed or replayed
- no distinction between transient failure and permanently bad payloads

## Event-Time Windows And Late Data

Define time semantics explicitly instead of assuming processing time is good enough.

Use this pattern when:

- aggregations depend on event occurrence time
- out-of-order records arrive regularly
- financial or operational metrics must remain stable after correction

Watch for:

- watermark settings copied from examples without business fit
- late-arriving corrections mutating published outputs unpredictably
- no policy for window closure, grace period, or correction handling

## Stream-Table And Table-Table Joins

Joins in streaming systems need freshness and state boundaries, not only SQL syntax.

Use this pattern when:

- streams enrich against dimension tables
- multiple continuous inputs are joined
- state size and key skew matter operationally

Watch for:

- dimension freshness assumptions that are never validated
- unbounded state due to missing TTL or window boundaries
- hot keys causing uneven partition load

## Savepoints, Checkpoints, And Progressive Promotion

Promote stateful jobs like data systems, not only code artifacts.

Use this pattern when:

- `Flink` or other stateful processors move across environments
- code changes interact with existing operator state
- rollback must preserve recoverability

Watch for:

- releases with no checkpoint or savepoint compatibility plan
- schema or operator changes that strand state
- rollback plans that only mention Git revert

## Partitioning And Hot-Key Containment

Partitioning is an architecture decision, not a runtime detail.

Use this pattern when:

- throughput is uneven across keys
- ordering is required within a key
- consumer groups scale horizontally

Watch for:

- one tenant, device, or entity dominating a partition
- partition count changes with no rebalance impact review
- ordering requirements that conflict with key design

## Recommended Pairings In This Repo

- source capture and replay: `cdc-and-incremental-loading`, `debezium-and-kafka-connect-cdc`
- event contracts: `avro-protobuf-json-schema-registry`, `data-contract-testing-with-schema-registry`
- operations and recovery: `data-observability-and-sla-management`, `incident-triage-and-pipeline-recovery`
- platform presets: `apache-kafka-streaming`, `apache-flink-stream-processing`
- reference checks: `references/streaming-checklist.md`
