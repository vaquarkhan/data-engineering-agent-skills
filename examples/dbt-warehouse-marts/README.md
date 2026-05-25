# dbt Warehouse Marts

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

- `dbt_project.yml`
- `models/staging/stg_orders.sql`
- `models/marts/fct_daily_revenue.sql`
- `models/schema.yml`
- `seeds/orders.csv`

## Example Commands

```bash
dbt seed
dbt run
dbt test
```
