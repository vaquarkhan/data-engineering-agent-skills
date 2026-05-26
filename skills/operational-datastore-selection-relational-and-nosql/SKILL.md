---
name: operational-datastore-selection-relational-and-nosql
description: Guides agents through choosing relational operational stores such as MySQL versus NoSQL options such as document, key-value, wide-column, or cache-backed systems. Use when deciding where application-adjacent or pipeline-adjacent operational data should live.
---

# Operational Datastore Selection Relational And NoSQL

## Overview

Use this skill when the real decision is not warehouse modeling, but what operational datastore should hold state, serve requests, or back data-driven application flows. It helps agents choose intentionally between relational systems such as `MySQL` and `PostgreSQL` versus `NoSQL` families such as document, key-value, wide-column, or cache-oriented stores.

## When to Use

- choosing `MySQL` versus `NoSQL` for application-facing or service-facing data
- selecting stores for metadata, idempotency keys, session state, event state, or operational APIs
- deciding whether flexible schema or strict relational constraints matter more
- evaluating consistency, scale, and access-pattern trade-offs
- preventing analytics or pipeline systems from being misused as OLTP stores

Do not treat datastore selection as a brand preference or trend decision.

## Workflow

1. Define the access pattern first.
   Clarify:
   - read versus write ratio
   - request latency expectations
   - query shapes
   - update frequency
   - retention and archival behavior

2. Define integrity and consistency needs.
   Include:
   - transactions
   - joins and relational constraints
   - uniqueness guarantees
   - conflict handling
   - tolerance for eventual consistency

3. Match the workload to the right store family.
   Common guidance:
   - relational stores such as `MySQL` fit well when transactions, constraints, and predictable relational queries matter
   - document stores fit when entity shapes vary and document-oriented retrieval dominates
   - key-value stores fit when lookup by key is primary and access patterns are narrow
   - wide-column stores fit when scale and partition-oriented access dominate
   - caches should accelerate another source of truth, not silently replace one

4. Check downstream and operational impact.
   Consider:
   - CDC and replication support
   - backup and restore behavior
   - schema evolution pain
   - observability and operational maturity
   - how analytics or warehouse ingestion will work

5. Record the trade-off explicitly.
   A good decision names what the chosen store is not good at.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "NoSQL scales better, so we should use it." | Scale is only one axis; transactions, operability, and query ergonomics still matter. |
| "`MySQL` is too old-fashioned for modern systems." | Mature relational systems remain strong choices when consistency and relational integrity are central. |
| "The schema changes a lot, so we need schemaless storage." | Frequent shape change often signals unclear contracts, not necessarily a datastore requirement. |

## Red Flags

- a warehouse or lakehouse is being used like an operational key-value store
- `NoSQL` is chosen with no explicit access-pattern justification
- relational transactions are required but omitted from the design
- a cache is treated as the only source of truth
- CDC, backup, or migration behavior is unknown

## Verification

- [ ] Access patterns and latency needs are explicit
- [ ] Integrity and consistency requirements are named
- [ ] The chosen store family matches the actual workload
- [ ] CDC, backup, migration, and analytics implications are understood
- [ ] Trade-offs and non-goals are documented
