# Copilot Setup

Use this repository with GitHub Copilot by referencing the skills and presets in your repository instruction files and review workflows.

## Recommended Setup

1. Keep this repository available as a companion reference or vendor it into your internal standards repo.
2. Add the operating guidance you want into your project instructions:
   - the classification skill
   - the platform preset
   - a small number of workflow skills for the current delivery stream
3. Use personas from `agents/` for focused review prompts or pull-request review checklists.

## Suggested Mapping

- project instructions: one general operating skill plus one preset
- feature-specific prompts: one or two workflow skills
- PR review instructions: one checklist reference or reviewer persona

## Good Review Uses

- `analytics-engineer-reviewer` for marts and metric work
- `data-platform-reliability-reviewer` for operational changes
- `data-platform-infrastructure-reviewer` for platform and access changes

## Tips

- Avoid giant instruction files that dump the whole repository into one context.
- Pair skills with machine-readable templates from `templates/` when starting new work.
- Use `skills-index.md` to choose the smallest useful subset for a task.
