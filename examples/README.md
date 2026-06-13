# Examples

This directory contains **14 example packs** that show how skills, templates, and presets combine into delivery-ready data engineering work.

| Type | Count | Contents |
| --- | --- | --- |
| **Runnable scaffold** | 5 | Spec/plan/tasks **plus** scripts, configs, and a local proof path |
| **Architecture blueprint** | 9 | `README.md`, `spec.md`, `plan.md`, `tasks.md` only — no executable code |

Use examples when:

- the team wants a concrete starting shape instead of a blank page
- the agent needs a scenario with stack, workflow, and expected outcome already made explicit
- pattern references feel too abstract without a reference implementation path

Each example includes at minimum:

- `README.md` for the scenario and architecture
- `spec.md` for intent and delivery requirements
- `plan.md` for the implementation path
- `tasks.md` for executable work breakdown

Runnable scaffolds add scripts, sample data, contracts, and smoke-test commands.

## Example Selector

| Example | Type | Best for | Typical stack or pattern | Recommended starting skills |
| --- | --- | --- | --- | --- |
| `aws-s3-glue-athena-iceberg` | Runnable | `AWS` lakehouse adoption | `S3`, `Glue`, `Athena`, `Iceberg` | `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`, `spark-and-distributed-processing` |
| `databricks-delta-medallion` | Runnable | medallion lakehouse delivery | `Databricks`, `Delta Lake`, `Auto Loader` | `delta-lake-and-medallion-architecture`, `spark-and-distributed-processing`, `data-observability-and-sla-management` |
| `dbt-warehouse-marts` | Runnable | warehouse analytics modeling | `dbt`, warehouse marts, semantic outputs | `warehouse-and-schema-design`, `dbt-and-analytics-engineering`, `semantic-layer-and-metric-governance` |
| `kafka-flink-streaming` | Runnable | stream processing and replay safety | `Kafka`, `Flink`, schema-aware streaming | `streaming-and-messaging-systems`, `kafka-resilience-and-schema-evolution`, `safe-backfill-and-replay-orchestration`, `mcp-data-observability-integration` |
| `aws-serverless-spark-msk-reliability` | Runnable | serverless Spark checkpoints and MSK guardrails | `MSK`, `S3`, serverless Spark, gated publish | `spark-serverless-reliability-and-state-management`, `kafka-resilience-and-schema-evolution`, `safe-backfill-and-replay-orchestration`, `mcp-data-observability-integration` |
| `api-saas-to-warehouse-ingestion` | Blueprint | SaaS ingestion into analytics platforms | API extraction, staging, warehouse load | `api-and-saas-ingestion-patterns`, `source-reliability-and-extraction-resilience`, `data-quality-and-contract-testing` |
| `gcp-pubsub-dataflow-bigquery` | Blueprint | managed `GCP` stream-to-analytics path | `Pub/Sub`, `Dataflow`, `BigQuery` | `streaming-and-messaging-systems`, `data-observability-and-sla-management`, `gcp-data-engineering` |
| `snowflake-dbt-reverse-etl` | Blueprint | warehouse-to-operational serving | `Snowflake`, `dbt`, reverse ETL | `dbt-and-analytics-engineering`, `reverse-etl-and-operational-data-serving`, `data-sharing-and-publishing-contracts` |
| `privacy-retention-deletion-workflow` | Blueprint | privacy operations and deletion propagation | retention, deletion, audit evidence | `privacy-retention-and-right-to-delete`, `lineage-pii-and-governance`, `incident-triage-and-pipeline-recovery` |
| `feature-store-online-offline-parity` | Blueprint | feature consistency between training and serving | feature store, online/offline parity | `feature-store-and-ml-data-pipelines`, `data-quality-and-contract-testing`, `data-observability-and-sla-management` |
| `multi-cloud-warehouse-cutover` | Blueprint | platform migration and consumer cutover | dual run, reconciliation, rollback | `data-migration-and-platform-cutover`, `data-reconciliation-and-financial-controls`, `data-platform-ci-cd-and-release-management` |
| `data-platform-cicd-progressive-release` | Blueprint | staged platform release flow | progressive release, shadow validation, rollback | `data-platform-ci-cd-and-release-management`, `data-quality-and-contract-testing`, `data-observability-and-sla-management` |
| `esg-regulatory-reporting-foundation` | Blueprint | governed sustainability and regulatory reporting | `ESG`, evidence, regional controls | `esg-and-sustainability-regulatory-reporting`, `regional-data-compliance-and-sovereignty`, `lineage-pii-and-governance` |
| `validation-and-security-review-foundation` | Blueprint | release readiness through proof | validation, testcase inventory, security controls | `data-quality-and-contract-testing`, `data-security-compliance-and-regulated-data`, `data-reconciliation-and-financial-controls` |

## Example Groups

### Architecture And Platform Shape

- `aws-s3-glue-athena-iceberg` (runnable)
- `databricks-delta-medallion` (runnable)
- `gcp-pubsub-dataflow-bigquery` (blueprint)
- `multi-cloud-warehouse-cutover` (blueprint)

### Warehouse And Analytics Delivery

- `dbt-warehouse-marts` (runnable)
- `snowflake-dbt-reverse-etl` (blueprint)
- `feature-store-online-offline-parity` (blueprint)

### Streaming And Reliability

- `kafka-flink-streaming` (runnable)
- `aws-serverless-spark-msk-reliability` (runnable)
- `gcp-pubsub-dataflow-bigquery` (blueprint)
- `data-platform-cicd-progressive-release` (blueprint)

### Governance, Privacy, And Compliance

- `privacy-retention-deletion-workflow` (blueprint)
- `validation-and-security-review-foundation` (blueprint)
- `esg-regulatory-reporting-foundation` (blueprint)

## Runnable Example Scaffolds

Only these five examples include local proof paths with sample configs, validation commands, smoke-test targets, and at least one rollback or recovery demonstration:

- `aws-s3-glue-athena-iceberg`
- `databricks-delta-medallion`
- `dbt-warehouse-marts`
- `kafka-flink-streaming`
- `aws-serverless-spark-msk-reliability`

Use `make smoke-test` inside each runnable example directory to execute the local proof slice when a `Makefile` is present. On Windows, run the Python commands listed in each example `README.md`.

The other nine examples are **architecture blueprints** — use them for `/spec` and `/plan` workflows, not for local execution.

## How To Use An Example

1. Check the **Type** column above (runnable vs blueprint).
2. Read the example `README.md` to understand the scenario and target shape.
3. Open the `spec.md` to see the expected requirements and acceptance criteria.
4. Use the `plan.md` to understand the intended delivery sequence.
5. Treat `tasks.md` as the operational execution breakdown.
6. For runnable scaffolds, run the proof path before adapting code to your stack.
7. Pair the example with the matching preset, skill bundle, and starter pack when adapting it to your project.

Machine-readable `runnable: true|false` flags live in `registry/assets.json` under `examples`.
