---
name: great-expectations-deequ-and-cuallee
description: Guides agents through data-quality frameworks such as Great Expectations, Deequ, and Cuallee. Use when implementing framework-based validation suites, reusable checks, or evidence-driven data-quality enforcement.
---

# Great Expectations Deequ And Cuallee

## Overview

Use this skill when the team wants structured quality enforcement through a data-quality framework instead of ad hoc checks. It helps agents align contracts, expectation suites, and publish gates.

## When to Use

- creating validation suites
- standardizing reusable checks
- integrating framework-based quality into CI or publish gates

## Workflow

1. Define the contract before choosing the framework shape.
2. Group expectations by dataset purpose and failure severity.
3. Make evidence outputs reviewable.
4. Tie framework results to publish or incident workflows.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The platform-specific feature is the whole design." | Platform features do not replace contract, compatibility, and operational planning. |
| "We can validate this after publish." | Late validation is expensive when downstream consumers already depend on the asset. |
| "Operations can figure out the edge cases later." | Replay, maintenance, and publish safety need to be explicit before adoption. |

## Red Flags

- downstream compatibility is assumed instead of documented
- publish or replay behavior is not explicit
- maintenance, rollback, or observability expectations are missing
## Verification

- [ ] Framework checks are grounded in real contracts
- [ ] Failure severity and routing are explicit
- [ ] Validation output is reviewable and actionable
