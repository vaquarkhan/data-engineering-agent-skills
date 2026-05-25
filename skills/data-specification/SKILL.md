---
name: data-specification
description: Creates structured specifications for data products and pipeline changes. Use when starting a new pipeline, model, ingestion flow, or any significant change with unclear requirements.
---

# Data Specification

## Overview

Write the data specification before writing pipeline code. The spec should define business intent, source and destination expectations, quality rules, and success criteria so the agent is not forced to guess.

## When to Use

- new ingestion or transformation projects
- schema or contract changes
- major changes to data products, marts, or semantic models
- requests that sound simple but leave operational details unclear

Do not use this for trivial spelling fixes or non-behavioral documentation edits.

## Workflow

1. State assumptions up front.
   Include:
   - business objective
   - source systems
   - destination systems
   - data grain
   - update cadence
   - retention expectations
   - security or privacy constraints

2. Write the specification around required sections.
   - Objective
   - Business outcomes
   - Source systems and contracts
   - Destination tables, files, or streams
   - Freshness and SLA expectations
   - Data quality rules
   - Security and access boundaries
   - Backfill and replay expectations
   - Success criteria
   - Open questions

3. Resolve ambiguity before planning.
   If the spec cannot answer frequency, grain, keys, slowly changing behavior, or null handling, pause and ask.

4. Save the spec in version control.
   A data change without a written spec becomes tribal knowledge.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We just need the table built quickly." | The wrong grain or contract creates expensive downstream rework. |
| "We can infer the business metric later." | That usually creates multiple conflicting definitions of the same metric. |
| "The destination schema is enough." | Schedules, freshness, backfills, and access rules matter just as much as columns. |

## Red Flags

- no business owner is named
- source-of-truth systems are unclear
- success is defined as "pipeline runs"
- backfill behavior is omitted
- quality rules are implied instead of written

## Verification

- [ ] The spec states the business outcome and expected users
- [ ] Source, destination, grain, cadence, and ownership are explicit
- [ ] Quality, security, and replay expectations are defined
- [ ] Open questions are listed instead of guessed
- [ ] The spec is saved in the repository
