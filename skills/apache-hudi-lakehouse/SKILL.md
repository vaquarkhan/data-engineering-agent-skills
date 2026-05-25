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

## Verification

- [ ] Mutation and incremental-read behavior are documented
- [ ] Compaction and maintenance are planned
- [ ] Downstream compatibility is understood
