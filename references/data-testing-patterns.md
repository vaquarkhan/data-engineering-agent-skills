# Data Testing Patterns

Use this reference when designing tests and validation evidence for data pipelines, models, contracts, and publishes.

## Test Layers

### Contract Tests

Use when validating schema, required fields, types, keys, compatibility, and allowed change behavior.

Examples:

- source contract shape
- dataset contract enforcement
- schema registry compatibility
- metric contract compatibility

### Transformation Tests

Use when validating that model or pipeline logic preserves the intended business meaning.

Examples:

- dbt schema tests
- deterministic SQL transformation checks
- Spark job output validation
- partition and watermark behavior

### Reconciliation Tests

Use when a critical target must match source reality or another trusted system.

Examples:

- row counts
- sums and financial totals
- accepted value distributions
- source-to-target balance checks

### Freshness And SLA Tests

Use when consumers depend on timing, not only correctness.

Examples:

- freshness windows
- late-arrival tolerance
- publish availability time
- stale-data alerts

### Replay And Backfill Tests

Use when reruns, replay, or cutovers must avoid corruption.

Examples:

- idempotent reruns
- duplicate prevention
- replay window validation
- rollback and publish-close checks

### Resiliency And Failure-Mode Tests

Use when pipelines must prove safe recovery under restart, outage, duplication, or partial publish conditions.

Examples:

- worker restart drills
- upstream outage and backlog catch-up tests
- checkpoint recovery tests
- duplicate delivery tests
- publish block and reopen validation

## Recommended Pattern By Workflow

### New Pipeline

- contract test
- transformation test
- freshness test

### Published Dataset

- contract test
- reconciliation test
- publish-readiness validation

### Streaming System

- schema compatibility test
- watermark or lateness test
- duplicate and replay test

### Regulated Data

- access and masking validation
- lineage and retention evidence
- deletion propagation test

## High-Value Assertions

- required fields stay required
- grain stays stable
- business keys remain unique when expected
- null behavior is explicit
- breaking schema changes are detected before publish
- backfills do not create duplicates
- publish remains blocked until validation passes

## Common Anti-Patterns

- relying only on "the job ran successfully"
- testing only small happy-path samples
- skipping reconciliation for financially important datasets
- skipping replay tests for pipelines that will inevitably be rerun
- never testing how the system recovers from the failures it is expected to survive
- treating dashboard correctness as a substitute for data-model correctness

## Practical Review Checklist

- [ ] Is there at least one contract-level test?
- [ ] Is there evidence that transformation logic is correct?
- [ ] Is reconciliation required for this dataset or metric?
- [ ] Is freshness or SLA part of the proof?
- [ ] Are replay, rerun, or cutover behaviors tested where relevant?
- [ ] Are failure and recovery behaviors tested where relevant?
- [ ] Are validation results captured before publish?

For deeper recovery and failure-drill design, use `references/data-resiliency-testing-patterns.md`.
