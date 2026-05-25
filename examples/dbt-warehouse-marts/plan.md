# Plan: dbt Warehouse Marts

## Architecture

- stage raw sources into clean, typed models
- build reusable intermediate transformations
- publish marts aligned to business grain and metrics
- attach tests, docs, and metric governance to the publish layer

## Risks

- marts can hide inconsistent grain
- duplicate metric logic across models can erode trust
- warehouse cost can grow if materializations are chosen poorly

## Verification

- model layering review
- YAML tests and documentation review
- metric contract review for shared KPIs
