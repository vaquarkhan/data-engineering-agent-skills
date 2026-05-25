# Data Engineering Agent Entry Point

Use this file as the generic entry point for agents that support `AGENTS.md`-style repository instructions.

## Operating Model

1. Start with `skills/using-data-agent-skills/SKILL.md`.
2. Load the platform preset from `presets/` that matches the environment.
3. Load only the workflow skills needed for the current task.
4. Pull in references or templates only when they add decision value or verification value.

## Default Workflow

- unclear request: use `data-specification`
- approved scope: use `pipeline-planning-and-task-breakdown`
- modeling work: use `warehouse-and-schema-design` and `dbt-and-analytics-engineering`
- streaming work: use `streaming-and-messaging-systems`
- lakehouse work: use `data-lake-and-zone-architecture` and `lakehouse-table-format-engineering`
- reliability issues: use `data-observability-and-sla-management` and `incident-triage-and-pipeline-recovery`

## Guardrails

- prefer specification before implementation
- do not guess unclear data grain or contract behavior
- treat quality, replay, lineage, privacy, and ownership as part of delivery
- prefer a small set of active skills over loading the whole repository

## High-Value References

- `skills-index.md`
- `templates/source-contract.yaml`
- `templates/dataset-contract.yaml`
- `templates/metric-contract.yaml`
- `templates/incident-runbook.md`
- `examples/README.md`
