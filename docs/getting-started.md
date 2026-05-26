# Getting Started

This repository works with any AI agent that can consume Markdown instructions, rules files, or repository-level guidance.

## What This Repository Gives You

- workflow-driven data engineering skills
- stack presets for major clouds and Apache ecosystems
- starter packs for common adoption paths
- example projects with specs, plans, and runnable scaffolds
- hooks for session start, contract checks, schema safety, cost checks, and backfill guardrails

## 5-Minute Quick Start

1. Clone the repository.

```bash
git clone https://github.com/vaquarkhan/data-engineering-agent-skills.git
cd data-engineering-agent-skills
```

2. Start with the main entry skill:

- `skills/using-data-engineering-agent-skills/SKILL.md`

3. Pick the closest platform preset:

- `presets/aws-data-engineering/PRESET.md`
- `presets/gcp-data-engineering/PRESET.md`
- `presets/databricks-lakehouse-engineering/PRESET.md`
- `presets/snowflake-modern-data-platform/PRESET.md`
- `presets/informatica-data-integration/PRESET.md`
- `presets/talend-data-integration/PRESET.md`

4. Pick the safest next lifecycle command:

- `/spec` for a new or unclear change
- `/plan` for sequencing approved work
- `/build` for implementation
- `/validate` for quality, contract, or reconciliation proof
- `/backfill` for replay or cutover work
- `/ship` for deployment and publish readiness

5. Use one bootstrap asset:

- `starter-packs/warehouse-analytics-starter.yaml`
- `starter-packs/streaming-reliability-starter.yaml`
- `starter-packs/data-platform-cicd-release-starter.yaml`
- `starter-packs/resiliency-testing-starter.yaml`
- `starter-packs/validation-security-review-starter.yaml`
- `starter-packs/regional-compliance-and-esg-reporting-starter.yaml`
- `starter-packs/test-data-lower-environments-starter.yaml`
- `starter-packs/enterprise-etl-modernization-starter.yaml`
- `templates/dataset-contract.yaml`
- `templates/backfill-plan.yaml`
- `templates/schema-change-plan.yaml`
- `templates/release-gate-evidence.yaml`
- `examples/dbt-warehouse-marts/`
- `scripts/validate_dataset_contract.py`

## Choose Your Path

### New pipeline

- start with `/spec`
- load `data-specification`
- pick a platform preset

### dbt project

- start with `starter-packs/warehouse-analytics-starter.yaml`
- load `warehouse-and-schema-design`
- load `dbt-and-analytics-engineering`
- run `examples/dbt-warehouse-marts/Makefile` for a local proof slice

### Streaming system

- start with `starter-packs/streaming-reliability-starter.yaml`
- load `streaming-and-messaging-systems`
- load `incident-triage-and-pipeline-recovery`
- run `examples/kafka-flink-streaming/Makefile` to exercise replay-safe local validation

### Cloud architecture review

- start with `data-lake-and-zone-architecture`
- load the closest cloud preset
- use `references/cloud-data-engineering-architecture-patterns.md` to choose the platform shape

### Pipeline orchestration

- start with `airflow-and-workflow-orchestration`
- load the platform preset that owns the scheduler or control plane
- use `references/pipeline-orchestration-patterns.md` to choose the right orchestration model

### Resiliency testing

- start with `starter-packs/resiliency-testing-starter.yaml`
- load `data-resiliency-testing-and-failure-injection`
- use `references/data-resiliency-testing-patterns.md` to design the failure drills

### Partner file ingestion

- start with `file-and-partner-feed-ingestion`
- load `source-reliability-and-extraction-resilience`
- use `references/file-ingestion-checklist.md` to define landing, validation, and replay-safe publish behavior

### Platform-native governance

- start with the matching cloud governance skill such as `glue-data-catalog-and-lake-formation-governance`, `unity-catalog-and-lakehouse-governance`, `microsoft-purview-and-azure-data-governance`, or `dataplex-and-bigquery-governance`
- load the matching cloud preset
- use `references/platform-native-governance-patterns.md` to choose ownership, catalog, access, and trusted-publish boundaries

### Disaster recovery planning

- start with `data-platform-disaster-recovery-and-business-continuity`
- load `data-resiliency-testing-and-failure-injection`
- use `references/data-platform-dr-bcp-checklist.md` to define restore and failover readiness

### Snowflake-native pipelines

- start with `snowflake-native-pipelines-and-governance`
- load `presets/snowflake-modern-data-platform/PRESET.md`
- keep governance, warehouse sizing, and publish controls in scope with the pipeline design

### BigQuery and Dataform

- start with `bigquery-and-dataform-platform-engineering`
- load `presets/gcp-data-engineering/PRESET.md`
- confirm `BigQuery`, `Dataform`, and `Dataflow` or `Dataproc` boundaries early

