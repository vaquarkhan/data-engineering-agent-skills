# Windsurf Setup

Use this repository with `Windsurf` by keeping a tight project rule bundle and pulling in extra skills only when needed.

## Quick Setup

Create a focused `.windsurfrules` file in your project. Start with the main entry skill, one preset, and one workflow skill.

Recommended starter bundle:

- `skills/using-data-engineering-agent-skills/SKILL.md`
- one preset from `presets/`
- one task skill such as `data-specification` or `dbt-and-analytics-engineering`

## Example Project Rules

```markdown
# Data engineering starter rules

[Paste skills/using-data-engineering-agent-skills/SKILL.md]

---

[Paste one platform preset]

---

[Paste one task workflow skill]
```

## Good Usage Pattern

1. start every session by classifying the task
2. keep the active bundle small
3. pull in checklist references only for review or validation
4. use `/validate` and `/backfill` concepts even if you invoke them in natural language

## Suggested Add-Ons

- `references/data-quality-checklist.md`
- `references/streaming-checklist.md`
- `templates/dataset-contract.yaml`
- `templates/incident-runbook.md`
