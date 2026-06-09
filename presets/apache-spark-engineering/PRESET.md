---
name: apache-spark-engineering
description: Adapts the core skills for Apache Spark-centered data engineering. Use when the primary execution engine is Apache Spark for large-scale batch transformations, SQL processing, or lakehouse integration.
---

# Apache Spark Engineering

## Overview

Use this preset when `Apache Spark` is the main compute engine. It maps shared workflows to Spark jobs, Spark SQL, partition-aware storage design, and batch or micro-batch processing patterns.

## Use When

- building large-scale batch pipelines with `Apache Spark`
- running Spark SQL transformations over lake or warehouse-adjacent storage
- managing joins, shuffles, partitioning, and distributed writes
- using Spark with `Iceberg`, `Delta`, or `Hudi`

## Preferred Platform Services

- execution: `Apache Spark`
- scheduling: external orchestrator such as `Apache Airflow`
- storage: object storage or distributed filesystems
- table formats: `Apache Iceberg`, `Delta Lake`, or `Apache Hudi`
- monitoring: Spark history server and platform-native observability

## Design Rules

- Choose `Spark` because the workload needs distributed compute, not by habit.
- Design partitioning, joins, and write modes explicitly.
- Keep job logic separate from orchestration and notebook convenience.
- Make backfills, retries, and small-file behavior operationally safe.

## Companion Skills

- serverless or timeout-bound Spark: `spark-serverless-reliability-and-state-management`
- execution plan and OOM diagnosis: `mcp-data-observability-integration`
- historical recomputation: `safe-backfill-and-replay-orchestration`
- reference: `references/spark-serverless-reliability-patterns.md`

## Verification

- [ ] The workload justifies `Apache Spark`
- [ ] Partitioning, join strategy, and write semantics are explicit
- [ ] Table format and storage assumptions are documented
- [ ] Monitoring and retry behavior are defined
