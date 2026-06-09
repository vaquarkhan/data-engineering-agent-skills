---
name: aws-data-engineering
description: Adapts the core skills for AWS-native data engineering teams. Use when the platform is primarily built on AWS services for storage, processing, orchestration, governance, and analytics.
---

# AWS Data Engineering

## Overview

Use this preset when the data platform is primarily AWS-native. It maps common data engineering concerns to services such as `S3`, `Glue`, `Athena`, `Redshift`, `EMR`, `Kinesis`, `Lake Formation`, `MWAA`, and `CloudWatch`.

Pair this preset with `skills/glue-data-catalog-and-lake-formation-governance/SKILL.md` when `Glue Data Catalog`, `Lake Formation`, governed sharing, and AWS-native metadata boundaries are the main concern.

## Use When

- landing and serving data on `AWS`
- using `S3` as the system of record for data lake storage
- orchestrating with `MWAA`, `Step Functions`, or event-driven workflows
- using `Glue`, `EMR`, `Athena`, or `Redshift` as core processing layers

## Preferred Platform Services

- storage: `S3`
- catalog and governance: `Glue Data Catalog`, `Lake Formation`
- orchestration: `MWAA`, `Step Functions`
- batch compute: `Glue`, `EMR`
- streaming: `Kinesis`, `MSK`
- warehouse and serving: `Redshift`, `Athena`
- table formats: `Apache Iceberg` where open lakehouse interoperability is required
- secrets and security: `IAM`, `Secrets Manager`, `KMS`
- monitoring: `CloudWatch`, `CloudTrail`

## Common Architecture Patterns

- `S3` landing zone plus `Glue` or `EMR` batch transforms, with `Athena` or `Redshift` serving for a lake-centric architecture
- `S3` plus `Iceberg` for lakehouse-style table management when open format interoperability matters
- `Redshift`-centric warehouse architecture when structured analytics and SQL-serving dominate
- `Kinesis` or `MSK` streaming pipelines feeding warehouse, lakehouse, or operational outputs
- Load `references/cloud-data-engineering-architecture-patterns.md` when choosing the overall AWS platform shape, not just service preferences

## Orchestration Patterns

- Prefer `MWAA` when the workflow is DAG-shaped, dependency-rich, and backfill-aware across `Glue`, `EMR`, `Athena`, or `Redshift`.
- Prefer `Step Functions` when the workflow is event-driven, branch-heavy, approval-oriented, or mainly coordinating AWS services.
- Use `EventBridge` plus queues or lightweight compute for arrival-triggered flows instead of building polling-heavy schedulers.
- Keep `Glue Workflows` for narrower `Glue`-centric chains rather than the default orchestrator for the whole platform.
- Load `references/pipeline-orchestration-patterns.md` when choosing among `MWAA`, `Step Functions`, and event-triggered patterns.

## Design Rules

- Prefer durable raw-zone storage in `S3` with clear partitioning and ownership.
- Treat `Lake Formation` and `IAM` policies as part of implementation, not documentation.
- Separate ad hoc query patterns from production-grade publish layers.
- Choose intentionally between warehouse-native serving and lakehouse tables such as `Iceberg`.
- Design backfills to avoid runaway scan cost in `S3`, `Athena`, and `Redshift`.
- Use platform-native monitoring and tagging so cost and ownership stay visible.

## Companion Skills

- `MSK` or `Kinesis` production hardening: `kafka-resilience-and-schema-evolution`
- serverless or timeout-bound `Glue` / `Lambda` Spark: `spark-serverless-reliability-and-state-management`
- replay or bounded backfill on AWS pipelines: `safe-backfill-and-replay-orchestration`
- live lag, DAG, or Spark plan diagnosis: `mcp-data-observability-integration`

## Verification

- [ ] Storage layout, partitioning, and retention are defined
- [ ] Access and encryption controls are mapped to `IAM`, `Lake Formation`, or `KMS`
- [ ] Orchestration, replay, and failure handling fit the selected AWS service
- [ ] Table format choices such as `Iceberg` are intentional and operationally supported
- [ ] Cost-sensitive scans and backfills have explicit limits or guardrails
