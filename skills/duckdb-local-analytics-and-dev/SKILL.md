---
name: duckdb-local-analytics-and-dev
description: Guides agents through DuckDB-based local analytics and development workflows. Use when prototyping models locally, validating transformations, reproducing data issues quickly, or building lightweight analytical tooling without a full warehouse.
---

# DuckDB Local Analytics And Dev

## Overview

Use this skill when `DuckDB` is the fastest path to local analytical iteration. It helps agents build reproducible local workflows that accelerate development without confusing prototype convenience for production architecture.

## When to Use

- prototyping data models and transformations locally before deploying to a warehouse
- reproducing production data issues with sample datasets
- running analytical queries during development without remote infrastructure
- building lightweight CLI tools, validators, or test harnesses
- validating dbt models locally with `dbt-duckdb` adapter
- creating proof-of-concept demonstrations with embedded analytics

Do not use this when the workload requires production durability, concurrent access, or distributed processing. DuckDB is a development and prototyping accelerator, not a production warehouse replacement.

## Workflow

1. Define the purpose and scope of the local workflow.
   Include:
   - what question or validation is this workflow answering?
   - what sample data is needed and where does it come from?
   - is this a one-time investigation or a repeatable development workflow?
   - what is the promotion path to production if the prototype succeeds?

2. Set up reproducible data inputs.
   - use sample files (CSV, Parquet, JSON) checked into the repository or downloaded by script
   - document how sample data was generated or extracted
   - keep sample sizes representative but small enough for fast iteration
   - use DuckDB's ability to read Parquet, CSV, and JSON directly without import steps
   - for sensitive data: use anonymized or synthetic samples only

3. Write transformations that map cleanly to production equivalents.
   - use standard SQL that translates to the target warehouse dialect
   - avoid DuckDB-specific functions unless the workflow stays local permanently
   - structure queries in the same layered pattern (staging → intermediate → marts) as production
   - when using `dbt-duckdb`: use the same model structure and tests as the production adapter
   - document which DuckDB-specific features would need replacement in production

4. Validate results locally with assertions and contract checks.
   - run row count checks, null assertions, and key uniqueness tests
   - compare output against expected results or golden files
   - use DuckDB's SUMMARIZE and descriptive statistics for quick sanity checks
   - integrate with the project's validation framework (Great Expectations, Cuallee, or custom)

5. Document the production promotion path.
   - what must change before this prototype runs in production?
   - list DuckDB-specific assumptions: single-node, in-process, file-based storage
   - define the target platform (Snowflake, BigQuery, Redshift, Spark) and dialect differences
   - identify features that need distributed execution (large joins, window functions at scale)
   - make promotion a conscious decision, not an accident

6. Keep the local workflow maintainable.
   - include a `Makefile` or script that runs the full local workflow from scratch
   - pin DuckDB version in requirements to prevent drift
   - clean up temporary databases between runs
   - document expected execution time so developers know what's normal
   - retire local workflows that no longer serve a purpose

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "DuckDB is so fast, we can just use it in production." | DuckDB is single-process and file-based. Production workloads need concurrency, durability, and operational tooling that DuckDB does not provide. |
| "The local prototype is basically the same as production." | Local prototypes skip authentication, network, concurrency, and scale concerns. The gap between local and production must be explicitly documented. |
| "We don't need sample data management — just point at production files." | Pointing at production data from local machines creates security and size problems. Curated samples are safer and faster. |
| "It works locally so it will work in the warehouse." | DuckDB SQL is largely standard but not identical to Snowflake, BigQuery, or Redshift dialects. Promotion requires testing on the real target. |

## Red Flags

- local DuckDB workflow is treated as production without a promotion plan
- sample data includes real PII or production secrets
- DuckDB-specific functions are used without documenting production equivalents
- no Makefile or script to reproduce the workflow from scratch
- local workflow runs against full production-scale files on a laptop
- prototype models are deployed to production without validation on the target platform
- temporary DuckDB databases accumulate without cleanup
- DuckDB version is not pinned, causing inconsistent results across team members

## Verification

- [ ] The purpose and scope of the local workflow are documented
- [ ] Sample data is reproducible, appropriately sized, and free of sensitive content
- [ ] SQL transformations use standard patterns that map to the target production platform
- [ ] Local assertions and contract checks validate correctness
- [ ] The production promotion path is documented with explicit dialect differences
- [ ] A Makefile or script reproduces the full workflow from a clean state
- [ ] DuckDB version is pinned and consistent across the team
