# Generic Markdown Rules Setup

This repository is plain Markdown and can be used with any agent or rules-based system that accepts instruction files.

## Minimal Setup

Pick:

- one operating skill
- one platform preset
- one or two workflow skills
- optional checklist references

## Good Default Starter Bundle

- `skills/using-data-agent-skills/SKILL.md`
- one preset from `presets/`
- `skills/data-specification/SKILL.md`
- `skills/pipeline-planning-and-task-breakdown/SKILL.md`
- `skills/data-quality-and-contract-testing/SKILL.md`

## Task-Specific Bundles

### Modeling

- `warehouse-and-schema-design`
- `dbt-and-analytics-engineering`
- `semantic-layer-and-metric-governance`

### Streaming

- `streaming-and-messaging-systems`
- `orchestration-and-backfills`
- `data-observability-and-sla-management`

### Lakehouse

- `lakehouse-table-format-engineering`
- `data-lake-and-zone-architecture`
- `delta-lake-and-medallion-architecture`

### Reliability

- `data-observability-and-sla-management`
- `incident-triage-and-pipeline-recovery`
- one relevant execution skill

## Tips

- Keep the bundle small and role-specific.
- Combine templates and examples with the skills to seed concrete artifacts.
- Prefer workflow skills over long descriptive docs when the agent must act.
