# Plan: Snowflake dbt Reverse ETL

## Architecture

- stage and model warehouse data in `dbt`
- define shared marts and metric contracts
- sync selected outputs into the operational destination with explicit side-effect controls

## Risks

- marts can drift from shared metric definitions
- reverse ETL retries can create destination-side problems
- change management for outbound fields can be weak

## Verification

- `dbt` model and metric review
- destination contract review
- operational visibility review for sync health
