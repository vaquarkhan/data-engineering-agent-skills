---
name: enterprise-etl-and-data-integration-modernization
description: Guides agents through operating, hardening, and modernizing enterprise ETL and integration stacks such as Informatica, Talend, DataStage, SSIS, and Matillion. Use when legacy mappings, job orchestration, migration, or coexistence with modern lakehouse patterns must be handled safely.
---

# Enterprise ETL And Data Integration Modernization

## Overview

Use this skill when delivery depends on classic enterprise ETL tooling, not only modern code-first platforms. It helps agents reason about mapping logic, scheduler dependencies, restart behavior, metadata export, migration sequencing, and coexistence between legacy ETL platforms and newer Spark, dbt, Airflow, or lakehouse stacks.

## When to Use

- working with `Informatica`, `Talend`, `DataStage`, `SSIS`, or `Matillion`
- reverse-engineering existing ETL mappings and workflows
- modernizing or migrating legacy ETL jobs
- adding quality, lineage, and operational controls to GUI-driven pipelines
- running hybrid estates where old and new tooling must coexist

Do not assume enterprise ETL logic is simple just because much of it is configured through a UI.

## Workflow

1. Inventory the actual delivery surface.
   Capture:
   - mappings and transformations
   - parameter files and environment variables
   - scheduler dependencies
   - restart and checkpoint behavior
   - external scripts and post-load actions

2. Recover business logic from the platform implementation.
   Identify:
   - joins and filters
   - surrogate-key logic
   - SCD behavior
   - reject handling
   - data-quality rules embedded in mappings

3. Make environment and deployment assumptions explicit.
   Document:
   - connection differences by environment
   - credential handling
   - promotion rules
   - metadata dependencies
   - non-obvious manual runbooks

4. Plan coexistence or migration safely.
   Decide:
   - what remains on the legacy platform
   - what moves to code-first pipelines
   - how parity will be validated
   - how cutover and rollback will work

5. Add observability and control points around the jobs.
   Include:
   - run metadata
   - reconciliation checks
   - lineage capture
   - failure classification
   - repeatable deployment evidence

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The ETL tool already handles everything." | GUI tooling still hides logic, dependencies, and failure modes that must be made explicit. |
| "We can just rewrite it later." | Legacy ETL estates become harder to migrate the longer the hidden assumptions remain undocumented. |
| "The mapping is self-explanatory." | Parameter files, scheduler behavior, and reject handling often carry critical business logic. |

## Red Flags

- mapping logic depends on undocumented manual steps
- environment promotion is done by hand with no parity validation
- restart or reject behavior is unknown
- migration plans ignore reconciliation and rollback

## Verification

- [ ] Mapping logic, dependencies, and restart behavior are inventoried
- [ ] Hidden environment and scheduler assumptions are documented
- [ ] Coexistence or migration boundaries are explicit
- [ ] Reconciliation, lineage, and operational controls exist around delivery
- [ ] Cutover and rollback plans are defined for migrations
