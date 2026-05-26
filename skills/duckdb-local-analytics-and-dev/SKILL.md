---
name: duckdb-local-analytics-and-dev
description: Guides agents through DuckDB-based local analytics and development workflows. Use when prototyping models locally, validating transformations, reproducing data issues quickly, or building lightweight analytical tooling without a full warehouse.
---

# DuckDB Local Analytics And Dev

## Overview

Use this skill when `DuckDB` is the fastest path to local analytical iteration. It helps agents build reproducible local workflows without confusing prototype convenience for production architecture.

## When to Use

- local data modeling and debugging
- reproducing warehouse issues quickly
- prototyping transformations before platform deployment
- lightweight analytical tooling and tests

## Workflow

1. Define the purpose of the local DuckDB workflow.
2. Keep local reproducibility explicit through inputs and scripts.
3. Use local validation to accelerate feedback, not bypass production rules.
4. Document what must change before production rollout.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The platform-specific feature is the whole design." | Platform features do not replace contract, compatibility, and operational planning. |
| "We can validate this after publish." | Late validation is expensive when downstream consumers already depend on the asset. |
| "Operations can figure out the edge cases later." | Replay, maintenance, and publish safety need to be explicit before adoption. |

## Red Flags

- downstream compatibility is assumed instead of documented
- publish or replay behavior is not explicit
- maintenance, rollback, or observability expectations are missing
## Verification

- [ ] The local workflow is reproducible
- [ ] Prototype assumptions are not mistaken for production readiness
- [ ] Promotion steps to the real platform are understood
