# Spec: dbt Warehouse Marts

## Objective

Create a trusted analytics project structure that turns raw warehouse sources into tested, documented marts and reusable business metrics.

## Source Systems

- warehouse-loaded raw and staging tables from source ingestion pipelines

## Destination

- `dbt` staging, intermediate, and mart models
- documented published marts
- governed business metrics

## Quality Rules

- marts require key and relationship tests
- high-value metrics require owners and exact definitions
- consumers should not infer grain from dashboard behavior

## Success Criteria

- model layers are clear
- marts are tested and documented
- metrics have explicit ownership and definitions
