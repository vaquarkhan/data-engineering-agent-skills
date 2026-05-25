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

## Verification

- [ ] Query latency and schema expectations are explicit
- [ ] Ingestion and materialized view behavior are documented
- [ ] Retention and freshness trade-offs are considered
