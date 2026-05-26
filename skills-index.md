# Skills Index

This index groups the repository by lifecycle and platform so teams can quickly load the smallest useful subset.

## Start Here

- `using-data-engineering-agent-skills`
- `using-data-agent-skills`

## Command-First Lifecycle

- `/spec` -> `data-specification`
- `/plan` -> `pipeline-planning-and-task-breakdown`
- `/build` -> use the matching execution skill plus one preset
- `/validate` -> `data-quality-and-contract-testing`, `data-reconciliation-and-financial-controls`, `schema-evolution-and-contract-migrations`, `data-resiliency-testing-and-failure-injection`
- `/review` -> `incident-triage-and-pipeline-recovery`, `data-observability-and-sla-management`, and reviewer personas in `agents/`
- `/backfill` -> `orchestration-and-backfills`, `data-migration-and-platform-cutover`
- `/ship` -> `data-platform-ci-cd-and-release-management`, `data-sharing-and-publishing-contracts`, `data-observability-and-sla-management`

## Define And Plan

- `data-specification`
- `pipeline-planning-and-task-breakdown`
- `warehouse-and-schema-design`
- `operational-datastore-selection-relational-and-nosql`
- `data-mesh-and-domain-oriented-design`
- `data-lake-and-zone-architecture`
- `master-data-and-entity-resolution`

## Build And Model

- `api-and-saas-ingestion-patterns`
- `file-and-partner-feed-ingestion`
- `source-reliability-and-extraction-resilience`
- `python-data-engineering-and-pipeline-packaging`
- `scala-data-engineering-on-jvm-runtimes`
- `java-data-engineering-and-integration-services`
- `etl-elt-and-modernization-strategy`
- `enterprise-etl-and-data-integration-modernization`
- `mainframe-modernization-and-data-offload`
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
- `data-security-compliance-and-regulated-data`
- `regional-data-compliance-and-sovereignty`
- `esg-and-sustainability-regulatory-reporting`
- `lower-environment-data-masking-and-obfuscation`
- `schema-evolution-and-contract-migrations`
- `privacy-retention-and-right-to-delete`
- `data-catalog-and-discovery`
- `glue-data-catalog-and-lake-formation-governance`
- `unity-catalog-and-lakehouse-governance`
- `microsoft-purview-and-azure-data-governance`
- `dataplex-and-bigquery-governance`
- `openmetadata-datahub-and-openlineage`
- `avro-protobuf-json-schema-registry`
- `data-contract-testing-with-schema-registry`
- `great-expectations-deequ-and-cuallee`
- `data-reconciliation-and-financial-controls`
- `semantic-layer-and-metric-governance`
- `data-sharing-and-publishing-contracts`

## Operate And Recover

- `data-quality-and-contract-testing`
- `data-quality-platforms-and-rule-management`
- `data-resiliency-testing-and-failure-injection`
- `data-platform-disaster-recovery-and-business-continuity`
- `test-data-preparation-and-synthetic-data`
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
- `snowflake-native-pipelines-and-governance`
- `bigquery-and-dataform-platform-engineering`
- `data-platform-operating-model-and-service-ownership`

## Platform Presets

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

## Common Bundles

### AWS Lakehouse

- preset: `aws-data-engineering`
- skills: `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`, `spark-and-distributed-processing`, `airflow-and-workflow-orchestration`

### Cloud Architecture Review

- preset: `aws-data-engineering`, `azure-data-engineering`, `gcp-data-engineering`, `databricks-lakehouse-engineering`, `snowflake-modern-data-platform`, or `alibaba-cloud-data-engineering`
- skills: `data-lake-and-zone-architecture`, `warehouse-and-schema-design`, `airflow-and-workflow-orchestration`

### API Ingestion

- preset: choose the platform stack
- skills: `api-and-saas-ingestion-patterns`, `source-reliability-and-extraction-resilience`, `cdc-and-incremental-loading`

### Partner File Ingestion

- preset: choose the platform stack
- skills: `file-and-partner-feed-ingestion`, `source-reliability-and-extraction-resilience`, `data-quality-and-contract-testing`

### Python Data Pipelines

- preset: choose the platform stack
- skills: `python-data-engineering-and-pipeline-packaging`, `data-quality-and-contract-testing`, `data-platform-ci-cd-and-release-management`

### Scala JVM Data Jobs

- preset: `apache-spark-engineering` or `apache-flink-stream-processing`
- skills: `scala-data-engineering-on-jvm-runtimes`, `spark-and-distributed-processing`, `streaming-and-messaging-systems`

### Java Data Services

- preset: choose the platform stack
- skills: `java-data-engineering-and-integration-services`, `api-and-saas-ingestion-patterns`, `data-platform-ci-cd-and-release-management`

### Databricks Medallion

