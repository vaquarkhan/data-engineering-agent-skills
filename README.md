# Data Engineering Agent Skills

Production-grade data engineering skills for AI coding agents.

This repository packages repeatable workflows, quality gates, and verification steps so agents can build data systems with the same discipline used by strong data engineering teams.

The goal is not to give agents generic prompts. The goal is to give them operating procedures for designing, planning, implementing, validating, and shipping reliable data products.

## Core Principles

- Spec before pipeline code
- Contract-first source and output design
- Idempotent, replayable, backfill-safe execution
- Data quality checks before publish
- Lineage, ownership, and governance by default
- Clear evidence for every change

## Lifecycle Commands

These commands are conceptual entry points. They can be mapped to any assistant, automation layer, or local workflow.

| What you're doing | Command | Key principle |
| --- | --- | --- |
| Define the data product | `/spec` | Intent before implementation |
| Plan the work | `/plan` | Small, verifiable tasks |
| Build incrementally | `/build` | Safe slices over big rewrites |
| Prove quality | `/test` | Contracts and checks are proof |
| Review the change | `/review` | Reliability, governance, cost |
| Simplify the system | `/simplify` | Clarity over accidental complexity |
| Ship and operate | `/ship` | Safe rollout and recovery paths |

## Initial Skill Pack

This repository now includes a broader production-grade skill pack:

- `using-data-agent-skills`
- `data-specification`
- `pipeline-planning-and-task-breakdown`
- `data-quality-and-contract-testing`
- `orchestration-and-backfills`
- `lineage-pii-and-governance`
- `spark-and-distributed-processing`
- `airflow-and-workflow-orchestration`
- `streaming-and-messaging-systems`
- `lakehouse-table-format-engineering`
- `data-lake-and-zone-architecture`
- `warehouse-and-schema-design`
- `data-mesh-and-domain-oriented-design`
- `delta-lake-and-medallion-architecture`
- `dbt-and-analytics-engineering`
- `cdc-and-incremental-loading`
- `schema-evolution-and-contract-migrations`
- `warehouse-performance-and-cost-optimization`
- `data-observability-and-sla-management`
- `incident-triage-and-pipeline-recovery`
- `terraform-and-data-platform-infrastructure`
- `semantic-layer-and-metric-governance`
- `notebook-to-production-hardening`
- `data-sharing-and-publishing-contracts`

Future skills can extend this pack for:

- source ingestion and API extraction
- feature store and ML data pipelines
- retention and deletion workflows
- migration and cutover playbooks
- platform-specific delivery patterns for tools such as `Glue`, `EMR`, `Flink`, `Kafka`, `Kinesis`, and `Iceberg`
- enterprise governance overlays and automated validation hooks

## Platform Presets

The core skills stay vendor-neutral. Platform-specific guidance lives in presets so agents can adapt the same workflow to the stack a team actually uses.

Current presets:

- `aws-data-engineering`
- `azure-data-engineering`
- `gcp-data-engineering`
- `databricks-lakehouse-engineering`
- `alibaba-cloud-data-engineering`
- `snowflake-modern-data-platform`
- `multi-cloud-hybrid-data-engineering`

## Project Structure

```text
data-engineering-agent-skills/
├── skills/         # Workflow-driven skill definitions
├── presets/        # Platform and stack-specific operating profiles
├── references/     # Reusable checklists and guidance
├── templates/      # Spec, plan, and task templates
├── docs/           # Contribution and format guidance
├── agents/         # Specialist personas and review roles
└── examples/       # Example projects and generated artifacts
```

## Skill Anatomy

Each skill lives in its own directory and has a `SKILL.md` entry point.

```text
skills/
  skill-name/
    SKILL.md
    supporting-file.md
```

Each `SKILL.md` should include:

- an overview of what the skill does
- clear signals for when to use it
- a step-by-step workflow
- common rationalizations and rebuttals
- red flags that indicate the skill is being ignored
- a verification checklist with evidence requirements

## What Makes This Different

This project is opinionated about data engineering quality:

- A pipeline is not done because it runs once.
- A model is not done because the SQL compiles.
- A table is not production-ready without ownership, contracts, checks, and recovery paths.
- An agent should not guess unclear data requirements when the specification can force clarity up front.

## Roadmap

### Phase 1

- publish the core skill pack
- add references and templates
- define contribution rules

### Phase 2

- add warehouse, transformation, ingestion, and streaming skills
- add domain presets for common stacks
- add specialist agent personas

### Phase 3

- add examples, automation hooks, and validation helpers
- add governance and enterprise preset overlays

## Contributing

Contributions should be:

- specific
- verifiable
- grounded in real data engineering practice
- compact enough for agents to follow consistently

See `CONTRIBUTING.md`, `docs/skill-anatomy.md`, and `docs/preset-anatomy.md`.
