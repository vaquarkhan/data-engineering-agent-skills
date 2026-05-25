---
name: reverse-etl-and-operational-data-serving
description: Guides agents through reverse ETL and operational data serving workflows. Use when sending curated warehouse data to business systems, SaaS tools, APIs, activation layers, or operational applications that rely on stable downstream contracts.
---

# Reverse ETL And Operational Data Serving

## Overview

Use this skill when trusted analytical data needs to move back into operational systems. It helps agents design stable outbound contracts, idempotent syncs, destination-aware quality rules, and failure-safe activation pipelines.

## When to Use

- syncing warehouse outputs into SaaS tools
- publishing segments, scores, or entity attributes to operational systems
- designing outbound APIs or activation datasets
- changing operationally consumed data contracts

Do not treat reverse ETL like a simple export job. Operational destinations have side effects and user-facing impact.

## Workflow

1. Define the outbound contract.
   Include:
   - destination system
   - key mapping
   - sync cadence
   - field semantics
   - deletion or unsync behavior

2. Understand the destination constraints.
   Consider:
   - rate limits
   - API semantics
   - idempotency behavior
   - partial update rules
   - rollback limitations

3. Make sync behavior explicit.
   Decide how the system handles:
   - upserts
   - deletes
   - deduplication
   - failures
   - replay

4. Validate business risk before publish.
   A bad reverse-ETL sync can affect campaigns, sales workflows, or customer experience directly.

5. Monitor delivery and divergence.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is just another export." | Operational destinations can create real downstream actions and customer-facing side effects. |
| "We can rerun if something goes wrong." | Replays may duplicate writes or retrigger actions in external tools. |
| "The warehouse model is already trusted." | Destination systems still need contract, mapping, and side-effect safety review. |

## Red Flags

- no destination-aware key mapping exists
- deletes or unsync behavior are undefined
- replay logic ignores external side effects
- sync failures are only visible after business users complain

## Verification

- [ ] Destination constraints and contract are explicit
- [ ] Sync behavior for inserts, updates, deletes, and retries is defined
- [ ] Business side effects and rollback limits are considered
- [ ] Delivery success and divergence are observable
