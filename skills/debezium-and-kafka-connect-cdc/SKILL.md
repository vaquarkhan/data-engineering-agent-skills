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

## Verification

- [ ] Connector snapshot and offset behavior are explicit
- [ ] Topic contracts and downstream CDC expectations are documented
- [ ] Recovery and schema evolution paths are defined
