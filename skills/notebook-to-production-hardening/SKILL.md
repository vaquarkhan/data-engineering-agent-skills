---
name: notebook-to-production-hardening
description: Guides agents through converting exploratory notebooks into production-ready data jobs. Use when operationalizing notebooks from Databricks, Jupyter, or similar environments into tested, packaged, repeatable workflows.
---

# Notebook To Production Hardening

## Overview

Use this skill when a notebook has outgrown exploration and needs to become a maintainable delivery artifact. It helps agents separate experimentation from production packaging, testing, configuration, and orchestration.

## When to Use

- moving notebook logic into scheduled jobs
- hardening `Databricks` or `Jupyter` notebooks for repeated use
- extracting reusable logic from cells into modules or packages
- improving testability and deployment discipline

Do not treat a manually rerun notebook as production just because it worked once.

## Workflow

1. Separate exploratory work from production logic.
   Identify:
   - reusable transformation code
   - parameters
   - environment assumptions
   - manual steps

2. Extract logic into versioned, testable units.

3. Replace hidden state with explicit inputs and configuration.

4. Add validation and operational hooks.
   Include:
   - contracts
   - logging
   - error handling
   - retry-safe outputs

5. Define how the job is deployed and monitored.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The notebook already works." | Interactive success does not mean repeatable, testable, or observable production behavior. |
| "We can keep using widgets and manual edits." | Hidden runtime state makes failures and reproducibility much worse. |
| "We will modularize later." | Notebook sprawl grows quickly once other teams depend on it. |

## Red Flags

- business logic depends on cell order
- configuration is hard-coded in notebook cells
- outputs are written with no validation or idempotency plan
- the deployment path is undefined

## Verification

- [ ] Reusable logic is extracted from the notebook flow
- [ ] Inputs, configuration, and outputs are explicit
- [ ] Validation, logging, and retry-safe behavior exist
- [ ] The production deployment and monitoring model are defined
