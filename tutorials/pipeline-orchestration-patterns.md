# Tutorial: Choosing Pipeline Orchestration Patterns

This tutorial explains how to choose the right orchestration pattern for data pipelines instead of defaulting to whichever scheduler is already available.

## Goal

By the end of this tutorial, you should be able to:

- choose between scheduler-driven, event-driven, lakehouse-native, and metadata-driven orchestration patterns
- map orchestration needs to `AWS`, `Azure`, `GCP`, and `Databricks`
- separate orchestration responsibilities from compute and business logic
- design retries, publish gates, and backfill controls that are operationally safe

## Step 1: Clarify What The Orchestrator Owns

The orchestrator should own:

- schedule or trigger entry
- dependency ordering
- retries, timeout, and concurrency controls
- validation gates
- backfill, rerun, and rollback coordination

The orchestrator should not own:

- hidden business logic
- transformation code that belongs in jobs or SQL
- raw secrets
- ambiguous state with no recovery model

Use `references/pipeline-orchestration-patterns.md` as the main guide.

## Step 2: Choose The Orchestration Shape

### Scheduler-Centric DAG

Choose this when:

- the workload is batch-oriented
- dependencies matter more than callbacks
- backfills and reruns are normal

Typical tools:

- `Airflow`
- `MWAA`
- `Cloud Composer`
- `Azure Data Factory` or `Synapse Pipelines` for connector-heavy flows

### Event-Driven Orchestration

Choose this when:

- workflows start from file arrival or events
- branching and compensation logic matter
- the control plane mostly coordinates services

Typical tools:

- `AWS Step Functions`
- `AWS EventBridge`
- `Azure Functions`, `Logic Apps`, `Event Grid`
- `Google Cloud Workflows`

### Lakehouse-Native Managed Pipeline

Choose this when:

- most work stays inside a lakehouse platform
- table refresh, expectations, and lineage should stay near the pipeline
- cross-platform control flow is limited

Typical tools:

- `Databricks Workflows`
- `Delta Live Tables`

### Metadata-Driven Fan-Out

Choose this when:

- one reusable orchestration template should serve many datasets or tenants
- runtime metadata should drive execution
- the team wants fewer copied DAGs and more parameterized control

## Step 3: Match The Cloud

### AWS

Use:

- `MWAA` for dependency-rich DAGs
- `Step Functions` for branching and service coordination
- `EventBridge` for arrival-triggered or operational-event-driven starts

### Azure

Use:

- `Azure Data Factory` or `Synapse Pipelines` for connector-heavy orchestration
- `Azure Databricks Workflows` when the compute stays in `Databricks`
- `Functions`, `Logic Apps`, or `Event Grid` for event-driven coordination

### GCP

Use:

- `Cloud Composer` for Airflow-style DAGs
- `Google Cloud Workflows` for API and service coordination
- `Cloud Scheduler` plus `Pub/Sub` for lightweight triggers

### Databricks

Use:

- `Databricks Workflows` when jobs, SQL tasks, and validations stay within the platform
- `Delta Live Tables` when the pipeline is primarily a managed table flow
- an external orchestrator if non-Databricks dependencies dominate

## Step 4: Keep The Control Plane Thin

Good orchestration keeps business logic outside the scheduler.

Prefer:

- packaged jobs
- callable SQL tasks
- clear handoffs to Spark, warehouse, or service code
- explicit run metadata and publish evidence

Avoid:

- giant DAGs with hidden transformations
- sensors that mask contract problems
- orchestration code that becomes the only place anyone understands the platform

## Step 5: Design Publish And Backfill Controls

Every orchestration choice should answer:

- what blocks publish?
- how are incomplete runs quarantined?
- how are backfills isolated from steady-state runs?
- how are duplicates prevented during retry or replay?

Useful supporting assets:

- `templates/backfill-plan.yaml`
- `templates/release-gate-evidence.yaml`
- `skills/orchestration-and-backfills/SKILL.md`

## Step 6: Use The Right Companion Skills

Load:

- `skills/airflow-and-workflow-orchestration/SKILL.md`
- `skills/data-quality-and-contract-testing/SKILL.md`
- `skills/orchestration-and-backfills/SKILL.md`
- `skills/incident-triage-and-pipeline-recovery/SKILL.md`

This keeps orchestration decisions tied to publish safety and recovery, not only scheduling syntax.

## Step 7: Review The Red Flags

Stop and redesign if:

- orchestration code contains the transformation logic
- the tool was chosen only because it already exists
- retry behavior is enabled without idempotency proof
- steady-state and backfill paths share the same unsafe defaults
- publish happens immediately after task success with no validation gate

## Recommended Reading

- `references/pipeline-orchestration-patterns.md`
- `references/cloud-data-engineering-architecture-patterns.md`
- `skills/airflow-and-workflow-orchestration/SKILL.md`
- `skills/orchestration-and-backfills/SKILL.md`
