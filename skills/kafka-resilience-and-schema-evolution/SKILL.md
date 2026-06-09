---
name: kafka-resilience-and-schema-evolution
description: Enforces production Kafka guardrails including non-breaking schema evolution, dead-letter queues for poison messages, and acks=all producer durability. Use when designing or changing Kafka topics, producers, consumers, schema registry policies, or streaming recovery paths.
---

# Kafka Resilience And Schema Evolution

## Overview

Generic streaming guidance is not enough for production Kafka. Agents routinely introduce breaking schema changes, under-provisioned durability settings, and missing poison-message isolation. This skill mandates enforceable broker, producer, consumer, and registry guardrails before any production change ships.

## When to Use

- creating or modifying `Kafka` topics, producers, or consumers
- setting or changing schema registry compatibility policies
- designing dead-letter queue (DLQ) routing for poison pill messages
- hardening producer durability (`acks`, retries, idempotence)
- reviewing consumer lag, replay, or failover behavior on Kafka-backed pipelines

Pair with `streaming-and-messaging-systems` for broader event design. Pair with `avro-protobuf-json-schema-registry` when registry subjects and compatibility CI are in scope.

## Workflow

1. Define the production contract before broker changes.
   Document:
   - topic key strategy and partition count rationale
   - retention, compaction, and replay policy
   - schema format and registry subject naming
   - consumer groups and downstream sinks
   - delivery semantics target (at-least-once with idempotent sinks, or stricter)

2. Enforce producer durability defaults.
   Require unless explicitly waived with owner approval:
   - `acks=all` (or `acks=-1`)
   - `enable.idempotence=true` when ordering and deduplication matter
   - bounded `retries` with `delivery.timeout.ms` aligned to SLA
   - `max.in.flight.requests.per.connection=1` when strict ordering is required
   - TLS/SASL configuration documented for non-development clusters

3. Block breaking schema evolution.
   Before any schema change:
   - set compatibility policy per subject (`BACKWARD`, `FORWARD`, or `FULL` — not `NONE` in production)
   - run compatibility checks in CI against registered schemas
   - document producer-then-consumer or consumer-then-producer rollout order
   - reject field removals, renames, or type changes without migration plan
   - load `references/kafka-production-guardrails.md` for DLQ and evolution patterns

4. Mandate dead-letter and poison pill isolation.
   Every production consumer that parses external payloads must define:
   - DLQ topic or sink with retention and access controls
   - classification rules (deserialization failure, schema mismatch, business rule violation)
   - alert routing when DLQ rate exceeds threshold
   - replay procedure with deduplication keys
   - no silent drop of unparseable records

5. Make lag and recovery observable.
   Plan for:
   - consumer group lag alerts with owner routing
   - offset reset policy documented and restricted
   - replay runbook that does not bypass DLQ classification
   - broker disk and retention monitoring for high-throughput topics

6. Load MCP observability when diagnosing live lag.
   Use `mcp-data-observability-integration` with `mcp/kafka.mcp.json` to inspect consumer group lag and topic metadata before changing consumer code or partition counts.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "acks=1 is fine because Kafka is durable." | Leader acknowledgment without full ISR acknowledgment loses events under failure scenarios. |
| "We can fix schema breaks by redeploying consumers quickly." | Breaking changes propagate to many consumers and batch sinks before redeploy completes. |
| "DLQs add too much operational overhead." | Poison pills without DLQs stall partitions, inflate lag, and hide data loss as consumer retries. |
| "Schema compatibility NONE is okay for internal topics." | Internal topics still feed warehouses, stream processors, and audit systems. |

## Red Flags

- production subjects use `NONE` compatibility
- producers use `acks=0` or `acks=1` without documented waiver
- consumers have no DLQ path for deserialization failures
- schema changes ship without CI compatibility validation
- consumer group lag has no alert owner
- replay procedures reset offsets without reconciliation or publish pause

## Verification

- [ ] Producer durability settings meet `acks=all` and idempotence requirements
- [ ] Schema compatibility policy is set and CI-validated for production subjects
- [ ] DLQ routing, alerts, and replay procedure are documented
- [ ] Consumer lag and retention monitoring exist with named owners
- [ ] Rollout order for schema changes is explicit and tested in non-production
