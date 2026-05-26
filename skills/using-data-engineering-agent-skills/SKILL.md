---
name: using-data-engineering-agent-skills
description: Helps agents classify data engineering work, choose the right preset and skill bundle, and pick the safest next command. Use when starting a session, triaging an ambiguous request, or deciding how to proceed.
---

# Using Data Engineering Agent Skills

## Overview

Start here before changing code, SQL, orchestration, contracts, or infrastructure. This skill maps the user request to the right data engineering workflow so the agent does not skip specification, quality, governance, replay, or rollback thinking.

## When to Use

- starting a new session
- deciding which skill should lead execution
- translating a vague request into the right workflow
- choosing the best preset, starter pack, or runnable example
- deciding the safest next command

Do not stop here once the task has been classified. Load the actual execution skill after triage.

## Workflow

1. Classify the task type.
   - New data product, new pipeline, or major behavior change: use `data-specification`
   - Approved scope that needs sequencing: use `pipeline-planning-and-task-breakdown`
   - Implementation across code, SQL, or jobs: use the relevant build skill plus a matching preset
   - `Python` implementation work: use `python-data-engineering-and-pipeline-packaging`
   - `Scala` JVM data jobs: use `scala-data-engineering-on-jvm-runtimes`
   - `Java` connectors or data services: use `java-data-engineering-and-integration-services`
   - `MySQL` versus `NoSQL` or operational-store choice: use `operational-datastore-selection-relational-and-nosql`
   - `ETL`, `ELT`, or transformation-boundary redesign: use `etl-elt-and-modernization-strategy`
   - Test data generation, seeded fixtures, or lower-environment realism: use `test-data-preparation-and-synthetic-data`
   - Production-like data refresh into development, QA, or staging: use `lower-environment-data-masking-and-obfuscation`
   - Quality, reconciliation, or contract correctness: use `data-quality-and-contract-testing`
   - Resiliency testing, failure injection, restart drills, or failover validation: use `data-resiliency-testing-and-failure-injection`
   - Reliability issue, incident, or broken publish: use `incident-triage-and-pipeline-recovery`
   - Replay, rerun, cutover, or historical repair: use `orchestration-and-backfills` and `data-migration-and-platform-cutover`
   - Governance, lineage, privacy, or access changes: use `lineage-pii-and-governance`
   - `PII`, `PCI`, `HIPAA`, `PHI`, or audit-bound data handling: use `data-security-compliance-and-regulated-data`
   - region-specific compliance, sovereignty, or localization rules: use `regional-data-compliance-and-sovereignty`
   - sustainability or `ESG` reporting data products: use `esg-and-sustainability-regulatory-reporting`
   - Schema changes or breaking contracts: use `schema-evolution-and-contract-migrations`
   - `Informatica`, `Talend`, or legacy ETL modernization: use `enterprise-etl-and-data-integration-modernization`

2. Choose the execution surface.
   - Python pipeline or validation package: `python-data-engineering-and-pipeline-packaging`
   - Scala Spark or JVM stream job: `scala-data-engineering-on-jvm-runtimes`
   - Java connector or metadata service: `java-data-engineering-and-integration-services`
   - Warehouse/dbt work: `warehouse-and-schema-design` + `dbt-and-analytics-engineering`
   - Spark or distributed processing: `spark-and-distributed-processing`
   - Pipeline scheduling, DAG behavior, or event-driven orchestration: `airflow-and-workflow-orchestration`
   - Streaming or messaging: `streaming-and-messaging-systems`
   - CDC and source replication: `cdc-and-incremental-loading` or `debezium-and-kafka-connect-cdc`
   - Lakehouse table work: `lakehouse-table-format-engineering` or `delta-lake-and-medallion-architecture`
   - Infra and environment setup: `terraform-and-data-platform-infrastructure`
   - Multi-jurisdiction governance and reporting: `regional-data-compliance-and-sovereignty` or `esg-and-sustainability-regulatory-reporting`
   - Enterprise ETL estates: `enterprise-etl-and-data-integration-modernization`

3. Choose the platform preset.
   - AWS-heavy platform: `aws-data-engineering`
   - Azure-heavy platform: `azure-data-engineering`
   - GCP-heavy platform: `gcp-data-engineering`
   - Databricks-first platform: `databricks-lakehouse-engineering`
   - Snowflake-centric warehouse platform: `snowflake-modern-data-platform`
   - Informatica-centered estate: `informatica-data-integration`
   - Talend-centered estate: `talend-data-integration`
   - Mixed platform or migration state: `multi-cloud-hybrid-data-engineering`
   - Apache-first stack: load the matching Apache preset for Spark, Flink, Airflow, Kafka, or Iceberg

