---
name: airflow-and-workflow-orchestration
description: Guides agents through workflow orchestration design and operation. Use when building or modifying Apache Airflow DAGs, scheduler-driven dependencies, retries, sensors, SLAs, or cross-system pipeline coordination.
---

# Airflow And Workflow Orchestration

## Overview

Use this skill when the problem is orchestration rather than transformation logic. It helps agents design `Airflow`-style workflows with explicit dependencies, retries, ownership, backfills, and publish-safe cutover behavior.

## When to Use

- building or modifying `Airflow` DAGs
- designing scheduling, sensors, task dependencies, or retry policy
- coordinating ingestion, transformation, quality checks, and publish steps
- changing backfill, catchup, or SLA behavior

Do not use this as a substitute for the underlying processing skill. Orchestration coordinates work; it does not define the compute logic itself.

## Workflow

1. Define the workflow contract.
   Capture:
   - owner
   - schedule or trigger mode
   - upstream and downstream dependencies
   - task boundaries
   - success and failure signals

2. Separate orchestration concerns from processing concerns.
   DAG tasks should call well-defined jobs, not hide business logic in orchestration code.

3. Design retries and timeouts deliberately.
   Account for:
   - idempotency
   - duplicate writes
   - sensor cost
   - late-arriving upstream data
   - alert routing

4. Make backfill behavior explicit.
   Decide how catchup, reruns, and historical windows behave before enabling them.

5. Gate publish steps on validation.
   A successful task chain is not enough if downstream tables fail quality checks.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can keep the transformation logic inside the DAG file." | That creates brittle orchestration code and harder testing and reuse. |
| "Retries are always safe." | Retries on non-idempotent tasks can duplicate data or corrupt publish layers. |
| "Catchup will handle backfills automatically." | Historical reprocessing usually needs different safeguards than normal schedule runs. |

## Red Flags

- business logic is embedded in scheduler wiring
- task ownership and alerts are undefined
- sensors poll without clear timeout or cost awareness
- publish tasks run without validation gates
- backfills rely on default catchup behavior with no review

## Verification

- [ ] DAG responsibilities are separated from compute logic
- [ ] Scheduling, retries, alerts, and dependencies are explicit
- [ ] Backfill and catchup behavior are documented
- [ ] Publish sequencing depends on validation, not just task completion
