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

## Verification

- [ ] The local workflow is reproducible
- [ ] Prototype assumptions are not mistaken for production readiness
- [ ] Promotion steps to the real platform are understood
