# Tutorial: Using Data Engineering Agent Skills

This tutorial explains how to use the repository in a real project from first load through implementation, validation, review, and release.

## Goal

By the end of this walkthrough, you should know how to:

- choose the correct start-here skill
- select a matching platform preset
- use the lifecycle commands correctly
- bootstrap work with starter packs, templates, and examples
- use hooks for safer data engineering workflows

## Step 1: Understand The Building Blocks

The repository is designed as an operating toolkit, not only a document library.

Main layers:

- `skills/` for workflow logic
- `presets/` for platform-specific mapping
- `references/` for checklists
- `templates/` for reusable artifacts
- `registry/` for machine-readable asset discovery
- `starter-packs/` for opinionated bundles
- `examples/` for scenario-based guidance
- `hooks/` for session-start and risk checks

Use these layers together rather than in isolation.

## Step 2: Start With The Main Entry Skill

Open:

- `skills/using-data-engineering-agent-skills/SKILL.md`

This is the default router for the repo. It helps the agent:

- identify task type
- pick the right skill
- pick the right preset
- suggest examples and templates
- choose the safest next command

If you only load one file first, load this one.

## Step 3: Pick The Closest Platform Preset

Choose one preset from `presets/` that matches the execution environment.

Examples:

- `presets/aws-data-engineering/PRESET.md`
- `presets/gcp-data-engineering/PRESET.md`
- `presets/databricks-lakehouse-engineering/PRESET.md`
- `presets/snowflake-modern-data-platform/PRESET.md`
- `presets/apache-airflow-orchestration/PRESET.md`
- `presets/apache-kafka-streaming/PRESET.md`

The preset should stay aligned with the actual stack being changed.

## Step 4: Choose The Right Lifecycle Command

The simplest mental model for this repo is the command lifecycle:

- `/spec` for defining a new or unclear data product
- `/plan` for turning an approved scope into small tasks
- `/build` for implementing changes in safe slices
- `/validate` for proving quality, contracts, and reconciliation
- `/review` for governance, reliability, operability, and cost review
- `/backfill` for replay, rerun, or cutover work
- `/ship` for publish and release readiness

Good default behavior:

- do not jump to `/build` if requirements are unclear
- do not jump to `/ship` if `/validate` evidence is missing
- do not treat replay or historical repair work as normal build work

## Step 5: Use The Smallest Useful Skill Bundle

Do not load the whole repo into the agent.

Use one small bundle based on the task.

### Example: dbt warehouse work

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `presets/snowflake-modern-data-platform/PRESET.md` or another warehouse preset
- `skills/warehouse-and-schema-design/SKILL.md`
- `skills/dbt-and-analytics-engineering/SKILL.md`

### Example: streaming work

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `presets/apache-kafka-streaming/PRESET.md`
- `skills/streaming-and-messaging-systems/SKILL.md`
- `skills/incident-triage-and-pipeline-recovery/SKILL.md`

### Example: pipeline orchestration design

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/airflow-and-workflow-orchestration/SKILL.md`
- the matching cloud preset such as `presets/aws-data-engineering/PRESET.md`
- `references/pipeline-orchestration-patterns.md`
- `templates/backfill-plan.yaml` when replay or historical repair is involved

### Example: cloud architecture design

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/data-lake-and-zone-architecture/SKILL.md`
- the matching cloud preset such as `presets/gcp-data-engineering/PRESET.md`
- `references/cloud-data-engineering-architecture-patterns.md`
- `templates/dataset-contract.yaml` for publish-bound datasets

### Example: resiliency testing

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- `skills/data-observability-and-sla-management/SKILL.md`
- `references/data-resiliency-testing-patterns.md`
- `templates/incident-runbook.md` and `templates/backfill-plan.yaml`

### Example: partner file ingestion

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/file-and-partner-feed-ingestion/SKILL.md`
- `skills/source-reliability-and-extraction-resilience/SKILL.md`
- `references/file-ingestion-checklist.md`
- `templates/source-contract.yaml`

### Example: platform-native governance

- `skills/using-data-engineering-agent-skills/SKILL.md`
- the matching governance skill such as `glue-data-catalog-and-lake-formation-governance`, `unity-catalog-and-lakehouse-governance`, `microsoft-purview-and-azure-data-governance`, or `dataplex-and-bigquery-governance`
- the matching cloud preset
- `references/platform-native-governance-patterns.md`

### Example: mainframe modernization

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/mainframe-modernization-and-data-offload/SKILL.md`
- `skills/data-migration-and-platform-cutover/SKILL.md`
- `skills/data-reconciliation-and-financial-controls/SKILL.md`
- `references/mainframe-modernization-checklist.md`

