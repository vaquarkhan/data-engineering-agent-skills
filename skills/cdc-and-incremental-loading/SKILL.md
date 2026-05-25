---
name: cdc-and-incremental-loading
description: Guides agents through change data capture and incremental load design. Use when building or modifying watermark-based loads, upserts, deduplication, merge logic, late data handling, or replayable incremental pipelines.
---

# CDC And Incremental Loading

## Overview

Use this skill when the system changes data over time and full reloads are not the right answer. It helps agents design safe incremental behavior with clear watermarks, merge rules, deduplication, and replay semantics.

## When to Use

- implementing CDC ingestion
- designing watermark-based or timestamp-based incremental loads
- merging inserts, updates, and deletes
- handling late-arriving data
- fixing duplicate or missing incremental records

Do not use this when a bounded full refresh is simpler and operationally safer.

## Workflow

1. Define the change contract.
   Include:
   - business key
   - change key or sequence
   - delete behavior
   - update semantics
   - source ordering guarantees

2. Choose the incremental strategy.
   Typical options:
   - append-only
   - merge/upsert
   - snapshot replacement
   - log-based CDC

3. Make watermark logic explicit.
   Record:
   - watermark column
   - lag tolerance
   - reprocessing window
   - retry and replay rules

4. Guard against duplicates and missed changes.
   Deduplication and late-data handling should be first-class logic.

5. Prove reruns are safe.
   Incremental pipelines that cannot be replayed safely are incomplete.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can just use updated_at as the watermark." | Timestamps alone often miss late changes, clock skew, or delete semantics. |
| "Duplicates are rare enough." | Rare duplicates are still expensive when they affect published metrics. |
| "We can rebuild everything if something goes wrong." | Large backfills are often slow, expensive, or operationally risky. |

## Red Flags

- no documented business key
- delete handling is absent
- watermark logic depends on assumptions no one wrote down
- replay requires manual surgery in production tables

## Verification

- [ ] The incremental contract covers inserts, updates, and deletes where relevant
- [ ] Watermark, lag, deduplication, and replay rules are explicit
- [ ] Late data behavior is defined
- [ ] Reruns and backfills are operationally safe
