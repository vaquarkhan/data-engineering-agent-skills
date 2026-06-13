# dbt Warehouse Marts

> **Example type:** Runnable scaffold — local proof path via `make smoke-test` or README commands.

## Scenario

Build a warehouse-centric analytics project with `dbt`, layered models, governed metrics, and documented marts for analyst and dashboard consumption.

## Core Stack

- warehouse platform such as `Snowflake`, `BigQuery`, or `Redshift`
- `dbt`
- semantic or metric governance layer

## Skills To Apply

- `warehouse-and-schema-design`
- `dbt-and-analytics-engineering`
- `semantic-layer-and-metric-governance`
- `warehouse-performance-and-cost-optimization`

## Example Outcome

- clean staging models
- reusable intermediate models
- publish marts with tests and docs
- shared metric definitions with ownership

## Minimal Runnable Scaffold

Files included:

- `Makefile`
- `dbt_project.yml`
- `profiles/profiles.yml`
- `contracts/fct_daily_revenue-contract.yaml`
- `models/staging/stg_orders.sql`
- `models/marts/fct_daily_revenue.sql`
- `models/schema.yml`
- `seeds/orders.csv`

## Example Commands

```bash
python -c "from pathlib import Path; Path('build').mkdir(exist_ok=True)"
dbt seed --project-dir . --profiles-dir profiles
dbt run --project-dir . --profiles-dir profiles
dbt test --project-dir . --profiles-dir profiles
python ../../scripts/validate_dataset_contract.py --contract contracts/fct_daily_revenue-contract.yaml --duckdb build/dbt_warehouse_marts.duckdb --query "select * from fct_daily_revenue order by order_date"
```

The default profile writes to `build/dbt_warehouse_marts.duckdb` when you run the example from this directory. Set `DBT_DUCKDB_PATH` only if you want a different output location.

Or run the full local proof path:

```bash
make smoke-test
```
