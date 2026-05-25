---
name: spark-and-distributed-processing
description: Guides agents through batch and distributed data processing design. Use when implementing or reviewing Spark-based pipelines, or managed distributed runtimes such as Glue and EMR.
---

# Spark And Distributed Processing

## Overview

Use this skill for batch workloads that exceed single-node processing and need distributed execution discipline. It helps agents reason about `Spark`, managed Spark services such as `Glue` and `EMR`, partitioning, joins, storage layout, and failure-safe processing.

## When to Use

- building or changing `Spark` jobs
- choosing between `Spark`, `Glue`, `EMR`, or smaller engines
- debugging expensive joins, skew, shuffle, or memory issues
- designing batch pipelines over large files or partitioned tables
- implementing transformations against lakehouse tables such as `Iceberg`, `Delta`, or `Hudi`

Do not use this for lightweight local transforms that fit comfortably in a single process.

## Workflow

1. Confirm distributed execution is actually required.
   Check:
   - input volume
   - latency expectations
   - transformation complexity
   - file sizes and partition counts
   - cost compared with simpler engines

2. Choose the runtime intentionally.
   - `Spark`: direct control and broad ecosystem support
   - `Glue`: managed AWS-native Spark execution
   - `EMR`: broader cluster control for Spark and related engines

3. Design the physical plan, not just the logical one.
   Account for:
   - partitioning and file layout
   - shuffle-heavy joins
   - skewed keys
   - checkpoint or intermediate persistence
   - write mode and idempotency behavior

4. Keep data contracts visible at the edges.
   Validate input assumptions before expensive execution and verify output contracts before publish.

5. Make backfills and reruns safe.
   Historical batch recomputation should define overwrite, merge, or append semantics explicitly.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Spark will handle optimization for us." | Engine optimizations help, but poor partitioning, skew, and write strategy still create failures or huge cost. |
| "We can just scale the cluster." | Scaling often masks bad physical design and can still fail on skew or bad shuffles. |
| "Managed Spark means we do not need runtime design." | `Glue` and `EMR` still require deliberate partitioning, retries, and storage strategy. |

## Red Flags

- `Spark` is chosen without a scale or latency reason
- partitioning and write strategy are undefined
- joins ignore skewed business keys
- rerun behavior for historical loads is unclear
- distributed compute is used where a smaller engine would be simpler and cheaper

## Verification

- [ ] The runtime choice is justified against workload needs
- [ ] Partitioning, join strategy, and write semantics are explicit
- [ ] Contracts and quality checks exist at input and output boundaries
- [ ] Backfill and retry behavior are documented for the distributed job
