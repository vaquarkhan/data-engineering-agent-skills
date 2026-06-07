---
name: clickhouse-real-time-analytics
description: Guides agents through ClickHouse-based real-time analytics design. Use when building fast analytical serving layers, event aggregations, materialized views, or low-latency metric access patterns.
---

# ClickHouse Real Time Analytics

## Overview

Use this skill when `ClickHouse` is the target for low-latency analytical serving. It helps agents design ingestion, partitioning, materialized views, and query-ready schemas for fast reads while maintaining operational safety and cost control.

## When to Use

- designing or modifying `ClickHouse` tables for real-time analytics
- building event-heavy analytical aggregation layers
- creating materialized views for pre-computed metrics
- optimizing low-latency dashboards and metric APIs
- planning ingestion patterns for high-throughput event streams

Do not use this when the workload is better served by a transactional database or a batch-oriented warehouse with no latency requirement.

## Workflow

1. Define latency, freshness, and query access patterns.
   Include:
   - acceptable query latency targets (p50, p99)
   - data freshness requirements (seconds, minutes, eventual)
   - primary query patterns (point lookups, time-range scans, aggregations)
   - expected concurrent query load and user base

2. Choose the right table engine and schema design.
   - `MergeTree` family for most analytical workloads
   - `ReplacingMergeTree` for deduplication on eventual consistency
   - `AggregatingMergeTree` for pre-aggregated rollups
   - `CollapsingMergeTree` or `VersionedCollapsingMergeTree` for mutable state
   - define sort keys aligned with primary query filters
   - choose partition keys for lifecycle management, not query speed

3. Design ingestion for throughput and merge safety.
   - batch inserts over single-row writes (target 1000+ rows per insert)
   - avoid too many partitions — high partition counts cause merge pressure
   - use `Buffer` tables or async insert when write concurrency is high
   - define deduplication strategy if at-least-once delivery is the source guarantee

4. Build materialized views with explicit contracts.
   - materialized views are insert-triggered, not retroactive
   - define what happens when the source schema changes
   - document the lag between source insert and view availability
   - test that view aggregations remain correct after merges

5. Plan retention, TTL, and storage tiering.
   - use TTL expressions for automatic partition drops
   - separate hot and cold storage tiers if cost is a concern
   - document retention SLA for each table
   - test that TTL does not silently drop data consumers still need

6. Make operations observable and recoverable.
   - monitor merge backlog, parts count, and replication lag
   - alert on query latency degradation and memory pressure
   - plan for cluster scaling: shard count, replica count, and rebalancing
   - define backup and restore procedures for critical tables

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "ClickHouse is fast so we don't need to optimize schema." | Sort keys, partition choices, and engine selection determine whether queries hit milliseconds or seconds. Speed is designed, not guaranteed. |
| "We can just insert one row at a time." | Single-row inserts cause excessive parts, merge pressure, and eventual degradation. Batching is not optional at scale. |
| "Materialized views handle everything automatically." | Views are insert-triggered and depend on merge behavior. Schema changes, backfills, and retroactive corrections require explicit planning. |
| "Retention is not urgent — storage is cheap." | Unbounded growth increases merge overhead, backup time, and query scan ranges. TTL and lifecycle management are operational requirements. |

## Red Flags

- single-row inserts in production without buffering
- partition key chosen for query speed instead of lifecycle management
- materialized views with no documentation of lag or schema change behavior
- no retention or TTL policy on high-volume tables
- sort key does not align with primary query patterns
- no monitoring of merge backlog or parts count
- cluster scaling plan is undefined despite growing data volumes
- backfill strategy assumes materialized views will retroactively process old data

## Verification

- [ ] Query latency, freshness, and access pattern requirements are documented
- [ ] Table engine, sort key, and partition key choices are justified
- [ ] Ingestion uses batched writes with explicit deduplication strategy
- [ ] Materialized views have documented contracts, lag expectations, and schema change plans
- [ ] TTL and retention policies are defined for all high-volume tables
- [ ] Operational monitoring covers merge backlog, parts count, replication lag, and query latency
- [ ] Scaling and recovery procedures are documented
