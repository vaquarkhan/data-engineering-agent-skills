---
name: apache-hudi-lakehouse
description: Guides agents through Apache Hudi lakehouse design. Use when managing incremental upserts, record-level mutations, timeline behavior, compaction, and Hudi-based lakehouse tables.
---

# Apache Hudi Lakehouse

## Overview

Use this skill when `Apache Hudi` is the primary table layer for incremental lakehouse workloads. It helps agents reason about mutation-heavy patterns, compaction, timeline behavior, and consumer expectations.

## When to Use

- choosing or operating `Apache Hudi`
- building record-level upsert pipelines
- managing compaction and incremental consumption
- supporting lakehouse tables with heavy mutations

## Workflow

1. Define mutation and read patterns.
2. Choose the right Hudi table and indexing behavior.
3. Plan compaction and incremental consumption explicitly.
4. Validate downstream engine compatibility and publish safety.

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

- [ ] Mutation and incremental-read behavior are documented
- [ ] Compaction and maintenance are planned
- [ ] Downstream compatibility is understood
