---
name: data-quality-and-contract-testing
description: Drives data implementation with contracts, assertions, and validation evidence. Use when adding or changing ingestion logic, transformations, schemas, or published data products.
---

# Data Quality And Contract Testing

## Overview

Data work is not complete when code runs. It is complete when source assumptions, output contracts, and quality checks prove the behavior is correct.

## When to Use

- new source ingestion
- schema changes
- transformation logic updates
- new or changed published tables
- bug fixes involving bad data or broken metrics

Do not use this only as a final cleanup step. It should guide implementation from the start.

## Workflow

1. Define the contract before implementation.
   Capture:
   - required fields
   - key constraints
   - expected types
   - allowed null behavior
   - freshness expectations
   - reconciliation rules

2. Write the validation plan first.
   Common validations:
   - uniqueness
   - non-null thresholds
   - referential integrity
   - accepted values
   - row count deltas
   - source-to-target totals

3. Reproduce data bugs with a failing check.
   If an incident or defect exists, write the failing validation or test before changing the pipeline.

4. Implement the smallest change that satisfies the contract.

5. Run the relevant validations and capture evidence.
   Evidence may include:
   - test output
   - query results
   - sample reconciliation output
   - dry-run logs

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The warehouse query looks right." | Visual inspection does not scale and misses edge cases. |
| "We will add checks after the model stabilizes." | Unchecked pipelines create low-trust data and harder incident response. |
| "A successful job means the data is valid." | Jobs succeed while still producing incorrect or incomplete data. |

## Red Flags

- no contract exists for a published dataset
- an incident fix ships without a failing reproduction check
- only happy-path sample data is validated
- freshness or completeness expectations are absent

## Verification

- [ ] Contracts are written before or alongside implementation
- [ ] Relevant checks exist for correctness, completeness, and freshness
- [ ] Defects are reproduced with a failing validation before the fix
- [ ] Evidence from validation is captured and reviewable
