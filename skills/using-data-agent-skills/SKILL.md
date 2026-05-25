---
name: using-data-agent-skills
description: Helps agents choose the right workflow for data engineering work. Use when starting a session, triaging a request, or deciding which skill should drive execution.
---

# Using Data Agent Skills

## Overview

Choose the right workflow before touching code, SQL, orchestration, or infrastructure. Most data engineering failures start with using the wrong process for the job.

## When to Use

- starting a new task
- triaging an ambiguous request
- deciding whether to specify, plan, build, test, review, or ship
- determining whether governance, quality, or backfill concerns apply

Do not use this as a replacement for the actual skill that matches the work.

## Workflow

1. Classify the request.
   - New data product or major behavior change: use `data-specification`
   - Approved scope that needs sequencing: use `pipeline-planning-and-task-breakdown`
   - Any change affecting contracts, checks, or correctness: use `data-quality-and-contract-testing`
   - Any change affecting schedules, reruns, or reprocessing: use `orchestration-and-backfills`
   - Any change affecting sensitive data, lineage, ownership, or access: use `lineage-pii-and-governance`

2. Surface assumptions before implementation.
   - source systems
   - destinations
   - freshness expectations
   - data volume
   - idempotency and replay expectations
   - security and retention constraints

3. Decide the operating mode.
   - Specify before build when intent is unclear.
   - Plan before build when work spans multiple files or systems.
   - Build only after success criteria are clear.
   - Test before publish for all behavioral changes.

4. Keep evidence as you go.
   - specification updates
   - plan and tasks
   - test or validation output
   - runbook or rollout notes where needed

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is just one pipeline tweak." | Small data changes can break downstream models, SLAs, or dashboards. Use the right skill anyway. |
| "The requirements are obvious." | Source assumptions, grain, freshness, and null handling are rarely obvious. |
| "We can add governance later." | Ownership, lineage, and access are hardest to retrofit after adoption. |

## Red Flags

- code changes begin without a defined success condition
- an agent guesses source semantics or data grain
- a rerun strategy is missing for a non-idempotent job
- a change touches sensitive data with no governance review

## Verification

- [ ] The task has been classified into the right skill workflow
- [ ] Key assumptions are written down
- [ ] Success evidence is identified before implementation begins
- [ ] Quality and governance concerns have not been skipped
