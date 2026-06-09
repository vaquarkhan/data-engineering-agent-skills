---
name: spark-serverless-reliability-and-state-management
description: Enforces timeout-aware rollbacks, resumable checkpoints, and orphan cleanup for serverless Spark workloads on AWS Lambda, Glue, and similar runtimes. Use when writing or reviewing Spark jobs in serverless environments, S3 checkpoint patterns, partial-failure recovery, or IceGuard-style state management.
---

# Spark Serverless Reliability And State Management

## Overview

Serverless Spark hides cluster failures behind short-lived runtimes and opaque retries. Silent partial writes, orphaned checkpoints, and timeout-induced corruption are common when agents treat serverless Spark like a long-running cluster job. This skill forces explicit state boundaries, resumable progress, and cleanup before any publish path opens.

## When to Use

- implementing or reviewing Spark on `AWS Lambda`, `AWS Glue` serverless, or comparable short-lived runtimes
- designing S3-backed checkpoints, progress markers, or staged write paths
- recovering from timeout, OOM, or mid-batch partial failure without double-counting
- translating IceGuard-style checkpoint and rollback patterns into agent workflows
- hardening batch Spark that must survive cold starts, memory limits, and hard execution ceilings

Do not use this for always-on EMR or Databricks clusters unless the job also runs in a serverless path with hard time limits.

## Workflow

1. Classify execution risk before coding.
   Document:
   - maximum runtime and memory ceiling
   - input cardinality and partition fan-out
   - whether output is append, merge, or overwrite
   - downstream consumers that would see partial data
   - whether the job is restartable from a known offset or partition set

2. Design a resumable checkpoint contract.
   Require:
   - durable progress markers in object storage (for example `s3://.../checkpoints/{run_id}/`)
   - explicit run identifiers tied to orchestration metadata
   - idempotent write semantics at the target grain
   - a manifest or `_SUCCESS`-style gate before publish
   - separation between staging prefixes and publish prefixes

   Load `references/spark-serverless-reliability-patterns.md` for checkpoint layout and orphan-detection patterns.

3. Implement timeout-aware rollback.
   Before any publish:
   - detect incomplete partitions or missing manifest files
   - roll back staged outputs when the runtime approaches its ceiling
   - persist last-good checkpoint state for resume
   - block downstream publish when rollback is incomplete
   - emit structured failure context (run id, partition range, bytes written)

4. Plan orphan and zombie cleanup.
   Include:
   - TTL or lifecycle rules for abandoned staging prefixes
   - a reconciliation job or hook that lists orphaned checkpoints older than N hours
   - explicit ownership for cleanup automation
   - guardrails against deleting in-flight runs

5. Pair with observability before production.
   Load `mcp-data-observability-integration` when live execution plans, stage metrics, or cluster signals are needed to diagnose OOM or skew before rollout.

6. Prove recovery paths in a bounded slice.
   Validate:
   - forced timeout mid-batch resumes without duplicate publish
   - rerun from checkpoint produces identical contract-compliant output
   - orphan cleanup does not remove active runs

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Lambda will just retry the whole function." | Retries can duplicate writes, leave orphaned staging data, and publish partial partitions. |
| "We can write directly to the final table path." | Serverless timeouts make direct writes dangerous without staging and manifest gates. |
| "Checkpointing is only for streaming." | Any resumable batch with hard runtime limits needs durable progress markers. |
| "Glue handles cleanup automatically." | Managed runtimes do not guarantee orphan cleanup or rollback of partial lake writes. |

## Red Flags

- writes go directly to publish paths with no staging boundary
- no run id or checkpoint manifest exists
- timeout handling is undefined
- partial S3 prefixes have no orphan detection or TTL policy
- resume logic cannot distinguish completed versus in-flight partitions
- agents scale partitions without checking memory ceiling per task

## Verification

- [ ] Runtime limits, write mode, and idempotency grain are documented
- [ ] Checkpoint and staging layout support safe resume
- [ ] Timeout rollback and publish gating are explicit
- [ ] Orphan cleanup ownership and detection exist
- [ ] Recovery was proven on a bounded partition slice before full rollout
