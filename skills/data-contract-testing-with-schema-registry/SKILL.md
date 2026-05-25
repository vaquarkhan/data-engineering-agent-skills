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

## Verification

- [ ] Compatibility targets are explicit
- [ ] Contract validation is part of release behavior
- [ ] Producer and consumer evolution risks are tested
