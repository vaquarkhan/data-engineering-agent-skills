---
name: informatica-data-integration
description: Adapts the core skills for Informatica-centered delivery. Use when pipelines, mappings, parameter files, and promotion workflows are primarily managed through Informatica PowerCenter, IICS, or adjacent enterprise integration tooling.
---

# Informatica Data Integration

## Overview

Use this preset when `Informatica` is a primary delivery surface. It maps data engineering workflows to `PowerCenter`, `Informatica Intelligent Cloud Services (IICS)`, parameter files, repository metadata, workflow scheduling, and enterprise integration controls.

## Use When

- the platform standard includes `Informatica PowerCenter` or `IICS`
- critical logic is encoded in mappings, mapplets, workflows, or taskflows
- environment promotion depends on repository objects and parameterization
- teams are modernizing or coexisting with `Informatica` and newer data platforms

## Preferred Platform Services

- transformation design: mappings, mapplets, reusable transformations
- orchestration: workflows, taskflows, or external schedulers
- connectivity: native connectors, agents, and managed runtime integration services
- metadata and lineage: repository exports, runtime logs, and platform metadata
- quality and controls: reject files, session logs, row-count evidence, reconciliation queries

## Design Rules

- Treat mapping exports, parameter files, and scheduler dependencies as part of the real implementation.
- Make environment-specific connection behavior explicit before migration or refactoring.
- Preserve restart, checkpoint, and reject-handling semantics during modernization.
- Add reconciliation around critical loads instead of trusting successful session status alone.
- Prefer incremental extraction of business logic from GUI artifacts into versioned documentation and tests.

## Verification

- [ ] Mappings, workflows, and parameter dependencies are documented
- [ ] Environment-specific connections and promotion rules are explicit
- [ ] Restart, reject, and recovery semantics are known
- [ ] Reconciliation and operational evidence exist around key jobs
- [ ] Migration or coexistence boundaries are clear where modernization is in scope
