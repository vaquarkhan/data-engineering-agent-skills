---
name: incident-triage-and-pipeline-recovery
description: Guides agents through production data incidents. Use when a pipeline fails, publishes bad data, misses an SLA, partially loads, corrupts state, or requires rollback, replay, or stakeholder communication.
---

# Incident Triage And Pipeline Recovery

## Overview

Use this skill when production behavior is already wrong and the team needs controlled recovery. It helps agents contain blast radius, diagnose quickly, restore trust, and avoid making the incident worse.

## When to Use

- failed production runs
- bad or partial publishes
- corrupted incremental state
- freshness SLA breaches
- emergency rollback or replay decisions

Do not jump to fixes before stabilizing the system and understanding impact.

## Workflow

1. Contain the incident.
   Decide whether to:
   - pause schedules
   - block downstream publish
   - isolate bad partitions
   - notify owners and consumers

2. Classify impact.
   Identify:
   - affected datasets
   - time window
   - downstream consumers
   - whether data is late, missing, duplicated, or wrong

3. Determine the safest recovery path.
   Options include:
   - rerun
   - replay
   - rollback
   - partial correction
   - full backfill

4. Validate recovery before reopening publish paths.

5. Record the incident and add a guardrail.
   A fixed incident with no prevention work is unfinished.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Let us rerun everything now." | Blind reruns can duplicate data or destroy evidence. |
| "We can clean up downstream later." | Downstream trust loss is often harder to recover than the pipeline itself. |
| "The root cause can wait." | Without a guardrail, the same incident often returns quickly. |

## Red Flags

- no attempt to contain blast radius
- reruns happen before impact is understood
- downstream consumers are not informed
- recovery succeeds but no new guardrail is added

## Verification

- [ ] Impact scope and affected consumers are identified
- [ ] The chosen recovery path is safer than the alternatives
- [ ] Publish is reopened only after validation
- [ ] Post-incident guardrails or checks are added
