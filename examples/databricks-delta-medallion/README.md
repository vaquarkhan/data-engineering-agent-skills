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

- `Makefile`
- `databricks.yml`
- `conf/medallion.yaml`
- `contracts/silver-contract.yaml`
- `contracts/silver-contract-v1.yaml`
- `src/bronze_to_silver.py`
- `src/validate_silver.py`
- `src/rollback_silver.py`
- `src/validate_rollback.py`
- `snapshots/silver_previous.jsonl`

## Example Commands

```bash
python src/bronze_to_silver.py --input sample/bronze.jsonl --output build/silver.jsonl
python ../../scripts/validate_dataset_contract.py --contract contracts/silver-contract.yaml --previous-contract contracts/silver-contract-v1.yaml --data build/silver.jsonl --reference-time 2026-05-02T00:00:00Z
python src/validate_silver.py --silver build/silver.jsonl
python src/rollback_silver.py --snapshot snapshots/silver_previous.jsonl --output build/silver.jsonl
python src/validate_rollback.py --silver build/silver.jsonl
```

Or run the full local proof path:

```bash
make smoke-test
```
