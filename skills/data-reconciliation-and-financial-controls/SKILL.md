---
name: data-reconciliation-and-financial-controls
description: Guides agents through reconciliation and control design for business-critical data. Use when validating financial, operational, or audit-sensitive metrics with source-to-target totals, control balances, exception tracking, or close-process dependencies.
---

# Data Reconciliation And Financial Controls

## Overview

Use this skill when correctness must be proven with control evidence, not only tests. It helps agents design reconciliations, control totals, exception workflows, and audit-friendly validation for high-trust datasets.

## When to Use

- finance, billing, or revenue pipelines
- audit-sensitive operational datasets
- month-end or close-process data products
- source-to-target control validations
- exception-based review flows

Do not rely on a few spot queries when the business requires reconciled numbers.

## Workflow

1. Define the control objective.
   Clarify:
   - what must reconcile
   - acceptable variance
   - reconciliation frequency
   - owner of exceptions

2. Choose the reconciliation pattern.
   Common patterns:
   - row-count reconciliation
   - control totals
   - aggregate balance checks
   - record-level exception matching

3. Make timing and cutoff rules explicit.
   Reconciliation often depends on accounting windows or source close timing.

4. Capture and route exceptions.

5. Preserve evidence.
   Control systems need reviewable records, not only ephemeral job output.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The transformation logic is simple enough to trust." | Critical numbers still need independent validation evidence. |
| "A small variance is probably fine." | Acceptable variance must be defined, not guessed after a miss. |
| "The warehouse total matches once, so we are done." | Control reliability requires repeatable evidence over time. |

## Red Flags

- no explicit acceptable variance exists
- cutoff timing is undocumented
- exceptions are noticed manually and inconsistently
- control evidence cannot be reproduced later

## Verification

- [ ] Control objectives and acceptable variance are defined
- [ ] Reconciliation logic is explicit and reviewable
- [ ] Exceptions have an owner and workflow
- [ ] Control evidence is retained for audit or review