### Example: data-quality tool strategy

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/data-quality-platforms-and-rule-management/SKILL.md`
- `skills/data-quality-and-contract-testing/SKILL.md`
- `skills/great-expectations-deequ-and-cuallee/SKILL.md`
- `references/data-quality-tooling-and-rule-management.md`

### Example: disaster recovery planning

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/data-platform-disaster-recovery-and-business-continuity/SKILL.md`
- `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- `references/data-platform-dr-bcp-checklist.md`
- `templates/incident-runbook.md`

### Example: regulated data work

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/data-security-compliance-and-regulated-data/SKILL.md`
- `skills/lineage-pii-and-governance/SKILL.md`
- `skills/privacy-retention-and-right-to-delete/SKILL.md`

### Example: Python pipeline implementation

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/python-data-engineering-and-pipeline-packaging/SKILL.md`
- one execution skill such as `spark-and-distributed-processing` or `api-and-saas-ingestion-patterns`

### Example: Scala or Java JVM work

- `skills/using-data-engineering-agent-skills/SKILL.md`
- `skills/scala-data-engineering-on-jvm-runtimes/SKILL.md` or `skills/java-data-engineering-and-integration-services/SKILL.md`
- the matching runtime skill such as `spark-and-distributed-processing` or `streaming-and-messaging-systems`

## Step 6: Bootstrap With A Starter Pack Or Template

If you want a quicker start, use a starter pack:

- `starter-packs/aws-lakehouse-starter.yaml`
- `starter-packs/databricks-medallion-starter.yaml`
- `starter-packs/warehouse-analytics-starter.yaml`
- `starter-packs/streaming-reliability-starter.yaml`
- `starter-packs/privacy-governance-starter.yaml`
- `starter-packs/regulated-data-compliance-starter.yaml`
- `starter-packs/data-platform-cicd-release-starter.yaml`
- `starter-packs/resiliency-testing-starter.yaml`
- `starter-packs/validation-security-review-starter.yaml`
- `starter-packs/regional-compliance-and-esg-reporting-starter.yaml`
- `starter-packs/test-data-lower-environments-starter.yaml`
- `starter-packs/enterprise-etl-modernization-starter.yaml`

If you need more control, start from templates:

- `templates/source-contract.yaml`
- `templates/dataset-contract.yaml`
- `templates/metric-contract.yaml`
- `templates/data-compliance-controls.yaml`
- `templates/incident-runbook.md`

## Step 7: Use Examples To Remove Guesswork

The examples are useful when the agent needs concrete patterns instead of only abstract workflow steps.

Recommended examples:

- `examples/dbt-warehouse-marts/`
- `examples/aws-s3-glue-athena-iceberg/`
- `examples/databricks-delta-medallion/`
- `examples/kafka-flink-streaming/`
- `examples/privacy-retention-deletion-workflow/`

Use them when:

- the team is adopting a new stack
- you need a known-good reference shape
- you want to reduce ambiguity for the agent

## Step 8: Use Hooks For Safer Operations

Run hooks from `hooks/` when you want a pre-flight check.

Examples:

```bash
bash hooks/session-start.sh
bash hooks/contract-check-pre.sh
bash hooks/schema-change-guard.sh
bash hooks/backfill-guard.sh
bash hooks/cost-check.sh
bash hooks/release-guard.sh
```

What they help with:

- `session-start.sh` recommends the right preset and next step
- `contract-check-pre.sh` checks contract completeness
- `schema-change-guard.sh` catches risky schema changes
- `backfill-guard.sh` forces replay safety questions
- `cost-check.sh` flags likely expensive patterns
- `release-guard.sh` checks progressive-release and rollback evidence before `/ship`

## Step 9: Review And Validate Before Publish

Before shipping a change, use:

- `skills/data-quality-and-contract-testing/SKILL.md`
- `references/data-quality-checklist.md`
- `references/security-compliance-regulated-data-checklist.md` when relevant
- reviewer personas under `agents/`

Useful personas:

- `agents/analytics-engineer-reviewer.md`
- `agents/data-platform-reliability-reviewer.md`
- `agents/data-platform-infrastructure-reviewer.md`
- `agents/data-security-and-compliance-auditor.md`

## Step 10: Continue With Pattern Tutorials

If you want a guided walkthrough for one design area instead of the whole repository flow, continue with:

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

## Step 11: Choose The Right Tool Surface

Use the setup guide or tutorial that matches your editor or agent:

- `docs/cursor-setup.md`
- `docs/kiro-setup.md`
- `docs/claude-setup.md`
- `docs/copilot-setup.md`
- `docs/windsurf-setup.md`
- `docs/opencode-setup.md`
- `docs/codex-setup.md`
- `docs/jetbrains-setup.md`

If you specifically want plugin-based installation, continue to:

- `tutorials/installing-vscode-and-jetbrains-plugins.md`

## Common Mistakes

- loading too many skills at once
- skipping `/spec` for unclear work
- treating a successful run as proof of correctness
- forgetting lineage, ownership, or publish impacts
- doing backfill work without replay, rollback, and reconciliation planning

## Recommended Daily Pattern

For most projects, this is a strong default loop:

1. start with `using-data-engineering-agent-skills`
2. choose one preset
3. run `/spec` or `/plan`
4. build in small slices
5. run `/validate`
6. review with the right persona
7. run `/ship` only when publish and rollback evidence exists
