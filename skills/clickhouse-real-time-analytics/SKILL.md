---
name: clickhouse-real-time-analytics
description: Guides agents through ClickHouse-based real-time analytics design. Use when building fast analytical serving layers, event aggregations, materialized views, or low-latency metric access patterns.
---

# ClickHouse Real Time Analytics

## Overview

Use this skill when `ClickHouse` is the target for low-latency analytical serving. It helps agents design ingestion, partitioning, materialized views, and query-ready schemas for fast reads.

## When to Use

- real-time analytics serving with `ClickHouse`
- event-heavy analytical aggregation
- low-latency dashboards and metrics

## Workflow

1. Define latency and query expectations.
2. Design schemas, partitions, and materialized views intentionally.
3. Align ingestion patterns with freshness and merge behavior.
4. Validate cost, retention, and downstream metric semantics.

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

- [ ] Query latency and schema expectations are explicit
- [ ] Ingestion and materialized view behavior are documented
- [ ] Retention and freshness trade-offs are considered
