---
name: dbt-and-analytics-engineering
description: Guides agents through analytics engineering workflows with dbt. Use when building or modifying staging models, marts, tests, snapshots, documentation, exposures, or semantic-layer-facing models.
---

# dbt And Analytics Engineering

## Overview

Use this skill when the job is analytics engineering rather than raw ingestion. It helps agents build trustworthy `dbt` projects with clear layering, reusable models, tests, documentation, and publish-safe business definitions.

## When to Use

- creating or changing `dbt` models
- building staging, intermediate, or mart layers
- adding tests, snapshots, or exposures
- organizing business logic for analysts and BI tools
- preparing semantic-layer-friendly outputs

Do not use this to justify putting ingestion or orchestration logic inside `dbt`.

## Workflow

1. Confirm the model's role.
   Decide whether it belongs in:
   - staging
   - intermediate
   - marts
   - snapshot or semantic-serving layers

2. Define the business grain and contract.
   Capture:
   - keys
   - metric intent
   - filter logic
   - null handling
   - freshness expectations

3. Add tests and documentation with the model.
   Typical checks:
   - unique
   - not null
   - relationships
   - accepted values
   - source freshness where relevant

4. Keep model boundaries clean.
   Avoid mixing raw cleanup, business logic, and publish semantics in one model.

5. Validate downstream usability.
   Make sure the output is understandable to analysts, dashboards, and metric consumers.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is only SQL, we do not need model structure." | Poor layering creates brittle marts and duplicate business logic. |
| "We can add tests after the dashboard is working." | Untested metrics create trust problems that are hard to unwind. |
| "A giant model is easier to maintain." | Monolithic models hide grain changes, assumptions, and reuse opportunities. |

## Red Flags

- model grain is unclear
- business logic is duplicated across marts
- no YAML tests or documentation accompany the change
- publish models depend directly on raw sources without clear staging

## Verification

- [ ] The model has a clear layer and business purpose
- [ ] Grain, keys, and metric assumptions are explicit
- [ ] Tests and documentation ship with the model
- [ ] Output usability for downstream consumers has been considered
