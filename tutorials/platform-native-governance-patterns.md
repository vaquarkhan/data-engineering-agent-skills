# Platform Native Governance Patterns

Use this tutorial when the team needs cloud-native governance choices, not only generic catalog guidance.

## What You Will Do

1. Choose the primary governance surface
2. Map ownership and publish boundaries
3. Align metadata and access controls
4. Validate day-2 operations

## Step 1: Choose The Primary Governance Surface

Start with the platform boundary:

- `AWS` -> `Glue Data Catalog` and `Lake Formation`
- `Databricks` -> `Unity Catalog`
- `Azure` -> `Microsoft Purview`
- `GCP` -> `Dataplex` plus `BigQuery` governance

Do not run multiple governance models with no clear primary system unless the hybrid design is deliberate.

## Step 2: Map Ownership And Publish Boundaries

Define:

- producer domains
- consumer boundaries
- trusted versus exploratory assets
- certification or publish expectations

## Step 3: Align Metadata And Access

For the chosen platform, define:

- hierarchy and ownership
- classifications or tags
- lineage expectations
- access and sharing behavior

## Step 4: Validate Day-2 Operations

Review:

- onboarding new datasets
- schema and policy changes
- adding new consumers
- promotion across environments or workspaces

## Recommended Companion Assets

- `references/platform-native-governance-patterns.md`
- `skills/glue-data-catalog-and-lake-formation-governance/SKILL.md`
- `skills/unity-catalog-and-lakehouse-governance/SKILL.md`
- `skills/microsoft-purview-and-azure-data-governance/SKILL.md`
- `skills/dataplex-and-bigquery-governance/SKILL.md`
