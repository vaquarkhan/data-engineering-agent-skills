---
name: data-mesh-and-domain-oriented-design
description: Guides agents through domain-oriented data product and data mesh design. Use when organizing ownership, domain boundaries, federated governance, and shared platform responsibilities across multiple teams.
---

# Data Mesh And Domain-Oriented Design

## Overview

Use this skill when the problem is organizational scale as much as technical scale. It helps agents design domain-owned data products with explicit boundaries, interoperable contracts, and platform guardrails that do not collapse back into central bottlenecks.

## When to Use

- designing domain-oriented data products
- defining ownership boundaries across multiple teams
- introducing or refining a data mesh operating model
- clarifying platform versus domain responsibilities
- reducing central-team bottlenecks in large data organizations

Do not use this to rename ordinary pipelines as "data products" without ownership, contracts, or service expectations.

## Workflow

1. Identify domains and business boundaries.
   Clarify:
   - which team owns the source behavior
   - which team owns publish-ready data
   - where cross-domain dependencies exist

2. Define data products, not just datasets.
   A data product should include:
   - owner
   - contract
   - consumers
   - freshness expectations
   - support and change path

3. Separate domain ownership from platform ownership.
   Platform teams should provide capabilities, standards, and guardrails rather than own every dataset.

4. Define federated governance rules.
   Include:
   - minimum contract rules
   - lineage requirements
   - discoverability
   - security and privacy baselines

5. Check whether mesh adds real value.
   Not every small team or simple platform needs full mesh operating complexity.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can call every table a data product." | Without ownership and service expectations, it is just a dataset with better branding. |
| "Data mesh means no central standards." | Federated governance still needs common interoperability rules. |
| "Each domain can optimize however it wants." | Unbounded local choices make shared discovery, trust, and reuse much worse. |

## Red Flags

- data products have no named owner
- domain boundaries are driven only by org chart convenience
- the platform team still owns operational details for every domain pipeline
- governance standards are implied but not codified

## Verification

- [ ] Domain boundaries and ownership are explicit
- [ ] Data products have contracts, consumers, and support expectations
- [ ] Platform versus domain responsibilities are clearly separated
- [ ] Federated governance rules exist for interoperability and trust
