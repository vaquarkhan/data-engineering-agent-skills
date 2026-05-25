---
name: api-and-saas-ingestion-patterns
description: Guides agents through API and SaaS ingestion workflows. Use when extracting data from REST, GraphQL, or SaaS platforms with pagination, rate limits, auth rotation, backfills, or unstable source contracts.
---

# API And SaaS Ingestion Patterns

## Overview

Use this skill when the source system is an external API or SaaS platform rather than a database or file drop. It helps agents design reliable extraction, pagination, throttling, auth handling, and backfill-safe ingestion contracts.

## When to Use

- extracting from REST or GraphQL APIs
- ingesting SaaS platform data
- handling pagination, cursors, or sync tokens
- dealing with rate limits and source-side throttling
- backfilling historical API data safely

Do not treat APIs like static tables. They change behavior, availability, and limits over time.

## Workflow

1. Define the source contract.
   Include:
   - endpoint or object name
   - auth method
   - extraction window
   - pagination style
   - rate limits
   - data freshness expectations

2. Design for extraction resilience.
   Handle:
   - retries
   - backoff
   - token refresh
   - idempotent re-fetch behavior
   - partial page failure

3. Make incremental behavior explicit.
   Decide whether the source supports:
   - updated timestamps
   - cursors
   - change tokens
   - full snapshots only

4. Record raw source evidence where useful.
   API sources often need raw response retention for incident diagnosis.

5. Validate contracts against source drift.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can just loop through pages." | Pagination bugs and retry gaps often cause silent data loss. |
| "The vendor API is stable enough." | SaaS APIs change rate limits, fields, and semantics more often than teams expect. |
| "If a request fails, we can rerun later." | Without windowing and idempotency rules, reruns can miss or duplicate data. |

## Red Flags

- no rate-limit strategy exists
- extraction windows depend on undocumented source behavior
- retries ignore duplicate or partial-page risks
- auth rotation and token expiry are not considered

## Verification

- [ ] The source contract covers pagination, limits, auth, and cadence
- [ ] Extraction retries and failures are operationally safe
- [ ] Incremental or snapshot behavior is explicit
- [ ] Source drift and raw evidence handling are considered
