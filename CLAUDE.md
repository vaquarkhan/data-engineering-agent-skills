# data-engineering-agent-skills

This is the `data-engineering-agent-skills` project: a production-grade skill registry and execution toolkit for data engineering agents.

## Project Structure

```text
skills/                  -> Core data engineering workflows (`SKILL.md` per directory)
presets/                 -> Platform presets for AWS, Azure, GCP, Databricks, Snowflake, and Apache stacks
references/              -> Checklists for quality, recovery, streaming, schema change, observability, and more
templates/               -> Source, dataset, metric, and incident templates
starter-packs/           -> Opinionated bundles by problem area
examples/                -> Scenario packs and runnable starter examples
hooks/                   -> Session and pre-flight workflow hooks
.claude/commands/        -> Slash commands (`/spec`, `/plan`, `/build`, `/validate`, `/review`, `/backfill`, `/ship`)
.gemini/commands/        -> Gemini command entry points for the same lifecycle
docs/                    -> Setup guides and getting-started documentation
vscode-extension/        -> VS Code family installer extension
jetbrains-plugin/        -> JetBrains installer plugin
```

## Start Here

1. Load `skills/using-data-engineering-agent-skills/SKILL.md`
2. Load the platform preset that matches the stack
3. Load only the task-specific skills needed for the current work
4. Pull in references, templates, and examples only when they improve decisions or verification

## Lifecycle Commands

- `/spec` -> define contract, SLA, lineage, schema, retention, and ownership
- `/plan` -> break pipeline changes into atomic tasks
- `/build` -> implement pipeline, model, or job changes incrementally
- `/validate` -> prove data quality, contract compliance, and reconciliation
- `/review` -> review reliability, cost, governance, and operability
- `/backfill` -> run safe replay and cutover workflows
- `/ship` -> deploy, observe, and keep rollback-safe release notes

## Conventions

- Every skill lives in `skills/<skill-name>/SKILL.md`
- Every preset lives in `presets/<preset-name>/PRESET.md`
- Frontmatter must contain `name` and `description`
- Skills should include: Overview, When to Use, Workflow, Common Rationalizations, Red Flags, Verification
- Presets should include: Overview, Use When, Preferred Platform Services, Design Rules, Verification

## Guardrails

- Prefer `/spec` before changing pipeline behavior
- Do not guess unclear data grain, freshness, schema, or contract semantics
- Treat quality, replay, lineage, privacy, and ownership as part of delivery
- Use hooks from `hooks/` when a session starts or before risky operations
- Use the smallest useful bundle of skills instead of loading the whole repository
