---
name: data-platform-ci-cd-and-release-management
description: Guides agents through CI/CD and release management for data platforms. Use when promoting pipeline code, SQL models, contracts, infra, or configuration across environments with validation gates, staged rollout, and rollback awareness.
---

# Data Platform CI CD And Release Management

## Overview

Use this skill when changes need controlled promotion across environments. It helps agents design release gates for code, contracts, infra, and datasets so teams can ship faster without losing trust.

## When to Use

- adding or changing CI pipelines for data projects
- promoting changes from dev to staging to production
- releasing `dbt`, orchestration, infra, or schema updates
- defining rollback-aware deployment behavior

Do not treat data releases like app-only deploys. Data contracts, backfills, and environment state matter too.

## Workflow

1. Identify the release surface.
   Include:
   - code
   - SQL models
   - infra
   - contracts
   - orchestration config
   - published datasets

2. Define validation gates per stage.
   Common gates:
   - lint or formatting
   - tests
   - contract validation
   - sample or shadow runs
   - reconciliation

3. Separate deployment from publish where needed.

4. Make rollback and forward-fix expectations explicit.

5. Record release ownership and approval points for high-risk changes.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "If tests pass, the data release is safe." | Data releases often need contract, reconciliation, and environment checks too. |
| "We can deploy and publish in one step." | Deployment and downstream visibility should not always be coupled. |
| "Rollback is easy because Git exists." | Rollback for data state and published outputs is often harder than code rollback. |

## Red Flags

- environment promotion rules are unclear
- releases do not separate code success from publish safety
- rollback is mentioned but not operationally real
- high-risk changes have no staged validation

## Verification

- [ ] Release surfaces and environment boundaries are explicit
- [ ] Validation gates exist for the change type
- [ ] Publish behavior is controlled where needed
- [ ] Rollback or forward-fix expectations are documented
