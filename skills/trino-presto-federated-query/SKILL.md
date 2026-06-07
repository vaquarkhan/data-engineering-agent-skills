---
name: trino-presto-federated-query
description: Guides agents through Trino and Presto federated query design. Use when querying across heterogeneous systems, planning semantic consistency, or managing performance and governance in federated analytics.
---

# Trino Presto Federated Query

## Overview

Use this skill when `Trino` or `Presto` sits across multiple data systems as a federated query layer. It helps agents reason about federation boundaries, predicate pushdown limits, consistency trade-offs, performance planning, and governed consumption patterns.

## When to Use

- querying across multiple heterogeneous data stores with `Trino` or `Presto`
- defining governed federated analytics access for users or applications
- managing performance, cost, and semantic consistency across systems
- building a query layer over lakehouse tables, relational databases, and object stores
- planning catalog and connector configuration for multi-source environments

Do not use this when all data lives in a single system or when a materialized serving layer would be simpler and more performant.

## Workflow

1. Define the federation scope and use case.
   Include:
   - which data systems are federated (data lake, warehouse, RDBMS, search, cache)
   - what queries need to cross system boundaries
   - who are the consumers (analysts, applications, dashboards)
   - what latency and concurrency expectations exist
   - is federation for ad-hoc exploration or production query patterns

2. Configure catalogs and connectors with explicit assumptions.
   - document which connector is used for each source and its capabilities
   - understand pushdown support per connector: predicates, projections, aggregations, limits
   - define authentication and access control per catalog
   - test connector behavior for null handling, type mapping, and timezone semantics
   - version connector configurations and treat them as infrastructure code

3. Design queries for federation-aware performance.
   - push filtering to the source where possible — cross-system joins are expensive
   - minimize data movement: filter early, aggregate at the source when pushdown supports it
   - avoid joining large datasets across different connectors — materialize one side first
   - use `EXPLAIN` to verify pushdown behavior before assuming it works
   - set query timeouts and resource limits to prevent runaway federated scans

4. Manage semantic consistency across sources.
   - the same entity in different systems may have different schemas, keys, or freshness
   - define a canonical schema for cross-system entities
   - document freshness differences: real-time source vs daily-refreshed warehouse copy
   - use views or virtual datasets to present consistent semantics to consumers
   - alert when source freshness diverges beyond acceptable thresholds

5. Implement access control and governance.
   - define who can query which catalogs and schemas
   - implement column-level or row-level security where sensitive data is federated
   - audit query patterns: who queries what, how often, and at what cost
   - prevent sensitive data from leaking through cross-system joins
   - document data classification per catalog for security reviews

6. Plan for operations, scaling, and failure modes.
   - define resource groups to isolate workloads and prevent noisy neighbors
   - plan for connector failures: what happens when one source is down?
   - monitor query queue depth, execution time, and memory usage per worker
   - define scaling strategy: add workers vs optimize queries
   - document disaster recovery: can the Trino cluster be rebuilt quickly?
   - plan for catalog and connector upgrades without query disruption

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Federation means we don't need to move data." | Federation moves data at query time instead of ETL time. Large cross-system joins are often slower and more expensive than materialized copies. |
| "Trino pushes everything down automatically." | Pushdown depends on the connector and the query pattern. Not all predicates, aggregations, or joins are pushed — verify with EXPLAIN. |
| "Users can just query everything from one place." | Federated access without governance exposes sensitive data, creates consistency confusion, and generates unexpected costs. Access control is mandatory. |
| "Performance will be fine because the sources are fast." | Federated query performance depends on network latency, pushdown capability, and data volume. A fast source does not guarantee a fast federated query. |

## Red Flags

- cross-system joins on large tables without materialization or pre-filtering
- no `EXPLAIN` verification of pushdown behavior for critical queries
- same entity has conflicting semantics across federated sources with no canonical definition
- no access control beyond "connect to the cluster and query anything"
- resource groups are not configured — one bad query starves all others
- connector failures cause cascading query failures with no graceful degradation
- no monitoring of query cost, duration, or resource consumption per user
- freshness differences between sources are not documented or surfaced to consumers

## Verification

- [ ] Federation scope, sources, and consumer expectations are documented
- [ ] Connector pushdown capabilities are tested and documented per catalog
- [ ] Cross-system queries are designed for pushdown and minimize data movement
- [ ] Semantic consistency is maintained through canonical schemas or governed views
- [ ] Access control and data classification are implemented per catalog
- [ ] Resource groups isolate workloads and prevent noisy-neighbor problems
- [ ] Operations monitoring covers query performance, failures, and resource usage
- [ ] Connector and cluster recovery procedures are documented and tested