- preset: `databricks-lakehouse-engineering`
- skills: `delta-lake-and-medallion-architecture`, `dbt-and-analytics-engineering`, `data-observability-and-sla-management`

### Warehouse Analytics

- preset: `snowflake-modern-data-platform` or `gcp-data-engineering`
- skills: `warehouse-and-schema-design`, `dbt-and-analytics-engineering`, `semantic-layer-and-metric-governance`, `snowflake-native-pipelines-and-governance`, `bigquery-and-dataform-platform-engineering`

### Operational Store Selection

- preset: choose the platform stack
- skills: `operational-datastore-selection-relational-and-nosql`, `source-reliability-and-extraction-resilience`

### Streaming

- preset: choose the platform stack
- skills: `streaming-and-messaging-systems`, `orchestration-and-backfills`, `incident-triage-and-pipeline-recovery`

### Pipeline Orchestration

- preset: `aws-data-engineering`, `azure-data-engineering`, `gcp-data-engineering`, or `databricks-lakehouse-engineering`
- skills: `airflow-and-workflow-orchestration`, `orchestration-and-backfills`, `data-quality-and-contract-testing`

### Streaming Architecture Review

- preset: `apache-kafka-streaming` or `apache-flink-stream-processing`
- skills: `streaming-and-messaging-systems`, `data-contract-testing-with-schema-registry`, `data-observability-and-sla-management`

### Governance And Privacy

- preset: choose the platform stack
- skills: `lineage-pii-and-governance`, `privacy-retention-and-right-to-delete`, `data-catalog-and-discovery`, `glue-data-catalog-and-lake-formation-governance`, `unity-catalog-and-lakehouse-governance`, `microsoft-purview-and-azure-data-governance`, `dataplex-and-bigquery-governance`

### Regulated Data And Compliance

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-security-compliance-and-regulated-data`, `lineage-pii-and-governance`, `privacy-retention-and-right-to-delete`, `data-sharing-and-publishing-contracts`

### Test Data And Lower Environments

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `test-data-preparation-and-synthetic-data`, `lower-environment-data-masking-and-obfuscation`, `data-security-compliance-and-regulated-data`

### Enterprise ETL Modernization

- preset: `informatica-data-integration` or `talend-data-integration`
- skills: `enterprise-etl-and-data-integration-modernization`, `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`

### Mainframe Modernization

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `mainframe-modernization-and-data-offload`, `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`

### ETL And ELT Modernization

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `etl-elt-and-modernization-strategy`, `enterprise-etl-and-data-integration-modernization`, `data-migration-and-platform-cutover`

### ML Features

- preset: choose the platform stack
- skills: `feature-store-and-ml-data-pipelines`, `data-quality-and-contract-testing`, `data-observability-and-sla-management`

### Warehouse Cutover

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`, `data-platform-ci-cd-and-release-management`

### Data Platform CI CD

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-platform-ci-cd-and-release-management`, `data-quality-and-contract-testing`, `data-reconciliation-and-financial-controls`

### Platform Disaster Recovery

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-platform-disaster-recovery-and-business-continuity`, `data-resiliency-testing-and-failure-injection`, `incident-triage-and-pipeline-recovery`

### Platform Operating Model

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-platform-operating-model-and-service-ownership`, `data-platform-ci-cd-and-release-management`, `data-catalog-and-discovery`

### Resiliency Testing

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-resiliency-testing-and-failure-injection`, `data-observability-and-sla-management`, `incident-triage-and-pipeline-recovery`, `orchestration-and-backfills`

### Validation And Security Review

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `data-quality-and-contract-testing`, `data-reconciliation-and-financial-controls`, `data-security-compliance-and-regulated-data`

### Data Quality Operating Model

- preset: choose the platform stack
- skills: `data-quality-platforms-and-rule-management`, `data-quality-and-contract-testing`, `great-expectations-deequ-and-cuallee`

### Regional Compliance And Sovereignty

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `regional-data-compliance-and-sovereignty`, `data-security-compliance-and-regulated-data`, `lineage-pii-and-governance`

### ESG And Sustainability Reporting

- preset: `multi-cloud-hybrid-data-engineering`
- skills: `esg-and-sustainability-regulatory-reporting`, `regional-data-compliance-and-sovereignty`, `data-reconciliation-and-financial-controls`

### Master Data

- preset: choose the platform stack
- skills: `master-data-and-entity-resolution`, `data-sharing-and-publishing-contracts`, `data-catalog-and-discovery`

### Open Source CDC

- preset: `apache-kafka-streaming`
- skills: `debezium-and-kafka-connect-cdc`, `avro-protobuf-json-schema-registry`, `data-contract-testing-with-schema-registry`

### Local Development

- preset: choose the platform stack
- skills: `duckdb-local-analytics-and-dev`, `warehouse-and-schema-design`, `data-quality-and-contract-testing`
