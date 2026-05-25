# Spec: Snowflake dbt Reverse ETL

## Objective

Create a `Snowflake` analytics layer with trusted marts and a safe operational sync for selected downstream attributes.

## Source Systems

- warehouse-loaded source data from upstream ingestion pipelines

## Destination

- `dbt` marts in `Snowflake`
- outbound sync into an operational SaaS destination

## Quality Rules

- marts require tests and documentation
- outbound sync must define key mapping and delete behavior
- shared metrics require owners

## Success Criteria

- marts are trusted and documented
- sync behavior is explicit and observable
- operational consumers receive governed data
