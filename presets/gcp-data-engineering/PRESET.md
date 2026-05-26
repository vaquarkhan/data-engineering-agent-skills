---
name: gcp-data-engineering
description: Adapts the core skills for Google Cloud data engineering teams. Use when the platform is primarily built on GCP services for storage, pipelines, analytics, streaming, and governance.
---

# GCP Data Engineering

## Overview

Use this preset when the data platform is centered on Google Cloud. It maps shared workflows to `Cloud Storage`, `BigQuery`, `Dataflow`, `Dataproc`, `Composer`, `Pub/Sub`, `Dataplex`, and Google Cloud observability services.

Pair this preset with `skills/bigquery-and-dataform-platform-engineering/SKILL.md` when `BigQuery` physical design, `Dataform`, and warehouse-native delivery are the main execution boundary.

Pair this preset with `skills/dataplex-and-bigquery-governance/SKILL.md` when `Dataplex`, policy tags, and GCP-native governed publishing are the main concern.

## Use When

- using `BigQuery` as the core analytics engine
- landing raw or staged data in `Cloud Storage`
- processing with `Dataflow`, `Dataproc`, or `BigQuery`
- orchestrating with `Composer` or event-driven cloud services

## Preferred Platform Services

- storage: `Cloud Storage`
- warehouse and serving: `BigQuery`
- orchestration: `Cloud Composer`, `Workflows`
- batch and stream processing: `Dataflow`, `Dataproc`
- messaging: `Pub/Sub`
- governance: `Dataplex`, `Data Catalog` where still in use
- secrets and security: `IAM`, `Secret Manager`, `Cloud KMS`
- monitoring: `Cloud Logging`, `Cloud Monitoring`

## Common Architecture Patterns

- `Cloud Storage` plus `BigQuery` for a warehouse-centric analytics platform with external landing
- `Pub/Sub` + `Dataflow` + `BigQuery` for streaming and analytical architecture with managed services
- `Cloud Storage` plus `Dataproc` or `Dataflow` feeding `BigQuery` when compute specialization is required
- `BigQuery`-first architecture when the warehouse is the main compute and serving boundary
- Load `references/cloud-data-engineering-architecture-patterns.md` when choosing between lake, warehouse, and stream-first patterns on `GCP`

## Orchestration Patterns

- Prefer `Cloud Composer` when the team needs `Airflow`-style DAGs, schedule windows, and backfill-aware dependencies.
- Prefer `Google Cloud Workflows` when the control plane mainly coordinates APIs, services, and branching logic.
- Use `Cloud Scheduler` plus `Pub/Sub` for lightweight trigger paths instead of deploying a large scheduler for simple starts.
- Keep `Composer` responsible for orchestration while heavy compute stays in `Dataflow`, `Dataproc`, `BigQuery`, or packaged jobs.
- Load `references/pipeline-orchestration-patterns.md` when choosing among `Composer`, `Workflows`, and event-triggered GCP patterns.

## Design Rules

- Treat `BigQuery` table design, partitioning, and clustering as core architecture decisions.
- Keep ingestion and transformation choices aligned with data volume and latency requirements.
- Use service accounts and platform-native secret management for pipeline identities.
- Watch query cost, storage lifecycle, and cross-region design carefully.
- Use governance metadata and policy tags where sensitive data is published.

## Verification

- [ ] `BigQuery` physical design choices are explicit
- [ ] Processing engine selection matches latency and scale requirements
- [ ] Access, secret handling, and encryption map to GCP-native controls
- [ ] Cost and region decisions are documented for compute and storage
