---
name: test-data-preparation-and-synthetic-data
description: Guides agents through preparing test data, masked fixtures, and synthetic datasets for development, QA, and lower environments. Use when teams need representative but safe data for validation, demos, training, or release testing.
---

# Test Data Preparation And Synthetic Data

## Overview

Use this skill when data work needs realistic test inputs without depending on unsafe copies of production. It helps agents decide when to use masked subsets, synthetic data, seeded fixtures, or contract-shaped test datasets.

## When to Use

- building lower-environment validation datasets
- preparing integration-test or QA data
- creating representative demo or training datasets
- generating synthetic data that preserves shape and edge cases
- defining seeded fixtures for pipelines, dbt, or Spark jobs

Do not assume production copies are the default answer for testing.

## Workflow

1. Define the testing objective.
   Clarify whether the data is needed for:
   - contract validation
   - business-logic testing
   - performance rehearsal
   - UI or dashboard testing
   - demo or training use

2. Choose the right test-data source.
   Decide between:
   - synthetic data generated from contracts
   - masked or tokenized production subsets
   - hand-authored fixtures for narrow edge cases
   - sampled lower-environment copies with strict controls

3. Preserve the behaviors that matter.
   Include:
   - edge cases
   - null patterns
   - cardinality and skew
   - late or duplicate events
   - partition or date-range coverage

4. Remove unsafe dependencies on production.
   Make sure:
   - identifiers are masked or replaced
   - sensitive values are not recoverable
   - secrets and direct production connections are not needed to regenerate the test set

5. Version and document the dataset.
   Record:
   - generation method
   - intended use
   - refresh cadence
   - limitations versus production behavior

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We need real data or the tests are useless." | Many test goals are satisfied by synthetic or masked data when the right shape and edge cases are preserved. |
| "A quick production copy is faster." | Unsafe lower-environment copies often become long-lived risk surfaces. |
| "The happy path sample is enough." | Test data that omits skew, nulls, duplicates, or boundary conditions gives false confidence. |

## Red Flags

- lower environments depend on live production extracts
- synthetic data ignores edge cases that drive failures
- masked datasets can still reveal identities or business-sensitive values
- no one can reproduce or refresh the test dataset safely

## Verification

- [ ] The testing objective is explicit
- [ ] The chosen test-data strategy matches the risk and realism needed
- [ ] Sensitive values are removed or protected appropriately
- [ ] Edge cases, skew, and replay behaviors are represented where relevant
- [ ] The dataset can be regenerated or refreshed safely
