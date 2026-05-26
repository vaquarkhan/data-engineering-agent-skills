# AWS S3 Glue Athena Iceberg

## Scenario

Build an AWS-native lakehouse pipeline that ingests operational data into `S3`, standardizes it with `Glue`, publishes `Iceberg` tables, and serves governed analytics through `Athena`.

## Core Stack

- `S3`
- `Glue`
- `Athena`
- `Apache Iceberg`
- `Lake Formation`
- optional orchestration with `MWAA`

## Skills To Apply

- `aws-data-engineering`
- `data-lake-and-zone-architecture`
- `lakehouse-table-format-engineering`
- `spark-and-distributed-processing`
- `data-quality-and-contract-testing`
- `data-sharing-and-publishing-contracts`

## Example Outcome

- raw landing in `S3`
- conformed `Iceberg` tables in a curated zone
- governed access through `Lake Formation`
- published analytical views queryable in `Athena`

## Minimal Runnable Scaffold

Files included:

- `Makefile`
- `jobs/normalize_customers.py`
- `jobs/reconcile_customers.py`
- `contracts/customers-contract.yaml`
- `config/lake-layout.yaml`
- `sql/create_publish_view.sql`
- `data/customers.jsonl`

## Example Commands

```bash
python jobs/normalize_customers.py --input data/customers.jsonl --output build/customers.ndjson
python ../../scripts/validate_dataset_contract.py --contract contracts/customers-contract.yaml --data build/customers.ndjson --reference-time 2026-05-02T00:00:00Z
python jobs/reconcile_customers.py --source data/customers.jsonl --normalized build/customers.ndjson
make publish-sql
```

Or run the full local proof path:

```bash
make smoke-test
```
