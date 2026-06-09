---
name: safe-backfill-and-replay-orchestration
description: Forces replay-safe rollout plans, reconciliation gates, and rollback paths before executing any data backfill or historical reprocessing. Use when running /backfill, rerunning pipelines, repairing publish windows, or any work that risks double-counting or downstream corruption.
---

# Safe Backfill And Replay Orchestration

## Overview

Backfills are among the highest-risk data engineering operations. Agents that rerun jobs without bounded windows, publish gates, or reconciliation checks routinely cause double-counting, corrupted metrics, and downstream trust loss. This skill blocks execution until a written replay plan, rollback path, and validation gates exist.

## When to Use

- running `/backfill` or any historical reprocessing request
- repairing a failed or partial publish window
- replaying events or partitions after an incident
- changing transformation logic that requires recomputation
- cutting over to new pipeline behavior with overlapping data windows

Always load this skill before `orchestration-and-backfills` execution steps. Treat plan approval as a hard gate, not a suggestion.

## Workflow

1. Stop before execution.
   Do not trigger reruns, delete partitions, or open publish paths until the replay plan is drafted and reviewed.

2. Run the backfill guard hook when available.
   Execute `hooks/backfill-guard.sh` or `hooks/backfill-guard.ps1` before planning destructive or wide-impact replay work.

3. Draft the replay plan from `templates/backfill-plan.yaml`.
   Require explicit values for:
   - affected time window and partitions
   - source of truth and downstream targets
   - execution mode (`replay`, `merge`, `overwrite`) and idempotency proof
   - publish pause state and downstream notifications
   - rollback strategy in plain language
   - validation checks with thresholds
   - required approvals

4. Separate incremental from backfill semantics.
   Confirm:
   - concurrency limits differ from daily runs when needed
   - watermark or cursor behavior will not skip or duplicate late data
   - metric definitions remain comparable across the replay window
   - downstream consumers know publish is paused

5. Define reconciliation gates before reopening publish.
   Load `data-reconciliation-and-financial-controls` when correctness must be proven.
   Minimum gates:
   - row count or volume parity within threshold
   - duplicate check on business keys
   - metric reconciliation for business-critical aggregates
   - contract checks on schema and nullability

6. Load companion skills by scenario.
   - cutover or dual-run: `data-migration-and-platform-cutover`
   - incident-driven replay: `incident-triage-and-pipeline-recovery`
   - schedule or dependency changes: `orchestration-and-backfills`

7. Execute in bounded slices.
   Order of operations:
   - dry run or single-partition proof when possible
   - expand to full window only after slice reconciliation passes
   - reopen publish only after all gates pass
   - record evidence in `templates/release-gate-evidence.yaml` when publish-bound

## Replay Plan Checklist

Copy and track before any execution:

```
Backfill gate:
- [ ] templates/backfill-plan.yaml drafted with owner and reason
- [ ] affected window and partitions bounded
- [ ] publish paused and downstream owners notified
- [ ] idempotent write strategy documented
- [ ] rollback strategy documented
- [ ] reconciliation checks defined with thresholds
- [ ] approvals captured
- [ ] dry run or slice proof completed
- [ ] full window reconciliation passed
- [ ] publish reopened only after evidence recorded
```

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is faster to rerun now and reconcile later." | Late reconciliation still leaves corrupted dashboards and irreversible downstream actions. |
| "The job is idempotent so a full rerun is safe." | Idempotency at the job level does not guarantee metric or aggregate correctness across windows. |
| "We only need to backfill one day." | Even small windows can duplicate keys, break slowly changing dimensions, or violate publish contracts. |
| "Rollback can be improvised if metrics look wrong." | Rollback under pressure is slow, incomplete, and often worsens blast radius. |

## Red Flags

- execution starts without a completed backfill plan template
- no publish pause for downstream consumers
- reconciliation thresholds are undefined
- backfill and incremental code paths are conflated
- no bounded slice proof before full-window replay
- rollback strategy is missing or untested

## Verification

- [ ] `templates/backfill-plan.yaml` is complete and approved
- [ ] Publish is paused and stakeholders are notified
- [ ] Idempotency and write strategy are explicit at target grain
- [ ] Reconciliation gates passed before publish reopen
- [ ] Recovery evidence is recorded for audit and future incidents
