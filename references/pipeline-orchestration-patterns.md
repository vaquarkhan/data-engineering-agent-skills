# Pipeline Orchestration Patterns

Use this reference when designing or reviewing pipeline orchestration across schedulers, cloud-native workflow services, and lakehouse-native control planes. It focuses on workflow shape, ownership boundaries, and platform fit rather than one specific product.

## What Orchestration Owns

The orchestrator should own:

- schedule, trigger, or event-entry logic
- dependency ordering and fan-in or fan-out behavior
- parameter passing and run-scoped metadata
- retries, timeout, concurrency, and alert routing
- validation gates before publish or promotion
- backfill, rerun, recovery, and rollback coordination

The orchestrator should not own:

- hidden business logic inside DAG or pipeline definitions
- raw credentials or secrets
- table transformation details that belong in jobs, SQL, or packages
- long-lived mutable state with no replay or recovery model

## Generic Selection Model

### Scheduler-Centric DAG

Use this pattern when:

- the workload is mainly time-windowed or dependency-driven
- multiple tasks must complete in a known order
- backfills and partial reruns are normal operations

Good fits:

- `Airflow`
- `MWAA`
- `Cloud Composer`
- `Azure Data Factory` and `Synapse Pipelines` for connector-heavy and parameterized flows

Watch for:

- one giant DAG with mixed ownership domains
- every upstream dependency becoming a long-polling sensor
- business logic moving into orchestration code because task packaging is weak

### Event-Driven Orchestration

Use this pattern when:

- workflows begin from file arrival, business events, or API callbacks
- branching and compensation matter more than cron-like schedules
- the control plane coordinates services rather than running heavy compute itself

Good fits:

- `AWS Step Functions`
- `AWS EventBridge` plus queues or lightweight compute
- `Azure Functions`, `Logic Apps`, or `Event Grid`
- `Google Cloud Workflows`
- `Cloud Scheduler` plus `Pub/Sub` for simple trigger paths

Watch for:

- event-triggered systems with no durable idempotency key
- retry storms because the trigger layer cannot distinguish transient and permanent failure
- accidental coupling between control-plane events and data-plane publish behavior

### Lakehouse-Native Managed Pipeline

Use this pattern when:

- most compute and data quality behavior stays inside one lakehouse platform
- the team wants platform-managed refresh, expectations, and lineage
- the orchestration surface should stay close to the table pipeline itself

Good fits:

- `Databricks Workflows`
- `Delta Live Tables`

Watch for:

- using platform-native orchestration for cross-platform dependencies it cannot represent clearly
- hidden retries or table refresh semantics that downstream teams do not understand
- notebook-driven jobs with no packaging or release discipline

### Metadata-Driven Fan-Out

Use this pattern when:

- many similar pipelines differ by dataset, tenant, region, or source configuration
- the team needs parameterized execution instead of copied DAG files
- routing, partition windows, and control-table state drive the run

Good pattern:

- one reusable orchestration template
- one dataset or control table describing runtime parameters
- isolated state and evidence per run or entity

Watch for:

- copy-paste DAG sprawl
- one pipeline instance mutating shared state used by another
- parameter catalogs with no ownership or schema controls

## Cross-Platform Best Practices

### Thin Control Plane

Keep orchestrators thin and delegate heavy logic to callable jobs, packages, SQL models, or platform-native tasks.

Why this works:

- retries stay more predictable
- business logic is easier to test
- compute migration does not require rewriting the whole orchestrator

### Explicit Publish Gate

Do not treat task completion as publish readiness.

Gate publish on:

- data quality checks
- contract validation
- reconciliation where financial or regulatory outputs are involved
- freshness and dependency completeness

### Separate Steady-State And Backfill Paths

Backfills usually need different concurrency, validation, and rollback controls than daily production runs.

Prefer:

- separate backfill parameters or dedicated DAG entry points
- throttled historical windows
- reconciliation evidence before consumer-facing publish

### Idempotent Resume Boundary

Every workflow stage should have a clear resume point and duplicate-write strategy.

Prefer:

- durable run IDs
- write-audit or watermark tables
- merge or replace semantics that match replay behavior

### Observable Failure Semantics

Operators need to know whether a run should retry, wait, quarantine input, or escalate.

Prefer:

- distinct task states for validation failure, dependency delay, infrastructure failure, and bad input
- alert routing that maps to real ownership
- dashboards that show backlog, retries, lag, and publish delay

## Cloud Patterns

