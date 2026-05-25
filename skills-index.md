# Skills Index

This index groups the repository by lifecycle and platform so teams can quickly load the smallest useful subset.

## Start Here

- `using-data-agent-skills`

## Define And Plan

- `data-specification`
- `pipeline-planning-and-task-breakdown`
- `warehouse-and-schema-design`
- `data-mesh-and-domain-oriented-design`
- `data-lake-and-zone-architecture`

## Build And Model

- `dbt-and-analytics-engineering`
- `cdc-and-incremental-loading`
- `spark-and-distributed-processing`
- `airflow-and-workflow-orchestration`
- `streaming-and-messaging-systems`
- `lakehouse-table-format-engineering`
- `delta-lake-and-medallion-architecture`
- `feature-store-and-ml-data-pipelines`
- `reverse-etl-and-operational-data-serving`

## Govern And Protect

- `lineage-pii-and-governance`
- `schema-evolution-and-contract-migrations`
- `privacy-retention-and-right-to-delete`
- `data-catalog-and-discovery`
- `semantic-layer-and-metric-governance`
- `data-sharing-and-publishing-contracts`

## Operate And Recover

- `data-quality-and-contract-testing`
- `warehouse-performance-and-cost-optimization`
- `data-observability-and-sla-management`
- `incident-triage-and-pipeline-recovery`
- `orchestration-and-backfills`
- `data-migration-and-platform-cutover`

## Platform And Infrastructure

- `terraform-and-data-platform-infrastructure`

## Platform Presets

- `aws-data-engineering`
- `azure-data-engineering`
- `gcp-data-engineering`
- `databricks-lakehouse-engineering`
- `alibaba-cloud-data-engineering`
- `snowflake-modern-data-platform`
- `multi-cloud-hybrid-data-engineering`

## Common Bundles

### AWS Lakehouse

- preset: `aws-data-engineering`
- skills: `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`, `spark-and-distributed-processing`, `airflow-and-workflow-orchestration`

### Databricks Medallion

- preset: `databricks-lakehouse-engineering`
- skills: `delta-lake-and-medallion-architecture`, `dbt-and-analytics-engineering`, `data-observability-and-sla-management`

### Warehouse Analytics

- preset: `snowflake-modern-data-platform` or `gcp-data-engineering`
- skills: `warehouse-and-schema-design`, `dbt-and-analytics-engineering`, `semantic-layer-and-metric-governance`

### Streaming

- preset: choose the platform stack
- skills: `streaming-and-messaging-systems`, `orchestration-and-backfills`, `incident-triage-and-pipeline-recovery`

### Governance And Privacy

- preset: choose the platform stack
- skills: `lineage-pii-and-governance`, `privacy-retention-and-right-to-delete`, `data-catalog-and-discovery`

### ML Features

- preset: choose the platform stack
- skills: `feature-store-and-ml-data-pipelines`, `data-quality-and-contract-testing`, `data-observability-and-sla-management`
