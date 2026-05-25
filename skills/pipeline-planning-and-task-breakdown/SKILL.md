---
name: pipeline-planning-and-task-breakdown
description: Breaks approved data specifications into safe, verifiable implementation tasks. Use when a data project spans multiple steps, systems, or files and needs dependency-aware sequencing.
---

# Pipeline Planning And Task Breakdown

## Overview

Turn a validated data specification into a sequence of small tasks that can be implemented and verified independently. A good plan protects the team from wide, risky pipeline edits.

## When to Use

- multi-step ingestion or modeling work
- changes involving orchestration, infrastructure, and transformations
- work that needs coordination across contracts, checks, and deployment

Do not use this when the task is a single isolated change with obvious verification.

## Workflow

1. Map the affected layers.
   Typical layers include:
   - source connections
   - raw landing
   - staging transformations
   - business models
   - orchestration
   - tests and checks
   - documentation and runbooks

2. Order work by dependency.
   Good sequence:
   - contracts
   - scaffolding
   - ingestion
   - transformations
   - checks
   - orchestration
   - rollout and recovery notes

3. Keep tasks small.
   Each task should:
   - have one clear outcome
   - touch a limited set of files
   - define how it will be verified
   - avoid mixing unrelated concerns

4. Call out risk points.
   Always identify:
   - schema evolution risk
   - backfill risk
   - cost or performance risk
   - downstream compatibility risk

5. Define evidence for every task.
   Examples:
   - test results
   - contract validation output
   - successful dry run
   - row count reconciliation
   - lineage or docs update

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is faster to change everything in one pass." | Wide changes increase blast radius and make rollback harder. |
| "We can skip task boundaries because the repo is small." | Data dependencies, not repo size, create risk. |
| "The orchestrator wiring can wait until the end." | Scheduling and retry behavior often shape the implementation. |

## Red Flags

- a single task spans ingestion, modeling, orchestration, and rollout
- verification says only "run the pipeline"
- rollback or compatibility concerns are not mentioned
- the plan does not separate build work from publish work

## Verification

- [ ] Tasks are ordered by dependency
- [ ] Each task has acceptance criteria and evidence
- [ ] Risks and rollback concerns are called out
- [ ] Checks and documentation are part of the plan, not afterthoughts
