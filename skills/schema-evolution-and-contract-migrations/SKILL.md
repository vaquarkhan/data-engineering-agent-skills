---
name: schema-evolution-and-contract-migrations
description: Guides agents through schema changes and contract migrations. Use when adding, renaming, removing, or changing columns, data types, nullability, keys, or downstream-facing data contracts.
---

# Schema Evolution And Contract Migrations

## Overview

Use this skill when a schema change can ripple through pipelines, models, dashboards, or external consumers. It helps agents make schema evolution deliberate, compatible, and recoverable.

## When to Use

- changing input or output schemas
- renaming or dropping columns
- changing data types or nullability
- adding keys or changing grain
- migrating consumers from an old contract to a new one

Do not treat schema changes as isolated SQL edits. They are compatibility events.

## Workflow

1. Classify the change.
   Decide whether it is:
   - additive
   - backward compatible
   - breaking
   - temporary dual-schema support

2. Map consumers and blast radius.
   Include:
   - upstream producers
   - downstream models
   - dashboards
   - APIs or extracts
   - external consumers

3. Create the migration path.
   Options may include:
   - dual writes
   - compatibility views
   - phased deprecation
   - explicit consumer cutover windows

4. Validate old and new contracts during the transition.

5. Remove deprecated paths only after confirmation that consumers moved.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is just a column rename." | Renames break dashboards, notebooks, and joins that depend on the old name. |
| "Consumers will update quickly." | Some consumers are undocumented or owned by other teams. |
| "Additive changes are always safe." | New columns can still change file contracts, schemas, and downstream assumptions. |

## Red Flags

- no consumer inventory exists
- breaking changes ship without transition support
- type changes are made without data validation
- deprecation timing is based on hope instead of confirmation

## Verification

- [ ] The change type and compatibility level are classified
- [ ] Consumers and blast radius are identified
- [ ] A migration and rollback path exists
- [ ] Old and new contract behavior are validated during transition
