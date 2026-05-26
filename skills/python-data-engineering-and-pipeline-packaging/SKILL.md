---
name: python-data-engineering-and-pipeline-packaging
description: Guides agents through Python-based data engineering implementation. Use when building or modifying Python ingestion jobs, orchestration helpers, PySpark entry points, validation code, packaging, dependency management, or operational CLI workflows.
---

# Python Data Engineering And Pipeline Packaging

## Overview

Use this skill when `Python` is the main implementation language for data pipelines or operational data tooling. It helps agents structure jobs as maintainable packages instead of loose scripts, choose the right execution boundary, manage dependencies explicitly, and keep runtime behavior testable and production-safe.

## When to Use

- building or modifying `Python` data pipelines
- packaging `PySpark`, ingestion, validation, or orchestration helper code
- moving from notebooks or scripts into production-ready modules
- managing dependency, environment, and runtime issues in `Python`
- adding CLI entry points, test harnesses, or local development workflows

Do not treat a working script as a production design just because it runs once.

## Workflow

1. Define the role of the Python code.
   Clarify whether it is:
   - a single-node transform
   - a `PySpark` job entry point
   - an orchestration helper
   - a validation or reconciliation tool
   - an integration or extraction service

2. Package logic into explicit modules.
   Prefer:
   - versioned packages
   - reusable modules
   - clear CLI or job entry points
   - isolated configuration
   - minimal hidden global state

3. Make dependency management real.
   Define:
   - environment model
   - pinned dependency strategy
   - native or system dependency assumptions
   - compatibility with runtime platforms such as `Airflow`, `Spark`, or container images

4. Keep runtime boundaries explicit.
   Decide:
   - what runs locally versus distributed
   - what belongs in orchestration versus the job package
   - how configuration, secrets, and environment values are supplied
   - how logs, retries, and exits behave operationally

5. Prove the package is maintainable.
   Require:
   - targeted tests
   - representative input cases
   - type or interface clarity where useful
   - reproducible local execution

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is only a small Python script." | Small scripts often become critical pipeline entry points with no packaging or test discipline. |
| "We can keep the business logic in the DAG or notebook." | Hidden logic in orchestration or notebook state becomes hard to test, reuse, and debug. |
| "Requirements are enough documentation." | Dependency files do not explain runtime assumptions, entry points, or platform compatibility. |

## Red Flags

- pipeline logic lives mostly in one script with no reusable module structure
- notebooks, DAGs, and job code duplicate the same transformation logic
- dependency versions are implicit or environment-specific
- local runs and deployed runs behave differently with no explanation
- secrets or environment assumptions are embedded in code

## Verification

- [ ] The Python code has a clear package and entry-point shape
- [ ] Runtime, dependency, and environment assumptions are explicit
- [ ] Orchestration code and business logic are separated
- [ ] Tests or reproducible execution paths exist for the important logic