### Mainframe modernization

- start with `mainframe-modernization-and-data-offload`
- load `data-migration-and-platform-cutover`
- use `references/mainframe-modernization-checklist.md` to define parity, coexistence, and cutover controls

### Data-quality tools and rule model

- start with `data-quality-platforms-and-rule-management`
- load `data-quality-and-contract-testing`
- use `references/data-quality-tooling-and-rule-management.md` to define tool boundaries and publish severity

### Validation and security review

- start with `starter-packs/validation-security-review-starter.yaml`
- load `data-quality-and-contract-testing`
- load `data-security-compliance-and-regulated-data`

### Python data engineering

- start with `python-data-engineering-and-pipeline-packaging`
- keep orchestration code separate from pipeline package logic
- make dependency and runtime assumptions explicit before release

### Scala JVM data jobs

- start with `scala-data-engineering-on-jvm-runtimes`
- confirm `Scala`, engine, and connector compatibility early
- validate packaging and runtime behavior beyond compile success

### Java data services

- start with `java-data-engineering-and-integration-services`
- define contract, retry, and idempotency behavior explicitly
- review resource and shutdown behavior before production rollout

### CI CD and release workflow

- start with `starter-packs/data-platform-cicd-release-starter.yaml`
- load `data-platform-ci-cd-and-release-management`
- load `data-reconciliation-and-financial-controls`

### ETL or ELT modernization

- start with `etl-elt-and-modernization-strategy`
- load `enterprise-etl-and-data-integration-modernization` if legacy tooling is involved
- load `data-migration-and-platform-cutover` when the modernization includes platform change

### MySQL versus NoSQL choice

- start with `operational-datastore-selection-relational-and-nosql`
- define access patterns and consistency needs first
- confirm CDC, backup, and analytics implications before implementation

### Schema migration

- start with `/validate`
- load `schema-evolution-and-contract-migrations`
- load `data-contract-testing-with-schema-registry` if contracts are versioned

### Backfill or cutover

- start with `/backfill`
- load `orchestration-and-backfills`
- load `data-migration-and-platform-cutover`

### Test data or lower environments

- start with `starter-packs/test-data-lower-environments-starter.yaml`
- load `test-data-preparation-and-synthetic-data`
- load `lower-environment-data-masking-and-obfuscation`

### Informatica or Talend estate

- start with `starter-packs/enterprise-etl-modernization-starter.yaml`
- load `enterprise-etl-and-data-integration-modernization`
- load `data-reconciliation-and-financial-controls`

### Regional compliance or ESG reporting

- start with `starter-packs/regional-compliance-and-esg-reporting-starter.yaml`
- load `regional-data-compliance-and-sovereignty`
- load `esg-and-sustainability-regulatory-reporting` when sustainability disclosures are in scope

## Recommended Tool Surfaces

- `docs/cursor-setup.md`
- `docs/kiro-setup.md`
- `docs/claude-setup.md`
- `docs/copilot-setup.md`
- `docs/windsurf-setup.md`
- `docs/opencode-setup.md`
- `docs/codex-setup.md`
- `docs/jetbrains-setup.md`

## Tutorials

If you want a longer guided walkthrough instead of only setup guidance, continue with:

- `tutorials/using-data-engineering-agent-skills.md`
- `tutorials/cloud-data-engineering-architecture-patterns.md`
- `tutorials/pipeline-orchestration-patterns.md`
- `tutorials/streaming-architecture-patterns.md`
- `tutorials/data-resiliency-testing-patterns.md`
- `tutorials/platform-native-governance-patterns.md`
- `tutorials/partner-feed-ingestion-and-replay-safe-file-processing.md`
- `tutorials/disaster-recovery-and-restore-drills.md`
- `tutorials/mainframe-modernization-and-cutover.md`
- `tutorials/data-quality-tools-and-rule-operating-model.md`
- `tutorials/etl-elt-modernization-and-cutover.md`
- `tutorials/regulated-data-and-compliance-workflows.md`
- `tutorials/installing-vscode-and-jetbrains-plugins.md`

## Hooks

Run hooks from `hooks/` to improve safety:

```bash
bash hooks/session-start.sh
bash hooks/contract-check-pre.sh
bash hooks/schema-change-guard.sh
bash hooks/release-guard.sh
```

## Notes

- Load the smallest useful bundle of skills.
- Prefer examples and starter packs when the agent needs concrete context.
- Use `registry/assets.json` if you need a machine-readable index of templates, starter packs, examples, MCP templates, and installer bundles.
- Treat contracts, quality, lineage, privacy, replay, and rollback as part of the default workflow.
