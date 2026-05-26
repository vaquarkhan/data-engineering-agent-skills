---
name: unity-catalog-and-lakehouse-governance
description: Guides agents through Unity Catalog governance workflows for Databricks lakehouses. Use when defining catalogs, schemas, external locations, access boundaries, shares, lineage, and cross-workspace governance for governed Delta Lake, ML, analytics, and serving assets.
---

# Unity Catalog And Lakehouse Governance

## Overview

Use this skill when `Unity Catalog` is the core governance surface for a `Databricks` platform. It helps agents design governed boundaries across catalogs, schemas, storage locations, shares, and access paths for lakehouse data products.

## When to Use

- designing `Unity Catalog` hierarchy and ownership
- defining external locations, credentials, and storage boundaries
- governing shared `Delta` tables, views, volumes, or models
- reviewing cross-workspace or multi-team lakehouse governance
- planning secure sharing, publish approvals, or governed consumer access

Do not reduce `Unity Catalog` to permissions only. It is also a publish, ownership, and operating-boundary decision.

## Workflow

1. Define the governance hierarchy.
   Decide:
   - catalog boundaries
   - schema boundaries
   - producer versus consumer separation
   - ownership and stewardship paths

2. Define storage and credential boundaries.
   Cover:
   - external locations
   - managed versus external tables
   - storage credentials
   - workspace and environment separation

3. Define access and sharing behavior.
   Include:
   - roles and groups
   - row or column restrictions where needed
   - governed views
   - cross-team or external sharing expectations

4. Align governance with lakehouse delivery.
   Require:
   - clear publish layers
   - lineage visibility
   - certification or trust signals
   - handling for schema and contract change

5. Validate day-2 operations.
   Review how promotions, new workspaces, external consumers, and object-store boundaries behave under the governance model.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We already use Databricks, so Unity Catalog design is obvious." | Poor catalog and location design creates long-term friction in ownership, sharing, and environment boundaries. |
| "We can give broad workspace access and tighten later." | Over-broad access becomes hard to unwind once shared data products are adopted. |
| "Lineage comes for free." | Platform lineage is useful only when publish boundaries and ownership are designed intentionally. |

## Red Flags

- catalogs and schemas do not map to ownership or publish boundaries
- external locations and credentials are inconsistent or ad hoc
- workspace separation and environment promotion are vague
- sharing or external-consumer behavior is undocumented
- governed lakehouse objects are published without trust or lineage signals

## Verification

- [ ] Catalog, schema, and ownership boundaries are intentional
- [ ] Storage and credential boundaries are explicit
- [ ] Access and sharing rules fit the consumer model
- [ ] Publish and lineage expectations are visible
- [ ] Promotions and day-2 operations work with the governance design
