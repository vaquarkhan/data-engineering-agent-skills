---
name: aws-data-engineering
description: Adapts the core skills for AWS-native data engineering teams. Use when the platform is primarily built on AWS services for storage, processing, orchestration, governance, and analytics.
---

# AWS Data Engineering

## Overview

Use this preset when the data platform is primarily AWS-native. It maps common data engineering concerns to services such as `S3`, `Glue`, `Athena`, `Redshift`, `EMR`, `Kinesis`, `Lake Formation`, `MWAA`, and `CloudWatch`.

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

## Design Rules

- Prefer durable raw-zone storage in `S3` with clear partitioning and ownership.
- Treat `Lake Formation` and `IAM` policies as part of implementation, not documentation.
- Separate ad hoc query patterns from production-grade publish layers.
- Choose intentionally between warehouse-native serving and lakehouse tables such as `Iceberg`.
- Design backfills to avoid runaway scan cost in `S3`, `Athena`, and `Redshift`.
- Use platform-native monitoring and tagging so cost and ownership stay visible.

## Verification

- [ ] Storage layout, partitioning, and retention are defined
- [ ] Access and encryption controls are mapped to `IAM`, `Lake Formation`, or `KMS`
- [ ] Orchestration, replay, and failure handling fit the selected AWS service
- [ ] Table format choices such as `Iceberg` are intentional and operationally supported
- [ ] Cost-sensitive scans and backfills have explicit limits or guardrails
