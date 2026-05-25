# Databricks Delta Medallion

## Scenario

Build a medallion-style lakehouse on `Databricks` using `Delta Lake`, `Unity Catalog`, and workflow-driven batch plus streaming ingestion.

## Core Stack

- `Databricks`
- `Delta Lake`
- `Unity Catalog`
- `Databricks Workflows`
- optional `Delta Live Tables`

## Skills To Apply

- `databricks-lakehouse-engineering`
- `delta-lake-and-medallion-architecture`
- `lakehouse-table-format-engineering`
- `notebook-to-production-hardening`
- `data-observability-and-sla-management`

## Example Outcome

- bronze ingestion for raw survivability
- silver conformance and contract checks
- gold business-facing publish tables
- governed access and lineage in `Unity Catalog`

## Minimal Runnable Scaffold

Files included:

- `databricks.yml`
- `conf/medallion.yaml`
- `src/bronze_to_silver.py`

## Example Commands

```bash
python src/bronze_to_silver.py --input sample/bronze.jsonl --output build/silver.jsonl
```
