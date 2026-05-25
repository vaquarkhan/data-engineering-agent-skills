---
name: gcp-data-engineering
description: Adapts the core skills for Google Cloud data engineering teams. Use when the platform is primarily built on GCP services for storage, pipelines, analytics, streaming, and governance.
---

# GCP Data Engineering

## Overview

Use this preset when the data platform is centered on Google Cloud. It maps shared workflows to `Cloud Storage`, `BigQuery`, `Dataflow`, `Dataproc`, `Composer`, `Pub/Sub`, `Dataplex`, and Google Cloud observability services.

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
