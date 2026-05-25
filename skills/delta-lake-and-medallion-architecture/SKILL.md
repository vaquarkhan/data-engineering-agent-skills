---
name: delta-lake-and-medallion-architecture
description: Guides agents through Delta Lake and medallion-style lakehouse design. Use when building or modifying bronze, silver, and gold layers, Delta Lake mutation patterns, streaming-to-batch lakehouse flows, or Databricks-centered serving architectures.
---

# Delta Lake And Medallion Architecture

## Overview

Use this skill when a `Delta Lake`-based lakehouse needs more than generic table-format guidance. It helps agents design medallion-style layers, transactional update behavior, CDC merges, and publish-safe transformation paths for Delta-centric platforms.

## When to Use

- designing `bronze`, `silver`, and `gold` layering
- implementing `Delta Lake` merges, upserts, or deletes
- building `Databricks`-centered batch and streaming lakehouse flows
- deciding how raw landing data evolves into trusted publish outputs

Do not use medallion terminology as decoration if the layers do not carry distinct responsibilities.

## Workflow

1. Define the layer responsibilities.
   Typical pattern:
   - bronze: raw or lightly standardized landing
   - silver: cleaned, conformed, contract-aware transformations
   - gold: business-facing publish-ready outputs

2. Define movement rules between layers.
   Capture:
   - validation requirements
   - mutation behavior
   - CDC merge strategy
   - schema enforcement and evolution policy

3. Keep bronze permissive and gold disciplined.
   Raw survival and publish trust need different operating rules.

4. Coordinate batch and streaming writers carefully.
   Checkpoints, merges, and small-file behavior must support recovery and maintenance.

5. Plan maintenance as part of the architecture.
   Include:
   - compaction
   - retention
   - optimization
   - cleanup

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Bronze, silver, and gold are enough architecture by themselves." | Layer names without contracts and rules create confusion, not design clarity. |
| "We can merge everything directly into gold." | Business-facing layers need stronger validation and stability than raw ingestion paths. |
| "Delta transactions solve every operational problem." | You still need thoughtful layering, maintenance, and replay design. |

## Red Flags

- bronze, silver, and gold have no explicit responsibilities
- gold tables are fed directly from unstable raw landing logic
- merge semantics are unclear for CDC or late data
- maintenance tasks such as compaction are ignored

## Verification

- [ ] Each medallion layer has a distinct purpose and quality bar
- [ ] Movement, validation, and mutation rules between layers are explicit
- [ ] Streaming and batch interaction with Delta tables is operationally safe
- [ ] Maintenance and lifecycle behavior are part of the design
