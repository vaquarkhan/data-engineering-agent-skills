---
name: airflow-and-workflow-orchestration
description: Guides agents through workflow orchestration design and operation across Airflow-style DAGs, cloud-native schedulers, and event-driven pipeline control planes. Use when building or modifying workflow dependencies, retries, triggers, sensors, SLAs, or cross-system pipeline coordination.
---

# Airflow And Workflow Orchestration

## Overview

Use this skill when the problem is orchestration rather than transformation logic. It helps agents design `Airflow`, `MWAA`, `Cloud Composer`, `Azure Data Factory`, `Step Functions`, `Google Cloud Workflows`, or `Databricks Workflows` patterns with explicit dependencies, retries, ownership, backfills, and publish-safe cutover behavior.

## When to Use

- building or modifying `Airflow` DAGs
- choosing between scheduler-driven, event-driven, or platform-native orchestration
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

2. Choose the orchestration model before choosing the product.
   Decide whether the workload is:
   - scheduler-driven
   - event-driven
   - metadata-driven fan-out
   - platform-native inside a lakehouse

3. Separate orchestration concerns from processing concerns.
   Workflow tasks should call well-defined jobs, not hide business logic in orchestration code.

4. Design retries and timeouts deliberately.
   Account for:
   - idempotency
   - duplicate writes
   - sensor cost
   - late-arriving upstream data
   - alert routing

5. Make backfill behavior explicit.
   Decide how catchup, reruns, and historical windows behave before enabling them.

6. Gate publish steps on validation.
   A successful task chain is not enough if downstream tables fail quality checks.

## Service Selection Hints

- `AWS`: prefer `MWAA` for dependency-rich DAGs, `Step Functions` for branching and service coordination, and lightweight event triggers for arrival-based flows.
- `Azure`: prefer `Azure Data Factory` or `Synapse Pipelines` for connector-heavy and parameterized workflows, and `Databricks Workflows` when execution stays in `Databricks`.
- `GCP`: prefer `Cloud Composer` for DAGs, `Google Cloud Workflows` for API and service coordination, and `Cloud Scheduler` plus `Pub/Sub` for simple triggers.
- `Databricks`: prefer `Databricks Workflows` or `Delta Live Tables` for platform-native jobs, and use an external orchestrator when dependencies cross platform boundaries.
- Load `references/pipeline-orchestration-patterns.md` when selecting or reviewing the orchestration model, not only the syntax of one tool.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can keep the transformation logic inside the DAG file." | That creates brittle orchestration code and harder testing and reuse. |
| "Retries are always safe." | Retries on non-idempotent tasks can duplicate data or corrupt publish layers. |
| "Catchup will handle backfills automatically." | Historical reprocessing usually needs different safeguards than normal schedule runs. |
| "The platform-default orchestrator is automatically the right one." | Tool choice should follow workload shape, cross-system boundaries, and recovery needs. |

## Red Flags

- business logic is embedded in scheduler wiring
- orchestrator choice is driven by habit rather than workflow shape
- task ownership and alerts are undefined
- sensors poll without clear timeout or cost awareness
- publish tasks run without validation gates
- backfills rely on default catchup behavior with no review

## Verification

- [ ] DAG responsibilities are separated from compute logic
- [ ] Orchestrator choice matches the workflow shape and platform boundary
- [ ] Scheduling, retries, alerts, and dependencies are explicit
- [ ] Backfill and catchup behavior are documented
- [ ] Publish sequencing depends on validation, not just task completion
