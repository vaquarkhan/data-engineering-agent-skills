![Data Engineering Agent Skills](https://raw.githubusercontent.com/vaquarkhan/data-engineering-agent-skills/main/images/DE-Skills-2.1.png)

# Data Engineering Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-70-brightgreen.svg)](#initial-skill-pack)
[![Presets](https://img.shields.io/badge/Presets-14-blue.svg)](#platform-presets)
[![Examples](https://img.shields.io/badge/Examples-13-purple.svg)](#end-to-end-examples)
[![MCP Configs](https://img.shields.io/badge/MCP%20Configs-10-orange.svg)](#mcp-config-templates)
[![Starter Packs](https://img.shields.io/badge/Starter%20Packs-12-red.svg)](#starter-packs)
[![Validate and Package](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/validate-and-package.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/validate-and-package.yml)
[![Release Artifacts](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/release-artifacts.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/release-artifacts.yml)
[![Proof Assets](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/proof-assets.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/proof-assets.yml)
[![Test Plugin Installation](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/test-plugin-installation.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/test-plugin-installation.yml)
[![Agent Benchmarks](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/agent-benchmarks.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/agent-benchmarks.yml)
[![Markdown Lint](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/markdown-lint.yml/badge.svg?branch=main)](https://github.com/vaquarkhan/data-engineering-agent-skills/actions/workflows/markdown-lint.yml)
[![GitHub Release](https://img.shields.io/github/v/release/vaquarkhan/data-engineering-agent-skills)](https://github.com/vaquarkhan/data-engineering-agent-skills/releases)

Production-grade data engineering skills for AI agents.

The open skill registry and execution toolkit for data engineering agents.

This repository packages repeatable workflows, quality gates, hooks, installer surfaces, and runnable examples so agents can build data systems with the same discipline used by strong data engineering teams.

The goal is not to give agents generic prompts. The goal is to give them operating procedures for defining, planning, implementing, validating, replaying, and shipping reliable data products.

## Agent Skills Registry Compatibility

This repository is structured to work with open `Agent Skills` registries:

- every capability lives in a directory containing a `SKILL.md`
- every `SKILL.md` starts with YAML frontmatter including at least `name` and `description`
- descriptions are written for progressive disclosure so agents can decide when to load the full skill
- supporting materials can live in `references/`, `templates/`, `examples/`, `hooks/`, and `scripts/`

Real setup paths:

```bash
git clone https://github.com/vaquarkhan/data-engineering-agent-skills.git
scripts/install.sh --tool all --target /path/to/project
```

Windows-friendly file install:

```powershell
pwsh scripts/install.ps1 --tool all --target C:\path\to\project
```

If your agent or editor supports importing a GitHub-hosted skill registry directly, use that tool's documented repository-install command against this repository URL rather than the example syntax from another project.

For Python-based proof assets and validators, install local dependencies with:

```bash
pip install -r requirements.txt
```

## Quick Start

### Start Here

1. load `skills/using-data-engineering-agent-skills/SKILL.md`
2. pick the closest platform preset from `presets/`
3. choose the safest next command from the lifecycle below
4. use one starter pack, template, or example to reduce guessing

### Install Surfaces

#### Plugin And Release Downloads

- `VS Code` family `.vsix`: [download from Releases](https://github.com/vaquarkhan/data-engineering-agent-skills/releases/latest)
- `JetBrains` plugin `.zip`: [download from Releases](https://github.com/vaquarkhan/data-engineering-agent-skills/releases/latest)
- plugin publishing and marketplace workflow setup: `docs/plugin-publishing.md`
- marketplace publish workflows exist, but this repository should be treated as GitHub Releases-first unless a marketplace listing is explicitly published
- `Claude` plugin bundle: use `.claude-plugin/`, `.claude/commands/`, and `CLAUDE.md`

#### Install By Tool

| Tool or surface | Best starting link | Install path |
| --- | --- | --- |
| `VS Code` | `vscode-extension/README.md` | download `.vsix` from Releases, then use the extension commands; do not assume a live marketplace listing |
| `Cursor` | `docs/cursor-setup.md` | use `.cursor/rules/` or `scripts/install.sh --tool cursor` |
| `Claude` | `docs/claude-setup.md` | use `.claude/commands/`, `.claude-plugin/`, `CLAUDE.md`, or `scripts/install.sh --tool claude` |
| `JetBrains` | `docs/jetbrains-setup.md` | download plugin `.zip` from Releases; marketplace publish is optional and may not be active |
| `Copilot` | `docs/copilot-setup.md` | use `.github/copilot-instructions.md` or `scripts/install.sh --tool copilot` |
| `Kiro` | `docs/kiro-setup.md` | use `.kiro/steering/` or `scripts/install.sh --tool kiro` |
| `Windsurf` | `docs/windsurf-setup.md` | use `.windsurfrules.example` or `scripts/install.sh --tool windsurf` |
| `OpenCode` | `docs/opencode-setup.md` | use `.opencode/` or `scripts/install.sh --tool opencode` |
| `Codex` | `docs/codex-setup.md` | use `AGENTS.md`, `CLAUDE.md`, `skills-index.md`, and `docs/codex-setup.md` |
| generic `AGENTS.md` consumers | `docs/getting-started.md` | use `scripts/install.sh --tool all` or copy the core files manually |

#### One-Line Script Install

```bash
scripts/install.sh --tool claude --target /path/to/project
scripts/install.sh --tool kiro --target /path/to/project
scripts/install.sh --tool windsurf --target /path/to/project
scripts/install.sh --tool opencode --target /path/to/project
scripts/install.sh --tool all --target /path/to/project
```

Windows-friendly install path:

```powershell
pwsh scripts/install.ps1 --tool all --target C:\path\to\project
```

#### Tool Setup Guides

- `docs/getting-started.md`
- `docs/cursor-setup.md`
- `docs/kiro-setup.md`
- `docs/claude-setup.md`
- `docs/copilot-setup.md`
- `docs/windsurf-setup.md`
- `docs/opencode-setup.md`
- `docs/codex-setup.md`
- `docs/jetbrains-setup.md`
- `docs/plugin-publishing.md`

#### Tutorials

- `tutorials/README.md`
- `tutorials/using-data-engineering-agent-skills.md`
- `tutorials/cloud-data-engineering-architecture-patterns.md`
- `tutorials/pipeline-orchestration-patterns.md`
- `tutorials/streaming-architecture-patterns.md`
- `tutorials/data-resiliency-testing-patterns.md`
- `tutorials/etl-elt-modernization-and-cutover.md`
- `tutorials/regulated-data-and-compliance-workflows.md`
- `tutorials/installing-vscode-and-jetbrains-plugins.md`

## Core Principles

- Spec before pipeline code
- Contract-first source and output design
- Idempotent, replayable, backfill-safe execution
- Data quality checks before publish
- Lineage, ownership, and governance by default
- Clear evidence for every change

## Feature Highlights

- Spec-first lifecycle with `/spec`, `/plan`, `/build`, `/validate`, `/review`, `/backfill`, and `/ship`
- 70 workflow skills covering ingestion, transformation, orchestration, streaming, lakehouse, warehousing, governance, quality tooling, legacy modernization, release, incident recovery, and platform operating concerns
- focused resilience testing coverage for failure drills, replay safety, restart behavior, backlog catch-up, publish protection, and disaster recovery readiness
- 14 platform presets spanning `AWS`, `Azure`, `GCP`, `Databricks`, `Snowflake`, `Alibaba Cloud`, `Informatica`, `Talend`, and Apache-first stacks
- Multi-agent packaging for `Cursor`, `Claude`, `Copilot`, `Gemini`, `Codex`, `Kiro`, `OpenCode`, `Windsurf`, `AGENTS.md`, and `CLAUDE.md` consumers
- Install surfaces for `VS Code` family editors, `JetBrains` IDEs, setup guides, one-line install scripts, and plugin release artifacts
- Plugin delivery and discovery workflows for `VS Code` and `JetBrains`, including release downloads, install smoke tests, markdown linting, and optional marketplace publish automation
- Runnable examples with contract validation, rollback demonstrations, smoke-test proof paths, and a benchmark pack that compares baseline vs with-skills concern coverage
- Structured operational templates for dataset contracts, compliance controls, backfills, schema changes, release gates, and incident response

## Feature Coverage

| Area | What is included | Good starting point |
| --- | --- | --- |
| Core delivery workflow | Spec-driven delivery, planning, validation, review, publish readiness, replay safety, and rollback-aware release flow | `skills/using-data-engineering-agent-skills/SKILL.md` |
| Cloud and platform coverage | `AWS`, `Azure`, `GCP`, `Databricks`, `Snowflake`, `Alibaba Cloud`, multi-cloud and hybrid guidance | `presets/` |
| Apache and OSS data stack | `Spark`, `Flink`, `Airflow`, `Kafka`, `Iceberg`, `Hudi`, `Beam`, `Trino`, `ClickHouse`, `DuckDB`, `LakeFS`, `OpenMetadata`, `DataHub`, `OpenLineage`, `Great Expectations`, `Deequ`, `Cuallee`, `Soda`, `Superset`, and schema-registry patterns | `skills-index.md` |
| Orchestration and streaming | Scheduler-driven, event-driven, and lakehouse-native orchestration patterns plus replay-safe streaming architecture guidance | `references/pipeline-orchestration-patterns.md`, `references/streaming-architecture-patterns.md` |
| Security, governance, and regulated data | `PII`, `PCI`, `HIPAA`, lineage, retention, deletion, privacy, audit evidence, platform security, publish controls, and cloud-native governance for `Glue Data Catalog`, `Lake Formation`, `Unity Catalog`, `Purview`, and `Dataplex` | `skills/data-security-compliance-and-regulated-data/SKILL.md`, `references/platform-native-governance-patterns.md` |
| Regional compliance and reporting | `GDPR`, sovereignty and residency patterns, `SAMA`, `Europe`, `USA`, `India`, `Saudi Arabia`, `CSRD`, `ESRS`, `BRSR`, and `ESG` reporting workflows | `references/regional-compliance-and-data-sovereignty-checklist.md`, `references/esg-and-sustainability-reporting-checklist.md` |
| Modernization and enterprise ETL | `ETL` versus `ELT`, data migration, cutover, enterprise ETL modernization, mainframe offload, and guidance for `Informatica`, `Talend`, `DataStage`, `SSIS`, `Matillion`, and mainframe-origin estates | `skills/etl-elt-and-modernization-strategy/SKILL.md`, `skills/mainframe-modernization-and-data-offload/SKILL.md` |
| Testing and lower environments | Contract testing, testcase patterns, data-quality tools, resiliency testing, failure drills, reconciliation, anti-patterns, synthetic data, masked lower environments, and validation-security review starter packs | `references/data-quality-tooling-and-rule-management.md`, `starter-packs/resiliency-testing-starter.yaml` |
| Language-specific engineering | `Python` pipeline packaging, `Scala` JVM data jobs, and `Java` integration or metadata services | `skills/python-data-engineering-and-pipeline-packaging/SKILL.md`, `skills/scala-data-engineering-on-jvm-runtimes/SKILL.md`, `skills/java-data-engineering-and-integration-services/SKILL.md` |
| Adoption and automation | `VS Code` extension, `JetBrains` plugin, `Kiro` steering, hooks, starter packs, examples, MCP templates, and machine-readable asset registry | `docs/getting-started.md`, `registry/assets.json` |

## Lifecycle Commands

These commands are the clearest way to understand the repo. They can be mapped to slash commands, prompts, hooks, or local workflows.

| What you're doing | Command | Key principle |
| --- | --- | --- |
| Define the data product | `/spec` | Contract, SLA, lineage, schema, retention, ownership |
| Plan the work | `/plan` | Small, atomic, verifiable tasks |
| Build incrementally | `/build` | Safe slices over big rewrites |
| Prove publish safety | `/validate` | Quality, contract compliance, and reconciliation are proof |
| Review the change | `/review` | Reliability, governance, cost, and operability |
| Replay or cut over safely | `/backfill` | Backfills, reruns, and cutovers need explicit guardrails |
| Ship and operate | `/ship` | Safe rollout, observability, and rollback paths |

## Choose Your Path

- New pipeline -> use `/spec`
- dbt project -> use `starter-packs/warehouse-analytics-starter.yaml`
- Streaming system -> use `starter-packs/streaming-reliability-starter.yaml`
- Streaming architecture review -> use `references/streaming-architecture-patterns.md`
- Cloud architecture review -> use `references/cloud-data-engineering-architecture-patterns.md`
- Pipeline orchestration review -> use `references/pipeline-orchestration-patterns.md`
- Validation and testcase review -> use `starter-packs/validation-security-review-starter.yaml`
- Resiliency testing -> use `starter-packs/resiliency-testing-starter.yaml`
- `Python` data pipeline work -> use `python-data-engineering-and-pipeline-packaging`
- `Scala` Spark or JVM jobs -> use `scala-data-engineering-on-jvm-runtimes`
- `Java` connectors or data services -> use `java-data-engineering-and-integration-services`
- `MySQL` versus `NoSQL` choice -> use `operational-datastore-selection-relational-and-nosql`
- Anti-pattern review -> use `references/data-engineering-anti-patterns.md`
- `ETL` or `ELT` modernization -> use `etl-elt-and-modernization-strategy`
- Partner file or `SFTP` ingestion -> use `file-and-partner-feed-ingestion`
- `Glue Data Catalog` or `Lake Formation` governance -> use `glue-data-catalog-and-lake-formation-governance`
- `Unity Catalog` governance -> use `unity-catalog-and-lakehouse-governance`
- Azure governance or `Purview` -> use `microsoft-purview-and-azure-data-governance`
- `Dataplex` or `BigQuery` governance -> use `dataplex-and-bigquery-governance`
- `Snowflake`-native pipelines -> use `snowflake-native-pipelines-and-governance`
- `BigQuery` or `Dataform` platform work -> use `bigquery-and-dataform-platform-engineering`
- Data-quality tool strategy -> use `data-quality-platforms-and-rule-management`
- Incident recovery -> use `incident-triage-and-pipeline-recovery`
- Disaster recovery planning -> use `data-platform-disaster-recovery-and-business-continuity`
- Platform operating model or golden paths -> use `data-platform-operating-model-and-service-ownership`
- Schema migration -> use `schema-evolution-and-contract-migrations`
- Cutover or backfill -> use `data-migration-and-platform-cutover`
- CI/CD and progressive release -> use `starter-packs/data-platform-cicd-release-starter.yaml`
- Regional compliance or sovereignty -> use `regional-data-compliance-and-sovereignty`
- `ESG` reporting -> use `starter-packs/regional-compliance-and-esg-reporting-starter.yaml`
- Regulated data (`PII`, `PCI`, `HIPAA`) -> use `data-security-compliance-and-regulated-data`
- Test data or synthetic fixtures -> use `test-data-preparation-and-synthetic-data`
- Lower-environment masked refresh -> use `lower-environment-data-masking-and-obfuscation`
- `Informatica` or `Talend` estate -> use `enterprise-etl-and-data-integration-modernization`
- Mainframe modernization -> use `mainframe-modernization-and-data-offload`

## Hooks

The `hooks/` directory adds a lightweight operating layer:

- `session-start.sh`
- `contract-check-pre.sh`
- `pipeline-review-pre.sh`
- `incident-mode.sh`
- `backfill-guard.sh`
- `schema-change-guard.sh`
- `cost-check.sh`
- `release-guard.sh`

Use these hooks when you want the repository to behave more like a workflow system than a static library.

## Initial Skill Pack

This repository now includes a broader production-grade skill pack:

- `using-data-engineering-agent-skills`
- `using-data-agent-skills`
- `data-specification`
- `pipeline-planning-and-task-breakdown`
- `data-quality-and-contract-testing`
- `data-resiliency-testing-and-failure-injection`
- `orchestration-and-backfills`
- `lineage-pii-and-governance`
- `data-security-compliance-and-regulated-data`
- `regional-data-compliance-and-sovereignty`
- `esg-and-sustainability-regulatory-reporting`
- `lower-environment-data-masking-and-obfuscation`
- `spark-and-distributed-processing`
- `airflow-and-workflow-orchestration`
- `streaming-and-messaging-systems`
- `file-and-partner-feed-ingestion`
- `lakehouse-table-format-engineering`
- `data-lake-and-zone-architecture`
- `warehouse-and-schema-design`
- `python-data-engineering-and-pipeline-packaging`
- `scala-data-engineering-on-jvm-runtimes`
- `java-data-engineering-and-integration-services`
- `operational-datastore-selection-relational-and-nosql`
- `data-mesh-and-domain-oriented-design`
- `delta-lake-and-medallion-architecture`
- `dbt-and-analytics-engineering`
- `cdc-and-incremental-loading`
- `schema-evolution-and-contract-migrations`
- `warehouse-performance-and-cost-optimization`
- `data-platform-disaster-recovery-and-business-continuity`
- `data-observability-and-sla-management`
- `incident-triage-and-pipeline-recovery`
- `data-platform-operating-model-and-service-ownership`
- `terraform-and-data-platform-infrastructure`
- `snowflake-native-pipelines-and-governance`
- `bigquery-and-dataform-platform-engineering`
- `semantic-layer-and-metric-governance`
- `notebook-to-production-hardening`
- `data-sharing-and-publishing-contracts`
- `data-catalog-and-discovery`
- `glue-data-catalog-and-lake-formation-governance`
- `unity-catalog-and-lakehouse-governance`
- `microsoft-purview-and-azure-data-governance`
- `dataplex-and-bigquery-governance`
- `privacy-retention-and-right-to-delete`
- `etl-elt-and-modernization-strategy`
- `mainframe-modernization-and-data-offload`
- `test-data-preparation-and-synthetic-data`
- `reverse-etl-and-operational-data-serving`
- `feature-store-and-ml-data-pipelines`
- `data-migration-and-platform-cutover`
- `api-and-saas-ingestion-patterns`
- `source-reliability-and-extraction-resilience`
- `enterprise-etl-and-data-integration-modernization`
- `data-reconciliation-and-financial-controls`
- `data-platform-ci-cd-and-release-management`
- `master-data-and-entity-resolution`
- `debezium-and-kafka-connect-cdc`
- `apache-beam-unified-batch-and-stream`
- `apache-hudi-lakehouse`
- `trino-presto-federated-query`
- `openmetadata-datahub-and-openlineage`
- `great-expectations-deequ-and-cuallee`
- `data-quality-platforms-and-rule-management`
- `lakefs-and-data-versioning`
- `clickhouse-real-time-analytics`
- `superset-and-metrics-serving`
- `avro-protobuf-json-schema-registry`
- `duckdb-local-analytics-and-dev`
- `data-contract-testing-with-schema-registry`

Future skills can extend this pack for:

- additional platform-specific delivery patterns for tools such as `EMR`, `Flink`, `Kafka`, `Kinesis`, `Iceberg`, `SSIS`, `DataStage`, and `Matillion`
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
- `informatica-data-integration`
- `talend-data-integration`
- `multi-cloud-hybrid-data-engineering`
- `apache-spark-engineering`
- `apache-flink-stream-processing`
- `apache-airflow-orchestration`
- `apache-kafka-streaming`
- `apache-iceberg-lakehouse`

## Project Structure

```text
data-engineering-agent-skills/
├── skills/           # Workflow-driven skill definitions
├── presets/          # Platform and stack-specific operating profiles
├── references/       # Reusable checklists and guidance
├── templates/        # Spec, plan, and task templates
├── registry/         # Machine-readable asset registry and indexes
├── hooks/            # Session-start and pre-flight automation hooks
├── docs/             # Setup, onboarding, and format guidance
├── vscode-extension/ # VS Code installer extension
├── jetbrains-plugin/ # JetBrains installer plugin
├── mcp/              # MCP configuration templates
├── starter-packs/    # Opinionated bundles by use case
├── agents/           # Specialist personas and review roles
├── .claude-plugin/   # Claude plugin manifests and install bundles
├── .kiro/            # Kiro steering adapter files
├── .opencode/        # OpenCode integration surface
├── CLAUDE.md         # Claude-style repository entry point
└── examples/         # Example projects and generated artifacts
```

## Setup Guides

Agent-specific setup guides are available in `docs/`:

- `docs/getting-started.md`
- `docs/cursor-setup.md`
- `docs/kiro-setup.md`
- `docs/claude-setup.md`
- `docs/copilot-setup.md`
- `docs/windsurf-setup.md`
- `docs/opencode-setup.md`
- `docs/generic-markdown-rules-setup.md`
- `docs/codex-setup.md`
- `docs/jetbrains-setup.md`

## Tutorials

Longer-form walkthroughs live in `tutorials/`:

- `tutorials/README.md`
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

## VS Code Extension

The first working `VS Code` extension scaffold lives in `vscode-extension/`.

Installable release assets are published from the repository release page as `.vsix` downloads.

Marketplace publishing is supported through `.github/workflows/publish-plugins.yml` for `VS Code Marketplace` and `Open VSX` when publish secrets are configured.

Start here for the `VS Code` family:

- `vscode-extension/README.md`
- `tutorials/installing-vscode-and-jetbrains-plugins.md`
- `docs/plugin-publishing.md`
- [latest release downloads](https://github.com/vaquarkhan/data-engineering-agent-skills/releases/latest)

It provides command-palette installers for:

- the full toolkit
- the core pack
- agent adapters
- starter packs
- MCP templates
- runnable examples

It is intended for the `VS Code` family:

- `VS Code`
- `Cursor`
- `Windsurf`
- `VSCodium`

## JetBrains Plugin

The first working JetBrains plugin scaffold lives in `jetbrains-plugin/`.

Installable plugin ZIP artifacts are published from the repository release page.

Marketplace publishing is supported through `.github/workflows/publish-plugins.yml` when JetBrains signing and marketplace secrets are configured.

Start here for `JetBrains` IDEs:

- `jetbrains-plugin/README.md`
- `docs/jetbrains-setup.md`
- `tutorials/installing-vscode-and-jetbrains-plugins.md`
- `docs/plugin-publishing.md`
- [latest release downloads](https://github.com/vaquarkhan/data-engineering-agent-skills/releases/latest)

It targets IntelliJ-platform IDEs such as:

- `IntelliJ IDEA`
- `PyCharm`
- `WebStorm`
- `DataGrip`
- `GoLand`
- `PhpStorm`

## Multi-Agent Packaging

Native adapters are included for multiple agent ecosystems:

- `.cursor/rules/`
- `.claude/commands/`
- `.claude-plugin/`
- `.gemini/commands/`
- `.kiro/steering/`
- `.github/copilot-instructions.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.opencode/`
- `.windsurfrules.example`

Direct setup links for common agent surfaces:

- `Claude` -> `docs/claude-setup.md`
- `Cursor` -> `docs/cursor-setup.md`
- `Copilot` -> `docs/copilot-setup.md`
- `Kiro` -> `docs/kiro-setup.md`
- `OpenCode` -> `docs/opencode-setup.md`
- `Windsurf` -> `docs/windsurf-setup.md`
- `Codex` -> `docs/codex-setup.md`
- generic `AGENTS.md` setup -> `docs/getting-started.md`

## Install Scripts

Installation helpers are available in `scripts/`:

- `scripts/install.sh --tool cursor|claude|copilot|gemini|kiro|windsurf|opencode|generic|all --target <path>`
- `scripts/install.ps1 --tool cursor|claude|copilot|gemini|kiro|windsurf|opencode|generic|all --target <path>`
- `scripts/install.sh --tool codex --target <path>`
- `scripts/install_toolkit.py`
- `scripts/hook_runner.py`
- `scripts/validate-skills.py`
- `scripts/validate-assets.py`
- `scripts/validate_dataset_contract.py`
- `scripts/check-links.py`
- `scripts/test-plugin-installation.py`
- `requirements.txt`
- `requirements-proof.txt`
- `scripts/sync-rules.sh`
- `scripts/sync-rules.ps1`

## Workflow Automation

Repository automation includes:

- `.github/workflows/validate-and-package.yml`
- `.github/workflows/test-plugin-installation.yml`
- `.github/workflows/proof-assets.yml`
- `.github/workflows/agent-benchmarks.yml`
- `.github/workflows/release-artifacts.yml`
- `.github/workflows/publish-plugins.yml`
- `.github/workflows/markdown-lint.yml`

## Machine-Readable Templates

Starter contract and response templates are available in `templates/`:

- `source-contract.yaml`
- `dataset-contract.yaml`
- `metric-contract.yaml`
- `data-compliance-controls.yaml`
- `backfill-plan.yaml`
- `schema-change-plan.yaml`
- `release-gate-evidence.yaml`
- `incident-runbook.md`

## Asset Registry

Machine-readable discovery lives in:

- `registry/assets.json`

Use it to index templates, starter packs, examples, MCP templates, agent adapters, and installer bundle contents without scraping the Markdown docs.

For human-readable selection of checklists and decision guides, start with:

- `references/README.md`

## MCP Config Templates

Template MCP configs are available in `mcp/` for:

- GitHub
- Postgres
- Snowflake
- BigQuery
- Databricks
- dbt Cloud
- Airflow
- Kafka
- Terraform
- Slack and Jira incident flows

Each template is a starting point only. Use `mcp/README.md` for environment-variable requirements and service-specific setup notes before connecting a live system.

## End-To-End Examples

Example project packs are available in `examples/`:

- `aws-s3-glue-athena-iceberg`
- `api-saas-to-warehouse-ingestion`
- `databricks-delta-medallion`
- `dbt-warehouse-marts`
- `gcp-pubsub-dataflow-bigquery`
- `kafka-flink-streaming`
- `snowflake-dbt-reverse-etl`
- `privacy-retention-deletion-workflow`
- `feature-store-online-offline-parity`
- `multi-cloud-warehouse-cutover`
- `data-platform-cicd-progressive-release`
- `esg-regulatory-reporting-foundation`
- `validation-and-security-review-foundation`

The first four example packs also include minimal runnable scaffolds and sample commands.

## Starter Packs

Use the starter packs in `starter-packs/` to adopt the repository by problem area:

- `aws-lakehouse-starter.yaml`
- `databricks-medallion-starter.yaml`
- `warehouse-analytics-starter.yaml`
- `streaming-reliability-starter.yaml`
- `privacy-governance-starter.yaml`
- `regulated-data-compliance-starter.yaml`
- `data-platform-cicd-release-starter.yaml`
- `validation-security-review-starter.yaml`
- `regional-compliance-and-esg-reporting-starter.yaml`
- `test-data-lower-environments-starter.yaml`
- `enterprise-etl-modernization-starter.yaml`
- `resiliency-testing-starter.yaml`

## Skills Catalog

See `skills-index.md` for a grouped catalog by lifecycle and platform.

## Agent Personas

Pre-configured specialist personas give targeted review perspectives for data engineering work:

| Agent | Role | Best for |
| --- | --- | --- |
| `data-architect` | Architecture reviewer | Platform shape, contracts, ownership, replay, and recovery design |
| `analytics-engineer-reviewer` | Analytics reviewer | `dbt`, marts, semantic consistency, and model grain |
| `data-platform-reliability-reviewer` | Reliability reviewer | SLAs, incidents, backfills, replay safety, and operational readiness |
| `data-platform-infrastructure-reviewer` | Infrastructure reviewer | Terraform, environment boundaries, secrets, and access controls |
| `data-security-and-compliance-auditor` | Security and compliance reviewer | `PII`, `PCI`, `HIPAA`, lineage, audit evidence, retention, and publish controls |

Use personas mainly for `/review`, `/validate`, and `/ship` when you want one focused lens on the current change.

## Reference Guides

Use `references/` for high-signal checklists and workflow support material.

| Reference | Covers |
| --- | --- |
| `references/README.md` | Human-readable selector for architecture, testing, compliance, ingestion, and operating-model checklists |
| `references/data-testing-patterns.md` | Contract tests, reconciliation, freshness, replay, and publish-proof patterns |
| `references/data-resiliency-testing-patterns.md` | Failure drills for restart, outage, replay, checkpoint recovery, backlog catch-up, and publish protection |
| `references/platform-native-governance-patterns.md` | Cloud-native governance choices across `Glue Data Catalog`, `Lake Formation`, `Unity Catalog`, `Purview`, and `Dataplex` |
| `references/data-platform-dr-bcp-checklist.md` | Recovery objectives, dependency inventory, failover choices, restore validation, and drill readiness |
| `references/data-platform-operating-model-checklist.md` | Service catalog, ownership, golden paths, support boundaries, and lifecycle flows for shared data platforms |
| `references/mainframe-modernization-checklist.md` | Mainframe source inventory, copybook mapping, batch-window behavior, reconciliation, coexistence, and cutover controls |
| `references/data-quality-tooling-and-rule-management.md` | Rule ownership, severity, tool boundaries, and operating-model choices for multi-tool data-quality programs |
| `references/file-ingestion-checklist.md` | Partner-feed contracts, landing, validation, duplicate handling, replay, and publish protection for file-based ingestion |
| `references/data-validation-and-testcase-patterns.md` | Concrete testcase categories for schema, nulls, duplicates, replay, security, skew, and late-data behavior |
| `references/data-platform-security-checklist.md` | Access, secrets, environment boundaries, auditability, and operational safety |
| `references/data-engineering-anti-patterns.md` | Common failure modes across validation, storage, pipelines, governance, and operations plus healthier counter-patterns |
| `references/security-compliance-regulated-data-checklist.md` | `PII`, `PCI`, `HIPAA`, lineage, retention, deletion, and release-gate evidence |
| `references/etl-elt-modernization-checklist.md` | Choosing ETL versus ELT boundaries, modernization sequencing, parity checks, and retirement of old paths |
| `references/progressive-data-release-patterns.md` | Shadow validation, canary publish, dual-run, consumer cutover, and rollback-window patterns for data releases |
| `references/test-data-preparation-checklist.md` | Safe synthetic data, masked fixtures, realism levels, and lower-environment validation coverage |
| `references/lower-environment-masking-checklist.md` | Non-production refresh boundaries, masking controls, auditability, and retained usability |
| `references/enterprise-etl-modernization-checklist.md` | Mapping discovery, parameterization, scheduler dependencies, and migration parity for `Informatica`, `Talend`, and similar ETL stacks |
| `references/regional-compliance-and-data-sovereignty-checklist.md` | Multi-country residency, transfer, jurisdiction overlays, and region-specific engineering controls including `Europe`, `USA`, `India`, and `Saudi Arabia` |
| `references/esg-and-sustainability-reporting-checklist.md` | Scope, methodology, assurance-readiness, and KPI traceability for `CSRD`, `ESRS`, `BRSR`, and similar sustainability reporting workflows |
| `references/streaming-architecture-patterns.md` | Event backbone, CDC/outbox, replay-safe sinks, DLQ, event-time, joins, savepoints, and hot-partition containment |
| `references/cloud-data-engineering-architecture-patterns.md` | Common lake, warehouse, lakehouse, streaming, and hybrid architecture patterns across `AWS`, `Azure`, `GCP`, `Databricks`, `Snowflake`, and `Alibaba Cloud` |
| `references/pipeline-orchestration-patterns.md` | Generic orchestration decisions plus `AWS`, `Azure`, `GCP`, and `Databricks` workflow patterns and best practices |
| `references/orchestration-patterns.md` | How skills, personas, commands, and hooks in this repository should compose without overlap |

## How This Toolkit Works

The repository is intentionally layered so agents do not confuse workflow, perspective, and entry point:

| Layer | What it is | Example | Job |
| --- | --- | --- | --- |
| Skill | Workflow with steps and exit criteria | `data-specification` | The process the agent should follow |
| Preset | Platform mapping and design rules | `aws-data-engineering` | The stack-specific adaptation layer |
| Persona | Specialized review perspective | `data-platform-reliability-reviewer` | The point of view applied during review |
| Command | User-facing lifecycle entry point | `/validate` | The easiest way to enter the right workflow |
| Hook | Pre-flight or session-start guardrail | `schema-change-guard.sh` | Early risk detection and routing |

Recommended composition:

```text
/spec -> /plan -> /build -> /validate -> /review -> /ship
```

Parallel review is useful only when perspectives are genuinely independent:

```text
/ship
  ├── analytics-engineer-reviewer
  ├── data-platform-reliability-reviewer
  └── data-security-and-compliance-auditor
```

## How Skills Work

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

Key design choices:

- **Workflow, not prose.** Skills are meant to guide agent behavior, not just describe concepts.
- **Verification is required.** Validation evidence, reconciliation, or rollout proof should exist before publish.
- **Progressive disclosure.** Start with one entry skill, then load the minimum useful preset, references, and examples.
- **Operational realism.** Replay, lineage, access, retention, and rollback are part of delivery, not afterthoughts.

## Why Data Engineering Agent Skills?

AI agents often default to the shortest path, which is risky in data systems. That usually means:

- skipping specification and contract definition
- treating a successful run as proof of correctness
- ignoring replay, backfill, and consumer impact
- leaving lineage, access, retention, and ownership implicit

This project is opinionated about avoiding those failure modes:

- A pipeline is not done because it runs once.
- A model is not done because the SQL compiles.
- A table is not production-ready without ownership, contracts, checks, and recovery paths.
- An agent should not guess unclear data requirements when the specification can force clarity up front.

## Release Notes

- `CHANGELOG.md`
- `docs/release-process.md`
- `docs/tag-taxonomy.md`
- `docs/walkthroughs.md`
- `docs/ide-support-matrix.md`

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

See `CONTRIBUTING.md`, `docs/skill-anatomy.md`, `docs/preset-anatomy.md`, `skills-index.md`, and `CHANGELOG.md`.

Inspired by [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
