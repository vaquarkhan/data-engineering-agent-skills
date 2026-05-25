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
- `master-data-and-entity-resolution`

## Build And Model

- `api-and-saas-ingestion-patterns`
- `source-reliability-and-extraction-resilience`
- `dbt-and-analytics-engineering`
- `cdc-and-incremental-loading`
- `debezium-and-kafka-connect-cdc`
- `apache-beam-unified-batch-and-stream`
- `spark-and-distributed-processing`
- `airflow-and-workflow-orchestration`
- `streaming-and-messaging-systems`
- `lakehouse-table-format-engineering`
- `delta-lake-and-medallion-architecture`
- `apache-hudi-lakehouse`
- `duckdb-local-analytics-and-dev`
- `feature-store-and-ml-data-pipelines`
- `reverse-etl-and-operational-data-serving`

## Govern And Protect

- `lineage-pii-and-governance`
- `schema-evolution-and-contract-migrations`
- `privacy-retention-and-right-to-delete`
- `data-catalog-and-discovery`
- `openmetadata-datahub-and-openlineage`
- `avro-protobuf-json-schema-registry`
- `data-contract-testing-with-schema-registry`
- `great-expectations-deequ-and-cuallee`
- `data-reconciliation-and-financial-controls`
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
- `data-platform-ci-cd-and-release-management`
- `trino-presto-federated-query`
- `clickhouse-real-time-analytics`
- `superset-and-metrics-serving`
- `lakefs-and-data-versioning`

## Platform Presets

- `aws-data-engineering`
- `azure-data-engineering`
- `gcp-data-engineering`
- `databricks-lakehouse-engineering`
- `alibaba-cloud-data-engineering`
- `snowflake-modern-data-platform`
- `multi-cloud-hybrid-data-engineering`
- `apache-spark-engineering`
- `apache-flink-stream-processing`
- `apache-airflow-orchestration`
- `apache-kafka-streaming`
- `apache-iceberg-lakehouse`

## Common Bundles

### AWS Lakehouse

- preset: `aws-data-engineering`
- skills: `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`, `spark-and-distributed-processing`, `airflow-and-workflow-orchestration`

### API Ingestion

- preset: choose the platform stack
- skills: `api-and-saas-ingestion-patterns`, `source-reliability-and-extraction-resilience`, `cdc-and-incremental-loading`

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

### Warehouse Cutover

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`, `data-platform-ci-cd-and-release-management`

### Master Data

- preset: choose the platform stack
- skills: `master-data-and-entity-resolution`, `data-sharing-and-publishing-contracts`, `data-catalog-and-discovery`

### Open Source CDC

- preset: `apache-kafka-streaming`
- skills: `debezium-and-kafka-connect-cdc`, `avro-protobuf-json-schema-registry`, `data-contract-testing-with-schema-registry`

### Local Development

- preset: choose the platform stack
- skills: `duckdb-local-analytics-and-dev`, `warehouse-and-schema-design`, `data-quality-and-contract-testing`
