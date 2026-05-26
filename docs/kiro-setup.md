# Kiro Setup

Use this repository with `Kiro` by installing workspace steering files under `.kiro/steering/`.

## Recommended Setup

1. Keep this repository available locally.
2. Create or use a workspace-level `.kiro/steering/` folder.
3. Start with these steering files:
   - `.kiro/steering/product.md`
   - `.kiro/steering/tech.md`
   - `.kiro/steering/structure.md`
4. Keep the main workflow entrypoint available:
   - `skills/using-data-engineering-agent-skills/SKILL.md`
5. Load one matching preset and only the workflow skills needed for the current task.

## How Kiro Should Use This Repo

- Use steering files for persistent workspace context.
- Use `skills/` and `presets/` as the task-specific operating layer.
- Use `references/` and `templates/` only when they improve decisions or provide reviewable evidence.
- Use `registry/assets.json` if you need a machine-readable index of templates, starter packs, examples, MCP templates, and install bundles.

## Suggested Flow

1. Classify the task with `skills/using-data-engineering-agent-skills/SKILL.md`
2. Load the platform preset matching the stack
3. Load one or two workflow skills
4. Pull in starter packs, templates, hooks, or examples as needed

## Tips

- Keep core steering files small and durable.
- Add specialized steering files under `.kiro/steering/` only when a project needs persistent extra context.
- Use `hooks/` and machine-readable templates for replay, schema, and release-sensitive work.
