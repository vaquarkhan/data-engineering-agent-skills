---
name: superset-and-metrics-serving
description: Guides agents through Superset and metrics-serving workflows. Use when publishing governed metrics to Superset, defining semantic consistency for dashboards, or managing chart-ready analytical datasets.
---

# Superset And Metrics Serving

## Overview

Use this skill when `Apache Superset` or a similar BI serving surface is the final consumer layer. It helps agents keep chart-ready data aligned with governed metrics, prevent dashboard drift, and manage the boundary between analytical modeling and visualization safely.

## When to Use

- publishing governed datasets into `Superset` for dashboard consumption
- aligning dashboard metrics with centralized semantic definitions
- preventing BI-layer drift from governed metric definitions
- managing access control and row-level security for dashboard datasets
- designing chart-ready schemas that optimize Superset query performance
- operating Superset as part of a broader data platform

Do not use this when the BI tool is self-service only with no governance expectations, or when metrics are exploratory without shared definitions.

## Workflow

1. Define the serving dataset and metric contract.
   Include:
   - which governed datasets or models should be exposed in Superset
   - metric definitions: calculation logic, grain, filters, and time dimensions
   - who owns each dataset and metric in Superset (matching upstream ownership)
   - freshness expectation: how stale can the data be before dashboards mislead?
   - access requirements: who can see which datasets and rows?

2. Design chart-ready schemas for query performance.
   - pre-aggregate where possible — Superset queries should not scan raw tables
   - define time columns explicitly with consistent timezone handling
   - use materialized views or dedicated serving tables for complex metrics
   - minimize joins in Superset SQL Lab — push join logic into the modeling layer
   - index or partition underlying tables to support common filter patterns

3. Keep dashboard metrics aligned with centralized definitions.
   - metrics in Superset must match the source-of-truth definition (dbt metrics, semantic layer)
   - avoid defining calculation logic directly in Superset that diverges from governed models
   - use Superset's metric definition layer to reference pre-built aggregations
   - when definitions change upstream, propagate changes to Superset metadata
   - audit for drift: scheduled comparison between Superset metrics and source definitions

4. Manage access, roles, and row-level security.
   - define Superset roles that map to data classification levels
   - implement row-level security (RLS) for multi-tenant or sensitive datasets
   - do not rely solely on Superset access control — apply defense in depth at the data layer
   - audit access patterns: who views what, and is it appropriate?
   - document the access model so security reviews have a clear reference

5. Separate governed dashboards from exploratory assets.
   - mark governed dashboards with certification or trust badges
   - define lifecycle for exploratory dashboards: auto-archive after inactivity
   - prevent exploratory queries from being mistaken for official metrics
   - establish a promotion path: exploratory → reviewed → certified
   - clean up orphaned charts and datasets regularly

6. Plan operations, monitoring, and incident response.
   - monitor Superset query performance and slow dashboard load times
   - alert when upstream data freshness falls behind dashboard expectations
   - define the incident response when dashboards show wrong numbers
   - plan Superset upgrades and database connection changes
   - backup dashboard definitions and metadata for disaster recovery

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Superset is just a visualization tool — governance doesn't apply." | Superset is where stakeholders consume metrics. Ungoverned dashboards spread wrong numbers faster than any other tool. |
| "Users can define their own metrics in SQL Lab." | Self-defined metrics without governance create conflicting numbers across teams. Governed defaults should exist before self-service. |
| "We don't need row-level security — everyone should see everything." | Access requirements change as data sensitivity increases. Building RLS later is much harder than designing it from the start. |
| "Dashboard performance is the BI team's problem." | Slow dashboards are usually caused by missing pre-aggregation or bad schema design upstream. Performance is a pipeline concern, not just a BI concern. |

## Red Flags

- metrics defined directly in Superset that contradict the governed semantic layer
- dashboards query raw tables with expensive joins instead of pre-aggregated serving tables
- no certification or trust badge to distinguish governed from exploratory dashboards
- row-level security is not implemented despite multi-tenant or sensitive data
- upstream freshness is not monitored — dashboards show stale data without warning
- orphaned dashboards and datasets accumulate without cleanup
- Superset metadata and definitions have no backup or version control
- metric definitions in Superset are never audited against source-of-truth models

## Verification

- [ ] Serving datasets and metric definitions are documented with ownership and freshness SLAs
- [ ] Chart-ready schemas are designed for query performance (pre-aggregation, indexing)
- [ ] Superset metrics align with centralized governed definitions and are audited for drift
- [ ] Access control and row-level security are implemented and documented
- [ ] Governed dashboards are certified and separated from exploratory assets
- [ ] Operations monitoring covers query performance and upstream data freshness
- [ ] Dashboard metadata is backed up and recoverable
