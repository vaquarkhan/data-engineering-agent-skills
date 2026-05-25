# Claude Setup

Use this repository with Claude-style agent workflows by loading skills as reusable instruction files.

## Recommended Setup

1. Keep this repository available locally.
2. Start sessions with:
   - `skills/using-data-agent-skills/SKILL.md`
   - one platform preset from `presets/`
   - one or more workflow skills based on the task
3. Pull in references only when you need verification checklists or deeper support material.

## Suggested Load Order

1. classification skill
2. platform preset
3. task workflow skill
4. supporting checklist

## Good Session Pattern

- For a new pipeline, load `data-specification`, `pipeline-planning-and-task-breakdown`, and the relevant preset.
- For a production issue, load `incident-triage-and-pipeline-recovery`, `data-observability-and-sla-management`, and the relevant execution skill.
- For modeling work, load `warehouse-and-schema-design`, `dbt-and-analytics-engineering`, and `semantic-layer-and-metric-governance`.

## Tips

- Keep the active skill set narrow per task.
- Treat the examples directory as a quick way to seed initial context for new projects.
- Use templates from `templates/` as the starting point for project-specific artifacts.
