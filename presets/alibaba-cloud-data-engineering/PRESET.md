---
name: alibaba-cloud-data-engineering
description: Adapts the core skills for Alibaba Cloud data engineering teams. Use when the platform is primarily built on Alibaba Cloud services for storage, batch, streaming, analytics, and governance.
---

# Alibaba Cloud Data Engineering

## Overview

Use this preset when the data platform is based on Alibaba Cloud. It maps core workflows to `OSS`, `MaxCompute`, `DataWorks`, `EMR`, `Realtime Compute for Apache Flink`, `AnalyticDB`, and Alibaba Cloud security and monitoring services.

## Use When

- using `Alibaba Cloud` as the primary deployment target
- storing lake data in `OSS`
- orchestrating pipelines with `DataWorks`
- processing with `MaxCompute`, `EMR`, or `Flink`

## Preferred Platform Services

- storage: `OSS`
- orchestration: `DataWorks`
- batch processing: `MaxCompute`, `EMR`
- streaming: `Realtime Compute for Apache Flink`
- warehouse and serving: `AnalyticDB`
- secrets and security: `RAM`, `KMS`
- monitoring: `CloudMonitor`, platform audit services

## Common Architecture Patterns

- `OSS` landing plus `MaxCompute` or `EMR` batch processing for lake-centric architecture
- `Realtime Compute for Apache Flink` plus `AnalyticDB` for streaming and analytical serving architecture
- `DataWorks`-centric orchestration and governance pattern for enterprise scheduling and lineage visibility
- mixed `EMR` and `MaxCompute` architecture where workloads differ by scale, engine requirements, or operational constraints
- Load `references/cloud-data-engineering-architecture-patterns.md` when choosing the overall Alibaba Cloud platform shape

## Design Rules

- Keep platform-native scheduling, lineage, and governance visible through `DataWorks` where possible.
- Distinguish clearly between lake storage in `OSS` and analytic serving layers such as `AnalyticDB`.
- Treat identity, regional deployment, and network boundaries as first-order architecture inputs.
- Plan backfills and heavy batch workloads around platform quotas and cost controls.

## Verification

- [ ] Storage, compute, and publish layers are clearly separated
- [ ] Scheduling and governance responsibilities are explicit
- [ ] Security and secret handling map to Alibaba Cloud-native controls
- [ ] Region, quota, and cost constraints have been considered
