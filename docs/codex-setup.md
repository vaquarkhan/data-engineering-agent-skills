# Codex Setup

Use this repository with Codex or other agents that support repository-local instruction files.

## Recommended Setup

1. Copy or reference `AGENTS.md`
2. Copy or reference `CLAUDE.md`
3. Copy or reference `hooks/` if you want workflow guardrails available locally
4. Keep the relevant platform preset and workflow skills available in the project
5. Use `templates/` and `examples/` to start new data products
6. Use `docs/getting-started.md` as the canonical quickstart

## Suggested Bundle

- `AGENTS.md`
- `CLAUDE.md`
- `skills/using-data-engineering-agent-skills/SKILL.md`
- one preset from `presets/`
- one or two task-specific skills

## Tips

- Keep the active context small
- Use starter packs from `starter-packs/` to pick a coherent bundle quickly
- Treat the runnable examples as the fastest path to adoption
- Use `/validate` and `/backfill` as first-class workflow phases, not afterthoughts
