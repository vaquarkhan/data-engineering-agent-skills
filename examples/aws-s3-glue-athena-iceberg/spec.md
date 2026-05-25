# Spec: AWS S3 Glue Athena Iceberg

## Objective

Create a governed AWS lakehouse pattern for ingesting operational data and publishing trusted analytical tables on `Athena`.

## Source Systems

- transactional API extracts delivered hourly
- daily dimension snapshots from an internal ERP export

## Destination

- raw files in `S3`
- curated `Iceberg` tables registered in the Glue catalog
- published analytical tables queryable in `Athena`

## Quality Rules

- primary entity keys must be unique in published tables
- freshness must remain under 2 hours for hourly feeds
- rejected records must be reviewable rather than silently dropped

## Governance

- `Lake Formation` governs consumer access
- published datasets require owners and classification tags

## Success Criteria

- lake zones are documented
- `Iceberg` publish tables are queryable in `Athena`
- contract checks and access controls are defined
