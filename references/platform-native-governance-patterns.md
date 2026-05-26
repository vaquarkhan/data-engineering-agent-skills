# Platform Native Governance Patterns

Use this guide when governance depends on cloud-native catalog and policy surfaces instead of only generic metadata tools.

## AWS: Glue Data Catalog And Lake Formation

Use this pattern when:

- the lake is centered on `S3`
- governed access flows through `Athena`, `Glue`, `EMR`, or `Redshift`
- dataset sharing and publish boundaries must stay AWS-native

Key design questions:

- How should databases and tables map to producer ownership?
- Where should `Lake Formation` permissions and tags enforce access boundaries?
- How are trusted publish layers distinguished from exploratory assets?

## Databricks: Unity Catalog

Use this pattern when:

- `Databricks` is the platform standard
- shared `Delta` assets need governed publishing
- multi-team or multi-workspace separation matters

Key design questions:

- How should catalogs and schemas reflect ownership and publish boundaries?
- Which assets use managed tables versus external locations?
- How are shares, views, and external consumers governed?

## Azure: Microsoft Purview

Use this pattern when:

- the platform spans `ADLS`, `Synapse`, `Data Factory`, `Databricks`, or `Fabric`
- lineage, classification, and certification are important to governed analytics
- the business needs one Azure-native evidence surface

Key design questions:

- How should collections and stewardship align to domains?
- Which scans and classifications are required to keep trusted discovery useful?
- How do certification and publish rules tie to governance?

## GCP: Dataplex And BigQuery Governance

Use this pattern when:

- governance spans both `Cloud Storage` and `BigQuery`
- policy tags and zone boundaries matter
- trusted discovery and regulated publishing must work on `GCP`

Key design questions:

- How should lakes, zones, and datasets map to producers and consumers?
- Where do policy tags enforce controls?
- How are trusted and exploratory assets differentiated?

## Cross-Platform Rules

- keep ownership visible in the governance hierarchy
- align governance with publish boundaries, not only storage boundaries
- include schema and policy change behavior in the design
- treat lineage and trust signals as part of adoption, not nice-to-have metadata
