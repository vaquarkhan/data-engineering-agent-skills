---
name: warehouse-and-schema-design
description: Guides agents through data warehouse and schema design. Use when defining fact and dimension models, keys, grain, normalization versus denormalization, serving-layer schema boundaries, and downstream-friendly table design.
---

# Warehouse And Schema Design

## Overview

Use this skill when the primary challenge is how data should be modeled for reliable analytics consumption. It helps agents choose good grain, keys, relationships, and serving patterns so downstream work stays understandable and performant.

## When to Use

- designing marts, warehouse schemas, or curated serving tables
- choosing fact and dimension boundaries
- deciding grain, surrogate keys, or relationship strategy
- balancing normalization and denormalization
- restructuring analytics-facing datasets for usability

Do not reduce schema design to column naming alone. Good schema design is about behavior, meaning, and query ergonomics.

## Workflow

1. Define the business grain first.
   Clarify:
   - what one row represents
   - what the primary analysis questions are
   - how time and change should be represented

2. Choose the schema pattern intentionally.
   Common options:
   - dimensional modeling
   - data vault-oriented integration layers
   - normalized serving models for operational analytics
   - denormalized marts for common consumption patterns

3. Define keys and relationships.
   Include:
   - business keys
   - surrogate keys where needed
   - slowly changing behavior
   - null and unknown-member handling

4. Optimize for consumers, not just model purity.
   A perfect logical model that no analyst can use is not successful.

5. Validate compatibility with performance, governance, and metric use.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can figure out grain later." | Grain mistakes spread quickly through metrics and dashboards. |
| "A wide table is always easier for analysts." | Very wide tables often hide conflicting grains and unclear semantics. |
| "Normalization is more correct, so we should always prefer it." | Correctness and usability both matter; serving models need intentional trade-offs. |

## Red Flags

- row grain is undocumented
- fact tables mix incompatible event types
- keys are inconsistent across domains
- schema choices are driven only by current dashboard convenience

## Verification

- [ ] Row grain and key strategy are explicit
- [ ] Schema pattern matches the business use case
- [ ] Consumer usability and performance have been considered
- [ ] Change-over-time behavior is documented where relevant
