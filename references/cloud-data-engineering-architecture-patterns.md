# Cloud Data Engineering Architecture Patterns

Use this reference when choosing the common architecture shape for a data platform on a specific cloud. It is meant for early platform design, modernization planning, and architecture review before implementation details lock in.

## Core Building Blocks

Most data engineering platforms need the same architectural decisions, even when the services differ:

- landing and source-ingestion boundary
- batch and streaming compute boundary
- lake, warehouse, or lakehouse storage model
- orchestration and control plane
- governance, lineage, and access boundary
- publish and serving layer
- observability, cost, and recovery model

The right architecture is usually a composition of these building blocks, not one product.

## Common Architecture Shapes

### Lake-Centric Batch Platform

Use this pattern when:

- raw files or CDC land in object storage first
- the team wants separation between landing, transformation, and publish zones
- open table formats or lakehouse interoperability matter

Typical shape:

```text
sources -> landing storage -> batch transforms -> refined tables -> publish views or marts
```

Good fit for:

- `AWS`: `S3` + `Glue` or `EMR` + `Athena` or `Redshift`
- `Azure`: `ADLS Gen2` + `Azure Databricks` or `Synapse Spark` + `Synapse SQL`
- `GCP`: `Cloud Storage` + `Dataflow` or `Dataproc` + `BigQuery`
- `Alibaba Cloud`: `OSS` + `MaxCompute` or `EMR` + `AnalyticDB`

Watch for:

- landing and publish data mixed together
- lake storage treated as a serving contract without quality or ownership guarantees
- no lifecycle or retention policy for raw zones

### Warehouse-Centric Analytics Platform

Use this pattern when:

- most transformations and serving can stay inside the warehouse
- the team wants simple operational boundaries and strong SQL-first delivery
- structured analytics workloads dominate over custom distributed processing

Typical shape:

```text
sources -> ingestion -> warehouse staging -> modeled layers -> semantic or BI serving
```

Good fit for:

- `Snowflake`
- `BigQuery`
- `Redshift`
- `Synapse Dedicated SQL`

Watch for:

- warehouse used for all raw file processing even when data volume or format is a poor fit
- no distinction between staging convenience and governed publish models
- warehouse tasks quietly becoming the only orchestration layer for a broad platform

### Lakehouse-Centric Unified Platform

Use this pattern when:

- batch and streaming share the same table semantics
- one platform should own ingestion, transforms, quality, lineage, and serving boundaries
- the team wants Spark-native scale with table-governance features

Typical shape:

```text
sources -> landing or Auto Loader -> bronze -> silver -> gold -> serving or sharing
```

Good fit for:

- `Databricks` with `Delta Lake`
- `AWS` with `S3` plus `Iceberg`
- `Azure` or `GCP` lakehouse stacks built around Spark engines and open table formats

Watch for:

- medallion layers used as ceremony without distinct contracts
- notebooks becoming the de facto production architecture
- no explicit recovery plan for checkpoints, merges, or stateful streaming updates

### Streaming-First Event Platform

Use this pattern when:

- event ingestion, low-latency processing, or replayable streams are first-class requirements
- downstream consumers depend on durable event backbones
- the platform needs explicit late-data, DLQ, and replay semantics

Typical shape:

```text
event sources -> broker or stream -> stateful or stateless processing -> analytical or operational sinks
```

Good fit for:

- `AWS`: `Kinesis` or `MSK`
- `Azure`: `Event Hubs`
- `GCP`: `Pub/Sub`
- `Alibaba Cloud`: `Realtime Compute for Apache Flink`
- `Databricks` streaming on top of cloud object storage and Delta tables

Watch for:

- batch architecture copied into streaming with no time or replay semantics
- consumer retry behavior treated as correctness
- no clear separation between canonical events and derived streams

### Hybrid Control-Plane Pattern

Use this pattern when:

- one platform owns storage and compute, but orchestration, governance, or publishing spans other systems
- the team is migrating from legacy ETL or mixed clouds
- an external scheduler or integration layer coordinates multiple execution surfaces

Typical shape:

```text
sources -> shared orchestration -> cloud-specific compute -> governed publish outputs
```

Good fit for:

- enterprise estates with `Informatica`, `Talend`, `Data Factory`, `Airflow`, or `DataWorks`
- multi-cloud migrations
- platforms with both warehouse-native and lake-native delivery paths

Watch for:

- hidden ownership gaps between scheduler, compute, and publish teams
- duplicated logic across multiple orchestration layers
- unclear source of truth for metadata, lineage, and recovery evidence

## Cloud-Specific Common Patterns

### AWS

Most common patterns:

- `S3` lake plus `Glue` or `EMR` batch processing
- `S3` + `Iceberg` + `Athena` or `Redshift` for lakehouse-style serving
- `Redshift`-centric warehouse pattern for structured analytics
- `Kinesis` or `MSK` streaming feeding warehouse or lake outputs

Typical service mapping:

- landing: `S3`
- transforms: `Glue`, `EMR`
- serving: `Athena`, `Redshift`
- orchestration: `MWAA`, `Step Functions`
- governance: `Lake Formation`, `Glue Data Catalog`

Best when:

- object storage is the durable system of record
- open table formats or lake-warehouse combinations matter
- the team can manage explicit cost and storage layout discipline

