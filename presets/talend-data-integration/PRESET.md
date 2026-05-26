---
name: talend-data-integration
description: Adapts the core skills for Talend-centered delivery. Use when pipelines, jobs, metadata, and deployment flows are primarily managed through Talend Studio, Talend Management Console, or Talend Cloud services.
---

# Talend Data Integration

## Overview

Use this preset when `Talend` is a primary execution surface. It maps data engineering workflows to `Talend Studio`, reusable job components, context variables, metadata repositories, deployment bundles, and Talend-managed execution environments.

## Use When

- the platform standard includes `Talend Studio` or `Talend Cloud`
- delivery depends on Talend jobs, context variables, and component-driven transformations
- runtime behavior changes by environment through context configuration
- teams need to stabilize or modernize existing Talend pipelines

## Preferred Platform Services

- transformation design: Talend jobs, reusable routines, and components
- environment management: context groups and deployment configuration
- orchestration: Talend scheduling or external schedulers
- metadata and quality: repository metadata, component-level validation, row-count evidence
- operations: job logs, task execution history, and deployment artifacts

## Design Rules

- Treat context variables and environment bindings as first-class parts of implementation.
- Recover transformation and reject-path logic from jobs before rewriting or migrating them.
- Document component assumptions, generated-code dependencies, and external scripts.
- Add reconciliation and lineage evidence around critical Talend-managed flows.
- Prefer phased coexistence with clear parity checks rather than big-bang migrations.

## Verification

- [ ] Job structure, contexts, and dependencies are documented
- [ ] Environment-specific behavior is explicit and reviewable
- [ ] Reject handling and restart behavior are understood
- [ ] Reconciliation and deployment evidence exist for critical jobs
- [ ] Modernization or coexistence plans define parity, cutover, and rollback
