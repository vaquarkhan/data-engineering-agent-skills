---
name: data-contract-testing-with-schema-registry
description: Guides agents through data-contract testing using schema registries and compatibility checks. Use when validating event contracts, stream schema evolution, consumer compatibility, or release gates for schema-managed systems.
---

# Data Contract Testing With Schema Registry

## Overview

Use this skill when contracts must be tested through registry-backed compatibility rules, not only by convention. It helps agents make event contract validation part of build and release behavior.

## When to Use

- testing event contract changes before release
- validating schema compatibility in CI
- coordinating producer and consumer evolution
- enforcing registry-backed contract quality gates

## Workflow

1. Define the contract and compatibility target.
2. Run compatibility checks before publish.
3. Test representative producer and consumer cases.
4. Tie failures to release blocking or explicit review.

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

- [ ] Compatibility targets are explicit
- [ ] Contract validation is part of release behavior
- [ ] Producer and consumer evolution risks are tested
