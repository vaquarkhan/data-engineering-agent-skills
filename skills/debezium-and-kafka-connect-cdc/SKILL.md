---
name: debezium-and-kafka-connect-cdc
description: Guides agents through Debezium and Kafka Connect CDC workflows. Use when streaming database changes into Kafka topics, managing connectors, snapshots, schema evolution, or downstream CDC consumers.
---

# Debezium And Kafka Connect CDC

## Overview

Use this skill when database changes must be captured and delivered through `Debezium` and `Kafka Connect`. It helps agents define connector safety, snapshot behavior, schema handling, and downstream CDC contracts.

## When to Use

- setting up `Debezium` connectors
- designing Kafka-based CDC from transactional databases
- handling snapshots, schema changes, and connector recovery
- feeding downstream stream processors or lakehouse sinks

## Workflow

1. Define source tables, keys, and change semantics.
2. Make connector snapshot and offset behavior explicit.
3. Define topic contracts, retention, and downstream consumers.
4. Plan for schema evolution and connector recovery.
5. Validate replay and bootstrap behavior before publish.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The platform-specific feature is the whole design." | Platform features do not replace contract, compatibility, and operational planning. |
| "We can validate this after publish." | Late validation is expensive when downstream consumers already depend on the asset. |
| "Operations can figure out the edge cases later." | Replay, maintenance, and publish safety need to be explicit before adoption. |

## Red Flags

- downstream compatibility is assumed instead of documented
- publish or replay behavior is not explicit
- maintenance, rollback, or observability expectations are missing
## Verification

- [ ] Connector snapshot and offset behavior are explicit
- [ ] Topic contracts and downstream CDC expectations are documented
- [ ] Recovery and schema evolution paths are defined