4. Recommend the fastest bootstrap asset.
   - New pipeline: start with `templates/source-contract.yaml` or `templates/dataset-contract.yaml`
   - Metrics or semantic work: start with `templates/metric-contract.yaml`
   - Operational recovery or release work: start with `templates/incident-runbook.md`, `templates/backfill-plan.yaml`, or `templates/release-gate-evidence.yaml`
   - Schema migration work: start with `templates/schema-change-plan.yaml`
   - Greenfield lakehouse adoption: use `starter-packs/aws-lakehouse-starter.yaml`
   - Medallion delivery: use `starter-packs/databricks-medallion-starter.yaml`
   - Warehouse modeling: use `starter-packs/warehouse-analytics-starter.yaml`
   - Streaming reliability: use `starter-packs/streaming-reliability-starter.yaml`
   - Data-platform release design: use `starter-packs/data-platform-cicd-release-starter.yaml`
   - Resilience drills and recovery proof: use `starter-packs/resiliency-testing-starter.yaml`
   - Validation and security review: use `starter-packs/validation-security-review-starter.yaml`
   - Privacy or governance work: use `starter-packs/privacy-governance-starter.yaml`
   - Regional compliance or ESG reporting: use `starter-packs/regional-compliance-and-esg-reporting-starter.yaml`
   - Test data and lower environments: use `starter-packs/test-data-lower-environments-starter.yaml`
   - Enterprise ETL modernization: use `starter-packs/enterprise-etl-modernization-starter.yaml`

5. Recommend an example project when concrete context helps.
   - Warehouse/dbt: `examples/dbt-warehouse-marts/`
   - Databricks medallion: `examples/databricks-delta-medallion/`
   - AWS lakehouse: `examples/aws-s3-glue-athena-iceberg/`
   - Kafka and Flink: `examples/kafka-flink-streaming/`
   - API or SaaS ingestion: `examples/api-saas-to-warehouse-ingestion/`
   - Privacy workflows: `examples/privacy-retention-deletion-workflow/`
   - Platform cutover: `examples/multi-cloud-warehouse-cutover/`

6. Choose the safe next command.
   - unclear intent or missing contracts: `/spec`
   - approved scope but too much ambiguity in sequencing: `/plan`
   - implementation work with clear acceptance criteria: `/build`
   - quality, reconciliation, or release gating: `/validate`
   - reliability, governance, or cost review: `/review`
   - replay, repair, or cutover work: `/backfill`
   - deployment or publish readiness: `/ship`

7. Pull in supporting references only when needed.
   - ingestion: `references/api-saas-ingestion-checklist.md`
   - quality: `references/data-quality-checklist.md`
   - security and compliance: `references/security-compliance-regulated-data-checklist.md`
   - asset discovery and install surfaces: `registry/assets.json`
   - testcase design: `references/data-validation-and-testcase-patterns.md`
   - resiliency testing: `references/data-resiliency-testing-patterns.md`
   - platform security: `references/data-platform-security-checklist.md`
   - anti-pattern review: `references/data-engineering-anti-patterns.md`
   - ETL and ELT strategy: `references/etl-elt-modernization-checklist.md`
   - progressive release: `references/progressive-data-release-patterns.md`
   - test data: `references/test-data-preparation-checklist.md`
   - lower environments: `references/lower-environment-masking-checklist.md`
   - enterprise ETL modernization: `references/enterprise-etl-modernization-checklist.md`
   - regional compliance: `references/regional-compliance-and-data-sovereignty-checklist.md`
   - ESG reporting: `references/esg-and-sustainability-reporting-checklist.md`
   - streaming architecture: `references/streaming-architecture-patterns.md`
   - cloud-specific common architecture patterns: `references/cloud-data-engineering-architecture-patterns.md`
   - pipeline orchestration across schedulers and clouds: `references/pipeline-orchestration-patterns.md`
   - streaming: `references/streaming-checklist.md`
   - recovery: `references/incident-recovery-checklist.md`
   - schema change: `references/schema-migration-checklist.md`
   - observability: `references/observability-and-sla-checklist.md`

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is only a small pipeline tweak." | Small data changes still break dashboards, contracts, or downstream jobs. Classify the work correctly first. |
| "We already know the stack." | Stack knowledge does not replace contract, replay, quality, or publish decisions. |
| "We can skip the example because the work is custom." | Examples reduce guessing and make rollout patterns safer even when the domain differs. |
| "Backfill is just rerunning the job." | Replay work can amplify bad data and downstream impact if windowing and reconciliation are unclear. |

## Red Flags

- the agent starts coding before choosing a workflow skill
- stack-specific implementation starts without a matching preset
- a replay or schema change is planned without explicit validation gates
- the agent loads the full repository instead of the smallest useful bundle
- there is no named next command for the current task

## Verification

- [ ] The task type has been mapped to the correct workflow skill
- [ ] A matching platform preset has been chosen where relevant
- [ ] A starter template, starter pack, or example has been recommended when useful
- [ ] The safest next command has been identified
- [ ] Quality, governance, replay, and rollback risks were not skipped during triage
