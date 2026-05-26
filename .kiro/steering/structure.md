---
inclusion: always
---

# Project Structure

Follow this routing pattern when working in this repository:

1. Start with `skills/using-data-engineering-agent-skills/SKILL.md`
2. Load the closest platform preset from `presets/`
3. Load only the workflow skills needed for the current task
4. Pull in references, templates, starter packs, or examples only when they improve proof or reduce ambiguity

Important structure rules:

- keep the active context small
- prefer starter packs and examples when bootstrapping new work
- use `templates/backfill-plan.yaml`, `templates/schema-change-plan.yaml`, and `templates/release-gate-evidence.yaml` for operationally risky changes
- use `hooks/session-start.sh`, `hooks/backfill-guard.sh`, `hooks/schema-change-guard.sh`, and `hooks/release-guard.sh` as pre-flight checks when useful

If a specialized steering file is needed later, add it under `.kiro/steering/` rather than overloading a single file.
