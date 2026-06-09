# Examples

This directory contains end-to-end example projects that show how the skills, templates, and presets can be combined into delivery-ready data engineering work.

Use examples when:

- the team wants a concrete starting shape instead of a blank page
- the agent needs a scenario with stack, workflow, and expected outcome already made explicit
- pattern references feel too abstract without a reference implementation path

Each example includes:

- `README.md` for the scenario and architecture
- `spec.md` for intent and delivery requirements
- `plan.md` for the implementation path
- `tasks.md` for executable work breakdown

## Example Selector

| Example | Best for | Typical stack or pattern | Recommended starting skills |
| --- | --- | --- | --- |
| `aws-s3-glue-athena-iceberg` | `AWS` lakehouse adoption | `S3`, `Glue`, `Athena`, `Iceberg` | `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`, `spark-and-distributed-processing` |
| `api-saas-to-warehouse-ingestion` | SaaS ingestion into analytics platforms | API extraction, staging, warehouse load | `api-and-saas-ingestion-patterns`, `source-reliability-and-extraction-resilience`, `data-quality-and-contract-testing` |
| `databricks-delta-medallion` | medallion lakehouse delivery | `Databricks`, `Delta Lake`, `Auto Loader` | `delta-lake-and-medallion-architecture`, `spark-and-distributed-processing`, `data-observability-and-sla-management` |
| `dbt-warehouse-marts` | warehouse analytics modeling | `dbt`, warehouse marts, semantic outputs | `warehouse-and-schema-design`, `dbt-and-analytics-engineering`, `semantic-layer-and-metric-governance` |
| `gcp-pubsub-dataflow-bigquery` | managed `GCP` stream-to-analytics path | `Pub/Sub`, `Dataflow`, `BigQuery` | `streaming-and-messaging-systems`, `data-observability-and-sla-management`, `gcp-data-engineering` |
| `kafka-flink-streaming` | stream processing and replay safety | `Kafka`, `Flink`, schema-aware streaming | `streaming-and-messaging-systems`, `kafka-resilience-and-schema-evolution`, `safe-backfill-and-replay-orchestration`, `mcp-data-observability-integration` |
| `aws-serverless-spark-msk-reliability` | serverless Spark checkpoints and MSK guardrails | `MSK`, `S3`, serverless Spark, gated publish | `spark-serverless-reliability-and-state-management`, `kafka-resilience-and-schema-evolution`, `safe-backfill-and-replay-orchestration`, `mcp-data-observability-integration` |
| `snowflake-dbt-reverse-etl` | warehouse-to-operational serving | `Snowflake`, `dbt`, reverse ETL | `dbt-and-analytics-engineering`, `reverse-etl-and-operational-data-serving`, `data-sharing-and-publishing-contracts` |
| `privacy-retention-deletion-workflow` | privacy operations and deletion propagation | retention, deletion, audit evidence | `privacy-retention-and-right-to-delete`, `lineage-pii-and-governance`, `incident-triage-and-pipeline-recovery` |
| `feature-store-online-offline-parity` | feature consistency between training and serving | feature store, online/offline parity | `feature-store-and-ml-data-pipelines`, `data-quality-and-contract-testing`, `data-observability-and-sla-management` |
| `multi-cloud-warehouse-cutover` | platform migration and consumer cutover | dual run, reconciliation, rollback | `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`, `data-platform-ci-cd-and-release-management` |
| `data-platform-cicd-progressive-release` | staged platform release flow | progressive release, shadow validation, rollback | `data-platform-ci-cd-and-release-management`, `data-quality-and-contract-testing`, `data-observability-and-sla-management` |
| `esg-regulatory-reporting-foundation` | governed sustainability and regulatory reporting | `ESG`, evidence, regional controls | `esg-and-sustainability-regulatory-reporting`, `regional-data-compliance-and-sovereignty`, `lineage-pii-and-governance` |
| `validation-and-security-review-foundation` | release readiness through proof | validation, testcase inventory, security controls | `data-quality-and-contract-testing`, `data-security-compliance-and-regulated-data`, `data-reconciliation-and-financial-controls` |

## Example Groups

### Architecture And Platform Shape

- `aws-s3-glue-athena-iceberg`
- `databricks-delta-medallion`
- `gcp-pubsub-dataflow-bigquery`
- `multi-cloud-warehouse-cutover`

### Warehouse And Analytics Delivery

- `dbt-warehouse-marts`
- `snowflake-dbt-reverse-etl`
- `feature-store-online-offline-parity`

### Streaming And Reliability

- `kafka-flink-streaming`
- `aws-serverless-spark-msk-reliability`
- `gcp-pubsub-dataflow-bigquery`
- `data-platform-cicd-progressive-release`

### Governance, Privacy, And Compliance

- `privacy-retention-deletion-workflow`
- `validation-and-security-review-foundation`
- `esg-regulatory-reporting-foundation`

## Runnable Example Scaffolds

The following examples include local proof paths with sample configs, validation commands, smoke-test targets, and at least one rollback or recovery demonstration:

- `aws-s3-glue-athena-iceberg`
- `databricks-delta-medallion`
- `dbt-warehouse-marts`
- `kafka-flink-streaming`
- `aws-serverless-spark-msk-reliability`

Use `make smoke-test` inside each runnable example directory to execute the local proof slice when a `Makefile` is present.

## How To Use An Example

1. Read the example `README.md` to understand the scenario and target shape.
2. Open the `spec.md` to see the expected requirements and acceptance criteria.
3. Use the `plan.md` to understand the intended delivery sequence.
4. Treat `tasks.md` as the operational execution breakdown.
5. Pair the example with the matching preset, skill bundle, and starter pack when adapting it to your project.
