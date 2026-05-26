# Changelog

All notable changes to this repository will be documented in this file.

## Unreleased

### Added

- multi-agent packaging for `Cursor`, `Claude`, `Copilot`, and `Gemini`
- install and sync scripts
- MCP config templates for common data engineering systems
- runnable scaffolds for the flagship examples
- starter packs, release docs, walkthrough guidance, and taxonomy docs
- additional OSS and platform-specific skills and presets
- command-first lifecycle with `/validate` and `/backfill`
- `hooks/` automation layer for session start, contract checks, schema safety, cost checks, and replay guardrails
- `CLAUDE.md`, `.opencode/`, `docs/getting-started.md`, `docs/windsurf-setup.md`, and `docs/opencode-setup.md`
- GitHub workflows for validation, packaging, and release artifact automation
- community and maintenance files including issue templates, PR template, `CODEOWNERS`, `SECURITY.md`, `SUPPORT.md`, and `CODE_OF_CONDUCT.md`
- regulated-data security and compliance assets for `PII`, `PCI`, `HIPAA`, lineage, governance, and audit evidence
- new reference guides for orchestration patterns, data testing patterns, and platform security review
- skills, presets, starter packs, and references for test data preparation, lower-environment masking, and enterprise ETL modernization across `Informatica`, `Talend`, and similar stacks
- CI/CD starter and example assets, progressive data-release guidance, streaming architecture patterns, and a release guard hook for safer `/ship` workflows
- ETL versus ELT modernization guidance plus regional compliance and ESG reporting assets covering Europe, USA, India, Saudi Arabia, `SAMA`, and similar multi-jurisdiction data obligations
- validation and testcase pattern guides, anti-pattern references, `MySQL` versus `NoSQL` datastore selection guidance, and a validation-security review starter pack with example assets
- language-specific implementation skills for `Python`, `Scala`, and `Java` data engineering workflows with routing updates in the entrypoint docs and session-start hook
- machine-readable asset registry, structured backfill/schema/release templates, asset-parity validation, stronger generic install coverage, and operational example assets for release workflows
- `Amazon Kiro` support through `.kiro/steering/` adapter files, `docs/kiro-setup.md`, installer support, registry wiring, and IDE-support documentation updates
- generic and per-cloud pipeline orchestration guidance covering scheduler-centric, event-driven, and lakehouse-native control-plane patterns across `AWS`, `Azure`, `GCP`, and `Databricks`
- common cloud-specific data engineering architecture guidance covering lake, warehouse, lakehouse, streaming, and hybrid patterns across `AWS`, `Azure`, `GCP`, `Databricks`, `Snowflake`, and `Alibaba Cloud`
- resiliency testing coverage for restart drills, failure injection, failover validation, backlog catch-up, checkpoint recovery, and publish protection through a dedicated skill, reference guide, starter pack, and install-surface wiring
- pattern-based tutorials for cloud architecture, pipeline orchestration, streaming architecture, and resiliency testing so users can follow guided walkthroughs instead of only reference guides
- more detailed tutorial coverage for `ETL` or `ELT` modernization and regulated-data compliance workflows, plus a richer example catalog that maps each example to scenarios, stack patterns, and starting skills
- new high-value missing-skill coverage for partner file ingestion, disaster recovery and business continuity, platform operating models, `Snowflake`-native pipelines, and `BigQuery` plus `Dataform` execution workflows
- a human-readable `references/README.md` selector plus new ingestion and disaster-recovery tutorials and checklist references for faster adoption
- platform-native governance coverage for `Glue Data Catalog`, `Lake Formation`, `Unity Catalog`, `Microsoft Purview`, and `Dataplex` plus new governance reference and tutorial assets
- mainframe modernization and data offload guidance plus stronger data-quality tooling and rule-management coverage across `dbt`, `Great Expectations`, `Deequ`, `Cuallee`, `Soda`, and warehouse-native quality flows
- release and plugin packaging updates for the `2.0.0` line, including install smoke tests, marketplace-publish scaffolding, release badge improvements, and stronger release-asset validation
- proof assets for executable examples, including a dataset-contract validator CLI, `dbt` plus `DuckDB` local execution, replay-safe streaming harness validation, reconciliation checks, and a dedicated proof workflow
- cross-platform toolkit hardening including a full installer backend, PowerShell hook surfaces, validator compatibility checks and tests, rollback-aware `Databricks` example proof, MCP setup guidance, expanded reviewer personas, and agent benchmark scoring assets

## 2026-05-25

### Added

- initial scaffold for the data engineering agent skill registry
- production-grade skill pack for modeling, governance, quality, observability, incidents, privacy, ML features, and cutovers
- platform presets across clouds and open-source technologies
- examples, templates, personas, and references
