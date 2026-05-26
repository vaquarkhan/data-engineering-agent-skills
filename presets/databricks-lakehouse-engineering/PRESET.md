---
name: databricks-lakehouse-engineering
description: Adapts the core skills for Databricks-centered data platforms. Use when the team standardizes on Delta Lake, Unity Catalog, Databricks Workflows, and lakehouse-native batch or streaming patterns.
---

# Databricks Lakehouse Engineering

## Overview

Use this preset when `Databricks` is the primary execution and governance surface, whether it runs on `AWS`, `Azure`, or `GCP`. It maps workflows to `Delta Lake`, `Unity Catalog`, `Databricks Workflows`, `Auto Loader`, `Delta Live Tables`, medallion-style layering, and Spark-native pipelines.

## Use When

- the platform standard is `Databricks`
- transformations and pipelines run primarily on Spark
- tables are managed in `Delta Lake`
- governance is anchored in `Unity Catalog`

## Preferred Platform Services

- table format: `Delta Lake`
- governance: `Unity Catalog`
- orchestration: `Databricks Workflows`
- ingestion: `Auto Loader`
- transformations: Spark jobs, SQL, notebooks, or package-based jobs
- declarative pipelines: `Delta Live Tables`
- monitoring: platform job monitoring plus cloud-native observability

## Common Architecture Patterns

- medallion lakehouse architecture with landing, bronze, silver, and gold boundaries
- unified batch and streaming platform with `Auto Loader`, streaming tables, and governed `Delta` outputs
- feature and analytics platform architecture where `Unity Catalog` governs shared tables, models, and consumers
- external-cloud landing plus `Databricks` transformation and serving when the object store is durable but execution is lakehouse-centric
- Load `references/cloud-data-engineering-architecture-patterns.md` when deciding whether `Databricks` should be the primary architecture boundary or part of a larger hybrid platform

## Orchestration Patterns

- Prefer `Databricks Workflows` when jobs, notebooks, SQL tasks, and validations mostly stay inside `Databricks`.
- Prefer `Delta Live Tables` when the workflow is fundamentally a managed table pipeline with expectations and refresh semantics owned by the platform.
- Use an external orchestrator when dependencies span systems outside `Databricks`, such as upstream files, external APIs, enterprise approvals, or non-Databricks publish steps.
- Keep orchestration decisions explicit so `Databricks` jobs do not hide recovery, replay, or cross-platform handoff behavior.
- Load `references/pipeline-orchestration-patterns.md` when deciding whether orchestration should stay inside `Databricks` or be coordinated externally.

## Design Rules

- Keep notebook convenience separate from production packaging and deployment discipline.
- Treat `Unity Catalog` permissions, lineage, and data sharing as part of the implementation.
- Use medallion layers only when each layer has a real quality and ownership boundary.
- Design incremental patterns around `Delta Lake` semantics, checkpoints, and merge behavior.
- Be explicit about cluster policy, job compute, and cost controls.
- Use `Delta Live Tables` only when the operational model matches the team needs.

## Verification

- [ ] Delta table strategy and mutation semantics are clear
- [ ] Medallion layering responsibilities are documented where used
- [ ] Governance and access are mapped through `Unity Catalog`
- [ ] Job packaging, orchestration, and compute strategy are documented
- [ ] Streaming or incremental designs account for checkpoints and replay behavior
