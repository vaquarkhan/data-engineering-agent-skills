---
name: apache-kafka-streaming
description: Adapts the core skills for Apache Kafka-centered streaming systems. Use when Apache Kafka is the primary event backbone for topics, consumers, retention, replay, and downstream stream-processing architectures.
---

# Apache Kafka Streaming

## Overview

Use this preset when `Apache Kafka` is the central messaging backbone. It maps shared workflows to topic design, retention, consumer groups, replay behavior, schema evolution, and streaming interoperability.

## Use When

- designing or operating `Apache Kafka` topics
- building consumer and producer contracts
- managing replay, retention, and consumer lag
- supporting Flink, Spark, or other streaming consumers from Kafka

## Preferred Platform Services

- messaging backbone: `Apache Kafka`
- schema management: schema registry or equivalent contract tooling
- stream processing: `Apache Flink`, `Kafka Streams`, or other compatible engines
- monitoring: broker, topic, and consumer lag observability

## Design Rules

- Make event keys, retention, and replay policy explicit.
- Keep schema evolution controlled and visible.
- Treat lag, poison records, and dead-letter handling as operational concerns.
- Design topics for stable contracts, not only producer convenience.

## Companion Skills

- production guardrails: `kafka-resilience-and-schema-evolution`
- live lag and topic inspection: `mcp-data-observability-integration`
- replay-bound recovery: `safe-backfill-and-replay-orchestration`
- reference: `references/kafka-production-guardrails.md`

## Verification

- [ ] Topic contracts and key strategy are defined
- [ ] Retention and replay behavior are explicit
- [ ] Consumer lag and bad-record handling are observable
- [ ] Schema evolution expectations are documented
