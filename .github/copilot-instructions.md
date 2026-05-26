# Copilot Instructions

Use the shared data engineering skill pack from this repository as the primary workflow source.

## Loading Order

1. Start with `AGENTS.md`
2. Use `skills/using-data-engineering-agent-skills/SKILL.md`
3. Load one platform preset from `presets/`
4. Load one or more workflow skills from `skills/`
5. Use checklist references from `references/` for review and verification

## Behavior

- prefer specification before code changes
- keep contracts, grain, and ownership explicit
- do not treat a successful run as proof of correctness
- prefer small, verifiable changes over wide rewrites
- use examples and templates when starting a new data product
- treat `/validate` and `/backfill` as first-class workflow phases

## Common Task Mappings

- new data product: `data-specification`, `pipeline-planning-and-task-breakdown`
- warehouse modeling: `warehouse-and-schema-design`, `dbt-and-analytics-engineering`
- lakehouse: `data-lake-and-zone-architecture`, `lakehouse-table-format-engineering`
- streaming: `streaming-and-messaging-systems`, `data-observability-and-sla-management`
- incidents: `incident-triage-and-pipeline-recovery`
