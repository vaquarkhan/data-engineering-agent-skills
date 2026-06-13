# Data Engineering Agent Entry Point

Use this file as the generic entry point for agents that support `AGENTS.md`-style repository instructions.

## Start Here

1. Load `skills/using-data-engineering-agent-skills/SKILL.md`
2. Load the platform preset from `presets/` that matches the environment
3. Load only the workflow skills needed for the current task
4. Pull in references, templates, and examples only when they improve decisions or proof

## Lifecycle Commands

- `/spec` -> define contract, SLA, lineage, schema, retention, ownership
- `/plan` -> break pipeline changes into atomic tasks
- `/build` -> implement pipeline, model, or job changes incrementally
- `/validate` -> prove data quality, contract compliance, and reconciliation
- `/review` -> review reliability, cost, governance, and operability
- `/backfill` -> run safe replay and cutover workflows
- `/ship` -> deploy, observe, rollback-safe release

## Default Routing

- unclear request -> `data-specification`
- approved scope -> `pipeline-planning-and-task-breakdown`
- `Python` data pipeline implementation -> `python-data-engineering-and-pipeline-packaging`
- `Scala` Spark, Flink, or JVM data job implementation -> `scala-data-engineering-on-jvm-runtimes`
- `Java` connector, integration, or metadata service work -> `java-data-engineering-and-integration-services`
- file drops, `SFTP`, or partner-managed feeds -> `file-and-partner-feed-ingestion`
- `Glue Data Catalog` or `Lake Formation` governance -> `glue-data-catalog-and-lake-formation-governance`
- `Unity Catalog` governance -> `unity-catalog-and-lakehouse-governance`
- `Purview` or Azure governance -> `microsoft-purview-and-azure-data-governance`
- `Dataplex` or `BigQuery` governance -> `dataplex-and-bigquery-governance`
- operational store choice such as `MySQL` versus `NoSQL` -> `operational-datastore-selection-relational-and-nosql`
- warehouse/dbt work -> `warehouse-and-schema-design` + `dbt-and-analytics-engineering`
- `Snowflake` warehouse-native pipelines -> `snowflake-native-pipelines-and-governance`
- `BigQuery` or `Dataform` platform work -> `bigquery-and-dataform-platform-engineering`
- `ETL` or `ELT` transformation-boundary work -> `etl-elt-and-modernization-strategy`
- mainframe offload or modernization -> `mainframe-modernization-and-data-offload`
- streaming work -> `streaming-and-messaging-systems`
- Kafka production hardening, DLQs, or schema guardrails -> `kafka-resilience-and-schema-evolution`
- serverless Spark on Lambda or short-lived runtimes -> `spark-serverless-reliability-and-state-management`
- agent observability via MCP (lag, Spark plans, run state) -> `mcp-data-observability-integration`
- lakehouse work -> `data-lake-and-zone-architecture` + `lakehouse-table-format-engineering`
- release workflow, promotion design, or gated rollout -> `data-platform-ci-cd-and-release-management`
- test data or QA datasets -> `test-data-preparation-and-synthetic-data`
- lower-environment refreshes or masked non-prod data -> `lower-environment-data-masking-and-obfuscation`
- `Informatica`, `Talend`, or legacy ETL estates -> `enterprise-etl-and-data-integration-modernization`
- regional or country-specific data obligations -> `regional-data-compliance-and-sovereignty`
- `ESG` or sustainability reporting -> `esg-and-sustainability-regulatory-reporting`
- quality or release gates -> `data-quality-and-contract-testing`
- data-quality tool selection, rule severity, or quality operating model -> `data-quality-platforms-and-rule-management`
- resiliency testing, failure injection, or failover drills -> `data-resiliency-testing-and-failure-injection`
- disaster recovery or business continuity planning -> `data-platform-disaster-recovery-and-business-continuity`
- reliability issue -> `data-observability-and-sla-management` + `incident-triage-and-pipeline-recovery`
- platform-team ownership, golden paths, or support-boundary design -> `data-platform-operating-model-and-service-ownership`
- replay or migration work -> `safe-backfill-and-replay-orchestration` + `orchestration-and-backfills` + `data-migration-and-platform-cutover`
- regulated data and audit-bound publish paths -> `data-security-compliance-and-regulated-data` + `lineage-pii-and-governance`

## Guardrails

- prefer specification before implementation
- do not guess unclear data grain, freshness, or contract behavior
- treat quality, replay, lineage, privacy, ownership, and rollback as part of delivery
- run hooks from `hooks/` before risky operations when possible
- prefer a small set of active skills over loading the whole repository
- treat `using-data-agent-skills` as a compatibility alias only (73 workflow skills + 1 alias directory)
- distinguish runnable example scaffolds (5) from architecture blueprints (9) in `examples/README.md`

## High-Value References

- `skills-index.md`
- `registry/assets.json`
- `templates/source-contract.yaml`
- `templates/dataset-contract.yaml`
- `templates/metric-contract.yaml`
- `templates/data-compliance-controls.yaml`
- `templates/backfill-plan.yaml`
- `templates/schema-change-plan.yaml`
- `templates/release-gate-evidence.yaml`
- `templates/incident-runbook.md`
- `examples/README.md`
- `hooks/README.md`
- `references/data-testing-patterns.md`
- `references/data-resiliency-testing-patterns.md`
- `references/data-platform-dr-bcp-checklist.md`
- `references/data-platform-operating-model-checklist.md`
- `references/file-ingestion-checklist.md`
- `references/platform-native-governance-patterns.md`
- `references/mainframe-modernization-checklist.md`
- `references/data-quality-tooling-and-rule-management.md`
- `references/data-validation-and-testcase-patterns.md`
- `references/data-platform-security-checklist.md`
- `references/data-engineering-anti-patterns.md`
- `references/etl-elt-modernization-checklist.md`
- `references/progressive-data-release-patterns.md`
- `references/test-data-preparation-checklist.md`
- `references/lower-environment-masking-checklist.md`
- `references/enterprise-etl-modernization-checklist.md`
- `references/regional-compliance-and-data-sovereignty-checklist.md`
- `references/esg-and-sustainability-reporting-checklist.md`
- `references/streaming-architecture-patterns.md`
- `references/spark-serverless-reliability-patterns.md`
- `references/kafka-production-guardrails.md`
- `references/mcp-data-observability-patterns.md`
- `references/cloud-data-engineering-architecture-patterns.md`
- `references/pipeline-orchestration-patterns.md`
- `references/README.md`
- `references/orchestration-patterns.md`
