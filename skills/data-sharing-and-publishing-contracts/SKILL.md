---
name: data-sharing-and-publishing-contracts
description: Guides agents through publishing data products for internal or external consumers. Use when sharing tables, files, extracts, APIs, or reverse-ETL-ready outputs that require stable contracts, ownership, and communication.
---

# Data Sharing And Publishing Contracts

## Overview

Use this skill when data leaves the producing team and becomes a product for other teams, systems, or partners. It helps agents define stable publish contracts with ownership, compatibility, and operational expectations.

## When to Use

- publishing curated tables or marts
- sharing extracts or files with other teams or partners
- exposing governed data through APIs or reverse ETL
- modifying an existing consumer-facing dataset

Do not publish widely-used data with implicit contracts.

## Workflow

1. Define the published contract.
   Include:
   - owner
   - audience
   - schema
   - grain
   - delivery method
   - freshness and retention expectations

2. Identify compatibility and versioning needs.

3. Define access and usage boundaries.
   Capture:
   - allowed consumers
   - privacy constraints
   - SLA expectations
   - communication path for changes

4. Validate publish readiness before release.

5. Document change policy.
   Consumers should know what can change, how they will be notified, and how long deprecated behavior lasts.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is just one extract for another team." | One-off exports often become critical dependencies. |
| "Consumers can ask if something changes." | Many consumers only discover changes after failure. |
| "The schema tells them everything they need." | Delivery timing, freshness, retention, and ownership matter too. |

## Red Flags

- published outputs have no owner
- delivery or freshness expectations are missing
- breaking changes are shipped without versioning or notice
- access boundaries are unclear for shared datasets

## Verification

- [ ] The publish contract covers audience, schema, delivery, and freshness
- [ ] Ownership and communication path are defined
- [ ] Compatibility and access expectations are explicit
- [ ] Release readiness is validated before consumers depend on it
