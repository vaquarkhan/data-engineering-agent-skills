---
name: data-contract-testing-with-schema-registry
description: Guides agents through data-contract testing using schema registries and compatibility checks. Use when validating event contracts, stream schema evolution, consumer compatibility, or release gates for schema-managed systems.
---

# Data Contract Testing With Schema Registry

## Overview

Use this skill when contracts must be tested through registry-backed compatibility rules, not only by convention. It helps agents make event contract validation a blocking part of build and release behavior with automated testing, consumer impact analysis, and evidence-driven release gates.

## When to Use

- testing event contract changes before production release
- validating schema compatibility as part of CI/CD pipelines
- coordinating producer and consumer schema evolution across teams
- enforcing registry-backed contract quality gates before deployment
- building release evidence that proves schema safety

Do not use this when schemas are not managed through a registry or when the system has no shared event contracts.

## Workflow

1. Define the contract and compatibility target per subject.
   Include:
   - which schema registry subjects are in scope
   - the compatibility level required: `BACKWARD`, `FORWARD`, `FULL`, or `TRANSITIVE` variants
   - who owns the contract (producing team, platform team, or shared)
   - which consumers depend on each subject and their minimum supported version

2. Implement contract tests in CI.
   - register the proposed schema against the registry's compatibility endpoint
   - use the registry's `/compatibility` API to check before merging
   - fail the build if compatibility is violated
   - produce test output showing which rules passed or failed
   - run tests against both the latest registered version and specific consumer versions

3. Test representative producer and consumer scenarios.
   - serialize sample records with the new schema and deserialize with the old
   - verify that default values produce correct behavior for removed or added fields
   - test edge cases: null handling, enum additions, nested record changes
   - for Protobuf: test field number stability and reserved field behavior
   - for Avro: test union type evolution and logical type compatibility

4. Validate downstream consumer impact before release.
   - identify all registered consumers of the subject
   - test that each consumer's current schema can read the proposed producer schema
   - document which consumers need upgrades for breaking changes
   - define the deployment order: consumer upgrade before or after producer change
   - communicate schema changes through established team channels

5. Tie contract test results to release gates.
   - schema compatibility check must pass before deployment proceeds
   - produce structured evidence (JSON report) of compatibility test results
   - store evidence alongside the release artifact for audit
   - block production deploys on compatibility failures — no manual overrides without review
   - include contract test results in pull request checks

6. Plan for contract migrations and breaking changes.
   - when breaking changes are necessary, define a migration plan
   - create a new subject or version namespace for the breaking schema
   - run both old and new contracts in parallel during migration
   - define a deprecation timeline for the old contract
   - document the consumer migration path with explicit deadlines

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We check compatibility manually before releasing." | Manual checks are inconsistent and skip edge cases. Automated registry-backed testing catches issues that humans miss under time pressure. |
| "Adding a field is always safe." | Adding a required field without a default breaks backward compatibility. Adding an optional field is safe only if consumers handle absence correctly. |
| "We only have one consumer so contract testing is overhead." | Consumers multiply over time. Establishing contract testing early prevents breaking changes from accumulating technical debt. |
| "The registry will reject incompatible schemas anyway." | Registry rejection at deploy time is too late. Testing in CI catches issues before code is merged and before release pressure builds. |

## Red Flags

- no contract tests in CI — compatibility is checked only at deploy time
- proposed schemas are registered directly without prior compatibility validation
- consumer dependency map does not exist — nobody knows who reads the events
- breaking changes are deployed with "we'll fix consumers later" attitude
- test output is not stored — no evidence trail for audits
- compatibility policy is set to `NONE` in production subjects
- contract test failures are routinely overridden without review
- migration plans for breaking changes have no timeline or consumer notification

## Verification

- [ ] Compatibility targets are defined per subject and match consumer expectations
- [ ] Contract tests run in CI and block merges on compatibility failures
- [ ] Producer and consumer serialization/deserialization are tested with sample records
- [ ] Consumer dependency map is documented and up to date
- [ ] Contract test evidence is produced, stored, and linked to releases
- [ ] Breaking changes have explicit migration plans with timelines
- [ ] Deployment order (producer-first vs consumer-first) is defined for each change type
