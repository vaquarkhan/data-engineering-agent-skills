---
name: bigquery-and-dataform-platform-engineering
description: Guides agents through BigQuery- and Dataform-centered data engineering workflows. Use when designing BigQuery physical models, ingestion boundaries, Dataform transformation workflows, slot or cost controls, and platform decisions across BigQuery, Dataflow, Dataproc, and GCP orchestration services.
---

# BigQuery And Dataform Platform Engineering

## Overview

Use this skill when `BigQuery` is the center of gravity for analytics engineering and data delivery on `GCP`. It helps agents decide what should run in `BigQuery`, what belongs in `Dataform`, and when the workflow should move to `Dataflow`, `Dataproc`, or external orchestration.

## When to Use

- designing or reviewing `BigQuery` physical models
- deciding between `Dataform`, `dbt`, `Dataflow`, or `Dataproc` responsibilities
- tuning partitioning, clustering, slots, and cost behavior
- defining ingestion and transformation boundaries on `GCP`
- building platform-native analytics workflows around `BigQuery`

Do not treat `BigQuery` as a universal default for every preprocessing and orchestration need.

## Workflow

1. Define the workload boundary.
   Clarify:
   - landing pattern
   - transformation complexity
   - latency requirements
   - governance and regional constraints
   - cost sensitivity

2. Design `BigQuery` physical layout intentionally.
   Cover:
   - partitioning
   - clustering
   - dataset boundaries
   - publish layers
   - data retention and serving expectations

3. Choose the transformation surface.
   Consider:
   - `Dataform` for warehouse-native SQL transformation workflows
   - `dbt` when the team already standardizes there
   - `Dataflow` or `Dataproc` when preprocessing or runtime requirements exceed warehouse-native fit

4. Define orchestration and operations.
   Include:
   - where orchestration runs
   - slot and concurrency behavior
   - failure and rerun expectations
   - validation gates before publish

5. Validate cost and governance behavior.
   Require:
   - slot or query cost awareness
   - service-account and secret controls
   - policy tags or governance metadata where needed
   - publish-readiness evidence

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Everything on GCP should run in BigQuery." | Some preprocessing, streaming, or protocol-heavy work belongs in `Dataflow`, `Dataproc`, or upstream services. |
| "Dataform is just a SQL wrapper." | It changes how transformation workflows, dependencies, testing, and deployment are managed. |
| "Partitioning and clustering can be tuned later." | Poor physical design often becomes a long-term cost and performance tax. |

## Red Flags

- BigQuery physical design is implicit or copied from defaults
- transformation boundaries between `Dataform`, `Dataflow`, and `Dataproc` are unclear
- cost or slot behavior is not considered during model design
- publish and validation behavior is undefined for warehouse-native pipelines
- governance metadata and access are treated as separate cleanup work

## Verification

- [ ] BigQuery physical design choices are explicit and workload-aware
- [ ] Dataform, BigQuery, and other GCP services have clear boundaries
- [ ] Cost, slots, and concurrency implications are documented
- [ ] Governance and access controls are accounted for
- [ ] Publish and validation behavior are explicit before release
