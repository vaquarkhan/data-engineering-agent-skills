---
name: lakehouse-table-format-engineering
description: Guides agents through lakehouse table design and open table format decisions. Use when designing or changing Iceberg, Delta, Hudi, partitioning, schema evolution, compaction, or batch and streaming interoperability.
---

# Lakehouse Table Format Engineering

## Overview

Use this skill when the storage layer itself is an architecture decision. It helps agents reason about `Iceberg`, `Delta`, `Hudi`, table evolution, partitioning, compaction, snapshot behavior, and how batch and streaming jobs interact with shared lakehouse tables.

## When to Use

- choosing between `Iceberg`, `Delta`, and `Hudi`
- designing lakehouse datasets with update or merge behavior
- changing partition strategy, snapshot retention, or compaction behavior
- integrating `Spark`, `Flink`, or warehouse readers with shared table formats
- implementing CDC-style or incremental lakehouse pipelines

Do not use this for unmanaged flat-file datasets that are not intended to behave like governed tables.

## Workflow

1. Define the table contract.
   Include:
   - grain and keys
   - mutation model
   - read patterns
   - retention and snapshot policy
   - compatibility requirements across engines

2. Pick the table format intentionally.
   - `Iceberg`: strong open-table interoperability and metadata-driven planning
   - `Delta`: strong lakehouse ergonomics and transactional patterns in Databricks-centered stacks
   - `Hudi`: strong incremental and record-level update use cases

3. Design physical layout for lifecycle, not only day-one queries.
   Consider:
   - partition evolution
   - small-file control
   - compaction
   - metadata growth
   - merge and delete behavior

4. Align compute engines with the table behavior.
   Batch and streaming writers must not conflict silently on checkpoints, commits, or schema changes.

5. Define maintenance and recovery operations.
   Table formats require operational housekeeping, not just one-time creation.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "A table format is just a storage detail." | Format choice affects interoperability, maintenance, mutation semantics, and long-term cost. |
| "We can decide compaction later." | Small files and metadata bloat become operational pain quickly. |
| "Any engine can read and write the table the same way." | Cross-engine support varies, especially for advanced write and mutation behavior. |

## Red Flags

- format selection is based only on familiarity
- mutation and delete semantics are undefined
- snapshot retention and cleanup are ignored
- batch and stream writers target the same table without coordination
- interoperability requirements are discovered after adoption

## Verification

- [ ] Table format choice is tied to interoperability and workload needs
- [ ] Mutation, partitioning, retention, and compaction rules are explicit
- [ ] Engine compatibility assumptions are documented
- [ ] Maintenance and recovery procedures exist for the table lifecycle
