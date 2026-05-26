---
name: etl-elt-and-modernization-strategy
description: Guides agents through ETL, ELT, and transformation-modernization decisions. Use when choosing execution boundaries, redesigning transformation layers, or moving from legacy ETL estates to warehouse- or lakehouse-centered ELT patterns.
---

# ETL ELT And Modernization Strategy

## Overview

Use this skill when the hard part is not a single job, but deciding where transformations should run and how a data estate should modernize over time. It helps agents reason about `ETL` versus `ELT`, pushdown versus external compute, orchestration boundaries, migration sequencing, and proof of parity during modernization.

## When to Use

- choosing between `ETL`, `ELT`, or hybrid transformation patterns
- moving from legacy ETL tools into warehouse, dbt, Spark, or lakehouse execution
- redesigning ingestion and transformation boundaries across raw, curated, and publish layers
- reducing operational sprawl caused by duplicate transformation logic
- modernizing batch-first estates without breaking existing delivery expectations

Do not assume `ELT` is always better just because the warehouse is powerful.

## Workflow

1. Define the transformation problem clearly.
   Clarify:
   - source latency and volume
   - data quality expectations
   - transformation complexity
   - cost sensitivity
   - publish or consumption latency

2. Map the current execution estate.
   Include:
   - where extraction happens
   - where transformations happen today
   - what logic is duplicated across tools
   - where lineage or observability breaks
   - what jobs are hardest to change safely

3. Choose the right execution boundary.
   Consider:
   - `ETL` when data must be reshaped or protected before landing
   - `ELT` when warehouse or lakehouse pushdown improves maintainability and scaling
   - hybrid patterns when extraction, privacy controls, or heavy preprocessing must happen before durable load

4. Plan the modernization path.
   Decide:
   - what stays temporarily on the old path
   - what moves first
   - how parity will be measured
   - how cutover and rollback will work

5. Prove the new shape operationally.
   Require:
   - reconciliation evidence
   - cost and performance review
   - lineage continuity
   - ownership and support readiness

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Everything should become ELT." | Some workloads still need pre-load shaping, masking, or protocol-specific extraction controls. |
| "The ETL tool is the problem." | The real issue may be unclear ownership, poor contracts, or duplicated logic across layers. |
| "We can rewrite all transformations at once." | Big-bang modernization usually breaks parity, runbooks, and downstream trust. |

## Red Flags

- the same business logic exists in extraction jobs, Spark, and warehouse SQL
- ETL versus ELT is chosen by tool preference instead of workload needs
- modernization plans skip parity, cutover, or rollback
- sensitive fields are moved into ELT layers without revisiting controls

## Verification

- [ ] The transformation boundary matches the real workload constraints
- [ ] ETL, ELT, and hybrid choices are explicit rather than assumed
- [ ] Modernization sequencing, parity proof, and rollback are defined
- [ ] Cost, lineage, controls, and support ownership were considered together