### AWS

Prefer `MWAA` when:

- the team needs dependency-rich DAGs across `Glue`, `EMR`, `Athena`, `Redshift`, and `S3`
- schedule windows, backfills, and task-level retries are first-class concerns

Prefer `Step Functions` when:

- the workflow coordinates AWS services and branching logic
- approvals, compensation, and short control-plane steps matter
- event-driven execution is more natural than a standing scheduler

Use `EventBridge` with queues or lightweight compute when:

- file arrival, change notifications, or operational events trigger work
- the flow is simple and polling would be wasteful

Keep `Glue Workflows` for:

- smaller `Glue`-centric chains where the team does not need full DAG flexibility

Best practices:

- keep dataset state and publish evidence outside transient task memory
- avoid long-running orchestration tasks that should be delegated to `Glue`, `EMR`, or containerized jobs
- design `S3`-triggered flows for idempotency because duplicate notifications happen

### Azure

Prefer `Azure Data Factory` or `Synapse Pipelines` when:

- connector-heavy ingestion, copy activity, and enterprise integration dominate
- the workflow is parameterized around datasets, environments, or landing patterns

Prefer `Azure Databricks Workflows` when:

- most compute, validation, and publish logic already lives in `Databricks`

Use `Event Grid`, `Functions`, or `Logic Apps` when:

- workflows are event-driven
- system integration and callback-driven branching matter more than batch DAG management

Best practices:

- separate control-flow pipelines from transformation code and notebooks
- use `Managed Identity` for orchestration-to-service access
- be explicit about private networking, self-hosted integration runtime, and environment-specific dependencies

### GCP

Prefer `Cloud Composer` when:

- you need `Airflow`-style DAGs, dependency-rich schedules, and backfill-aware coordination

Prefer `Google Cloud Workflows` when:

- the workflow mainly coordinates APIs, services, and branching logic
- serverless control-plane execution is more important than DAG authoring flexibility

Use `Cloud Scheduler` plus `Pub/Sub` when:

- the trigger path is lightweight and the main compute begins elsewhere

Best practices:

- keep `Composer` focused on orchestration, not embedded data processing
- align trigger design with `BigQuery`, `Dataflow`, and `Dataproc` execution boundaries
- document region, service-account, and cost implications for each orchestration path

### Databricks

Prefer `Databricks Workflows` when:

- jobs, notebooks, SQL tasks, and task dependencies mostly stay inside `Databricks`
- cluster, job, and notification policy should live with the platform workload

Prefer `Delta Live Tables` when:

- the workload is a managed table pipeline with expectations and lakehouse-native refresh behavior

Use an external orchestrator when:

- dependencies span systems outside `Databricks`
- approvals, external API coordination, or non-Databricks control flow dominate

Best practices:

- keep notebooks out of the orchestration-critical path unless they are production-hardened
- make checkpoint, retry, and table mutation semantics explicit
- document whether orchestration state lives in `Databricks` alone or also in an external scheduler

## Decision Shortcuts

```text
Is the workflow mostly time-windowed and dependency-rich?
├── Yes -> choose a scheduler-centric DAG tool
└── No -> Is it mostly event-driven or service-coordination heavy?
         ├── Yes -> choose an event-driven control-plane tool
         └── No -> Does it stay mostly inside one lakehouse platform?
                  ├── Yes -> use the platform-native workflow surface
                  └── No -> use a thin external orchestrator and keep compute in platform-specific jobs
```

## Red Flags

- orchestration code contains the main business transformation
- one workflow mixes daily schedule, backfill, replay, and cutover paths with no separate controls
- sensors or polling loops hide upstream contract problems
- publish happens after task success with no validation gate
- the orchestrator was chosen because it was already available, not because it fits the workload
- workflow ownership and alert routing are unclear across data, platform, and source teams

## Recommended Pairings In This Repo

- workflow design: `skills/airflow-and-workflow-orchestration/SKILL.md`
- replay and reruns: `skills/orchestration-and-backfills/SKILL.md`
- validation gates: `skills/data-quality-and-contract-testing/SKILL.md`
- release and promotion: `references/progressive-data-release-patterns.md`
- streaming triggers and stateful jobs: `references/streaming-architecture-patterns.md`
- cloud presets: `presets/aws-data-engineering/PRESET.md`, `presets/azure-data-engineering/PRESET.md`, `presets/gcp-data-engineering/PRESET.md`, `presets/databricks-lakehouse-engineering/PRESET.md`
