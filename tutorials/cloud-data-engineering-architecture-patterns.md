# Tutorial: Choosing Cloud Data Engineering Architecture Patterns

This tutorial explains how to choose a common cloud architecture pattern for a data platform before implementation starts.

## Goal

By the end of this tutorial, you should be able to:

- choose between lake, warehouse, lakehouse, streaming, and hybrid platform shapes
- map the architecture shape to `AWS`, `Azure`, `GCP`, `Databricks`, `Snowflake`, or `Alibaba Cloud`
- identify the right storage, compute, orchestration, governance, and publish boundaries
- avoid common architecture mistakes that create data swamps, brittle platforms, or unclear ownership

## Step 1: Start With The Platform Shape, Not The Product List

Before choosing services, decide which overall pattern fits the workload:

- lake-centric batch platform
- warehouse-centric analytics platform
- lakehouse-centric unified platform
- streaming-first event platform
- hybrid control-plane platform

Use `references/cloud-data-engineering-architecture-patterns.md` as the main decision guide.

Do not begin by listing services the cloud already offers. Start by defining the system shape you need.

## Step 2: Identify The Architecture Drivers

Ask:

- does raw data land first in object storage?
- is the warehouse the primary transformation and serving layer?
- are batch and streaming supposed to share table semantics?
- does low-latency event processing drive the design?
- are orchestration, compute, and publishing split across multiple systems?

These questions usually narrow the architecture quickly.

## Step 3: Choose The Closest Pattern

### Lake-Centric Batch Platform

Choose this when:

- raw files or CDC land in storage first
- layered zones and retention controls matter
- open table formats or flexible compute are important

Typical fit:

- `AWS`: `S3` + `Glue` or `EMR` + `Athena` or `Redshift`
- `Azure`: `ADLS Gen2` + `Azure Databricks` or `Synapse Spark`
- `GCP`: `Cloud Storage` + `Dataflow` or `Dataproc`

### Warehouse-Centric Analytics Platform

Choose this when:

- structured analytics dominates
- SQL-first transformation is a strength
- serving and governance can stay inside the warehouse boundary

Typical fit:

- `Snowflake`
- `BigQuery`
- `Redshift`
- `Synapse Dedicated SQL`

### Lakehouse-Centric Unified Platform

Choose this when:

- batch and streaming should converge on the same governed table layer
- Spark-native scale matters
- one platform should own most transformation and serving boundaries

Typical fit:

- `Databricks`
- `S3` + `Iceberg`
- cloud lakehouse stacks with Spark and open table formats

### Streaming-First Event Platform

Choose this when:

- event backbones and replayable streams are first-class requirements
- latency matters as much as correctness
- downstream consumers depend on ordered or near-real-time data

Typical fit:

- `Kinesis` or `MSK`
- `Event Hubs`
- `Pub/Sub`
- `Realtime Compute for Apache Flink`

### Hybrid Control-Plane Platform

Choose this when:

- orchestration and governance span more than one execution surface
- the team is modernizing a mixed estate
- legacy ETL and new cloud-native systems must coexist for a while

Typical fit:

- `Informatica`, `Talend`, `Airflow`, `Data Factory`, or `DataWorks` coordinating multiple compute surfaces

## Step 4: Map The Pattern To The Cloud

Once the pattern is chosen, load the closest preset:

- `presets/aws-data-engineering/PRESET.md`
- `presets/azure-data-engineering/PRESET.md`
- `presets/gcp-data-engineering/PRESET.md`
- `presets/databricks-lakehouse-engineering/PRESET.md`
- `presets/snowflake-modern-data-platform/PRESET.md`
- `presets/alibaba-cloud-data-engineering/PRESET.md`

The preset tells you how that cloud usually realizes the chosen pattern.

## Step 5: Define The Critical Boundaries

For the architecture to stay healthy, make these boundaries explicit:

- landing versus publish
- orchestration versus compute
- governed datasets versus intermediate datasets
- streaming versus batch responsibilities
- ownership and access controls
- rollback and recovery path

If these boundaries are unclear, the architecture is not ready, even if the service list looks complete.

## Step 6: Pick The Right Companion Skills

Use these skills with the architecture reference:

- `skills/data-lake-and-zone-architecture/SKILL.md`
- `skills/warehouse-and-schema-design/SKILL.md`
- `skills/airflow-and-workflow-orchestration/SKILL.md`
- `skills/data-observability-and-sla-management/SKILL.md`

Use `skills/using-data-engineering-agent-skills/SKILL.md` first if the architecture work is still ambiguous.

## Step 7: Use A Concrete Example

Useful examples:

- `examples/aws-s3-glue-athena-iceberg/`
- `examples/databricks-delta-medallion/`
- `examples/dbt-warehouse-marts/`
- `examples/gcp-pubsub-dataflow-bigquery/`
- `examples/multi-cloud-warehouse-cutover/`

Use an example when:

- the team is moving to a new cloud pattern
- the architecture discussion is too abstract
- implementation choices are drifting without a shared reference shape

## Step 8: Review The Red Flags

Stop and re-evaluate if:

- the architecture is only a product list with no data flow
- raw, refined, and publish outputs are mixed together
- governance and access are deferred to "later"
- one tool is expected to solve ingestion, transforms, orchestration, serving, and governance by default
- hybrid or migration responsibilities exist but no owner is assigned

## Recommended Reading

- `references/cloud-data-engineering-architecture-patterns.md`
- `references/pipeline-orchestration-patterns.md`
- `skills/data-lake-and-zone-architecture/SKILL.md`
- `skills/warehouse-and-schema-design/SKILL.md`