### Azure

Most common patterns:

- `ADLS Gen2` lake with `Data Factory` ingestion and `Azure Databricks` transformation
- `Synapse`-oriented platform combining pipelines, Spark, and SQL serving
- `Fabric`-leaning analytics pattern where the platform standard is already Microsoft-centric

Typical service mapping:

- landing: `ADLS Gen2`
- transforms: `Azure Databricks`, `Synapse Spark`
- serving: `Synapse Dedicated SQL`, `Azure SQL`, `Fabric`
- orchestration: `Azure Data Factory`, `Synapse Pipelines`
- governance: `Purview`

Best when:

- enterprise identity, private networking, and Microsoft integration are primary constraints
- connector-heavy ingestion and parameterized pipeline management matter

### GCP

Most common patterns:

- `Cloud Storage` plus `BigQuery` analytics platform
- `Pub/Sub` + `Dataflow` + `BigQuery` streaming and analytical pattern
- `Dataproc` or `Dataflow` feeding `BigQuery` for compute specialization

Typical service mapping:

- landing: `Cloud Storage`
- transforms: `Dataflow`, `Dataproc`, `BigQuery`
- serving: `BigQuery`
- orchestration: `Cloud Composer`, `Workflows`
- governance: `Dataplex`, policy tags, catalog metadata

Best when:

- the team wants strong serverless or managed analytics services
- `BigQuery` is the center of gravity for consumption

### Databricks

Most common patterns:

- medallion lakehouse with `Auto Loader`, `Delta Lake`, and `Databricks Workflows`
- unified batch plus streaming pipelines feeding governed Delta tables
- platform-native analytics and feature pipelines under `Unity Catalog`

Typical service mapping:

- landing: object storage plus `Auto Loader`
- transforms: Spark jobs, SQL, `Delta Live Tables`
- serving: `Delta` tables, SQL warehouses, governed sharing
- orchestration: `Databricks Workflows`
- governance: `Unity Catalog`

Best when:

- one platform should unify ingestion, transformation, quality, lineage, and governed table delivery
- Spark-native scale and lakehouse semantics are core architecture choices

### Snowflake

Most common patterns:

- warehouse-centric transformation and semantic-serving platform
- streams and tasks driven incremental model inside `Snowflake`
- external landing or CDC sources feeding staged and modeled warehouse layers

Typical service mapping:

- landing: external stages, partner ingestion, or external cloud storage
- transforms: `Snowflake` SQL, tasks, dynamic tables
- serving: secure shares, marts, semantic outputs
- orchestration: `Snowflake Tasks` or external schedulers
- governance: roles, masking, row access, tags

Best when:

- SQL-first delivery and governed data sharing matter more than custom distributed processing
- the warehouse should remain the primary execution and serving boundary

### Alibaba Cloud

Most common patterns:

- `OSS` lake with `DataWorks` orchestration and `MaxCompute` batch processing
- `Realtime Compute for Apache Flink` feeding analytical outputs in `AnalyticDB`
- mixed `EMR` and `MaxCompute` pattern for larger enterprise platforms

Typical service mapping:

- landing: `OSS`
- transforms: `MaxCompute`, `EMR`, `Realtime Compute for Apache Flink`
- serving: `AnalyticDB`
- orchestration: `DataWorks`
- governance: platform-native metadata and access controls

Best when:

- the estate is Alibaba-native and region, quota, and platform integration shape the architecture

## Selection Guide

```text
Is object storage the durable source of record?
├── Yes -> choose lake-centric or lakehouse-centric architecture
└── No -> Is the warehouse the main compute and serving boundary?
         ├── Yes -> choose warehouse-centric architecture
         └── Is low-latency streaming first-class?
              ├── Yes -> choose streaming-first architecture
              └── choose hybrid control-plane architecture
```

## Architecture Review Questions

- Where does raw data land, and who owns that boundary?
- Which platform owns transformation logic, and why is that the right compute surface?
- Which layer is allowed to publish shared data to downstream consumers?
- Where do lineage, access policy, and retention controls live?
- How are backfill, replay, and rollback coordinated across batch and stream paths?
- Which system is the control plane, and which systems only execute work?
- Which cost boundary is easiest to monitor and enforce on this cloud?

## Red Flags

- the architecture is described only as a product list with no flow boundaries
- one cloud service is expected to solve ingestion, transformation, governance, orchestration, and serving by default
- publish datasets are not distinguished from raw or intermediate layers
- cross-cloud or legacy integrations exist but ownership is not assigned
- lakehouse or medallion terminology is used without clear quality or consumer contracts

## Recommended Pairings In This Repo

- lake and zone boundaries: `skills/data-lake-and-zone-architecture/SKILL.md`
- warehouse modeling: `skills/warehouse-and-schema-design/SKILL.md`
- orchestration decisions: `references/pipeline-orchestration-patterns.md`
- cloud mapping: `presets/aws-data-engineering/PRESET.md`, `presets/azure-data-engineering/PRESET.md`, `presets/gcp-data-engineering/PRESET.md`, `presets/databricks-lakehouse-engineering/PRESET.md`, `presets/snowflake-modern-data-platform/PRESET.md`, `presets/alibaba-cloud-data-engineering/PRESET.md`
