# Plan: AWS S3 Glue Athena Iceberg

## Architecture

- land source extracts in a raw `S3` zone
- standardize and validate with `Glue`
- write curated `Iceberg` tables to the refined zone
- expose published views for `Athena`

## Risks

- raw files can create small-file and partition sprawl
- `Iceberg` maintenance is required for long-term health
- access must be aligned between catalog metadata and actual permissions

## Verification

- row-count reconciliation between raw and curated layers
- quality checks on published tables
- access validation for authorized and unauthorized consumers
