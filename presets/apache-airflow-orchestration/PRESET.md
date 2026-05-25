---
name: apache-airflow-orchestration
description: Adapts the core skills for Apache Airflow-based orchestration. Use when Apache Airflow is the primary scheduler for DAGs, dependencies, retries, SLAs, and coordinated data pipeline execution.
---

# Apache Airflow Orchestration

## Overview

Use this preset when `Apache Airflow` is the main orchestration layer. It maps shared workflows to DAG design, task boundaries, backfills, catchup behavior, retries, sensors, and publish-safe scheduling.

## Use When

- building or modifying `Apache Airflow` DAGs
- coordinating batch, warehouse, or lakehouse workflows
- designing catchup and backfill behavior
- separating orchestration logic from execution logic

## Preferred Platform Services

- orchestration: `Apache Airflow`
- execution: external jobs, SQL tasks, Spark jobs, or API tasks
- metadata and monitoring: Airflow metadata database and runtime logs
- notifications: external alerting and incident routing

## Design Rules

- Keep DAGs focused on orchestration, not embedded business logic.
- Make retries and backfills safe for the underlying write pattern.
- Use clear task boundaries and ownership.
- Gate publish steps on validation, not only DAG completion.

## Verification

- [ ] DAG responsibilities are separated from compute logic
- [ ] Catchup, retries, and backfills are explicit
- [ ] Ownership, alerts, and failure handling are documented
- [ ] Publish safety is enforced in the workflow
