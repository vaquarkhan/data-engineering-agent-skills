---
name: apache-iceberg-lakehouse
description: Adapts the core skills for Apache Iceberg-based lakehouse design. Use when Apache Iceberg is the primary table format for open lakehouse interoperability, schema evolution, partition evolution, and multi-engine analytics.
---

# Apache Iceberg Lakehouse

## Overview

Use this preset when `Apache Iceberg` is the core table format. It maps shared workflows to open lakehouse interoperability, snapshot-based reads, schema evolution, partition evolution, and maintenance-aware design.

## Use When

- building a lakehouse around `Apache Iceberg`
- supporting multi-engine reads and writes
- evolving schemas and partitions over time
- managing snapshots, compaction, and table lifecycle

## Preferred Platform Services

- table format: `Apache Iceberg`
- compute: `Apache Spark`, `Apache Flink`, or compatible engines
- storage: object storage or distributed filesystems
- catalog: metastore or catalog service compatible with Iceberg
- monitoring: table maintenance and query performance observability

## Design Rules

- Choose `Iceberg` for interoperability and lifecycle needs, not only trend value.
- Make snapshot retention, compaction, and partition evolution explicit.
- Validate engine compatibility for advanced writes and mutation patterns.
- Keep publish contracts separate from raw lake survival rules.

## Verification

- [ ] Iceberg is justified by interoperability or lifecycle requirements
- [ ] Snapshot, partition, and maintenance behavior are documented
- [ ] Engine compatibility assumptions are explicit
- [ ] Publish and governance expectations are clear
