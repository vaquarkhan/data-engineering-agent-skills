# Cursor Setup

Use this repository in `Cursor` by referencing the skills and supporting docs as project rules.

## Recommended Setup

1. Clone the repository locally.
2. Choose whether you want:
   - a small subset of skills copied into `.cursor/rules/`, or
   - this repository referenced as the source for shared rule content
3. Start with:
   - `skills/using-data-engineering-agent-skills/SKILL.md`
   - the stack preset under `presets/`
   - one or two task-specific skills such as `data-specification` or `dbt-and-analytics-engineering`

## Practical Pattern

- Use one general operating rule that tells the agent to classify work first.
- Add the platform preset that matches your environment.
- Add only the task-specific skills needed for the current project to keep context focused.

## Suggested Project Rule Flow

1. Load `using-data-engineering-agent-skills`.
2. Load the relevant preset such as `aws-data-engineering` or `databricks-lakehouse-engineering`.
3. Load workflow-specific skills only when the task needs them.
4. Load checklist references for review or release readiness.

## Tips

- Avoid loading every skill at once.
- Keep project-specific policies in your own repo and use this repository for reusable workflow logic.
- Prefer referencing templates and examples when starting new data products.
- Run `hooks/session-start.sh`, `hooks/schema-change-guard.sh`, or `hooks/release-guard.sh` for risky work if you want an extra pre-flight layer.
