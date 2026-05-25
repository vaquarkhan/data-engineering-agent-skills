# Contributing

Thanks for contributing to `data-engineering-agent-skills`.

## What To Contribute

Good contributions usually fall into one of these groups:

- new skills for recurring data engineering workflows
- new presets for cloud, lakehouse, or warehouse platforms
- improvements to existing skills based on real project experience
- reference checklists that support existing skills
- templates for specifications, plans, contracts, or runbooks
- example projects that show how the system should be used

## Quality Bar

Every contribution should be:

- specific, not generic advice
- verifiable, with observable exit criteria
- practical, based on real delivery work
- compact, so an agent can actually follow it
- vendor-neutral by default unless the file is clearly a stack-specific extension

## Skill Requirements

Every skill must:

- live under `skills/<skill-name>/SKILL.md`
- use lowercase hyphen-separated names
- define both what the skill does and when to use it
- include a workflow, rationalizations, red flags, and verification steps

## Preset Requirements

Every preset should:

- live under `presets/<preset-name>/PRESET.md`
- use lowercase hyphen-separated names
- describe where the preset fits and where it does not fit
- map common concerns to platform-native services
- keep the shared skills vendor-neutral and move stack details into the preset
- include verification expectations for security, cost, reliability, and governance

## Content Guidelines

- Prefer process over explanation.
- Prefer examples over abstract rules.
- Prefer checklists over long essays.
- Prefer direct language over marketing language.
- Do not add branding phrases that imply a tool authored the content.
- Do not duplicate a shared workflow when a preset overlay is enough.

## Pull Request Expectations

Before opening a change:

- confirm the skill or template solves a repeatable problem
- keep the scope small and reviewable
- update nearby docs when behavior changes
- include at least one realistic example when adding a new pattern

## Suggested Flow

1. Open an issue or write a short proposal.
2. Add or update the relevant skill, reference, or template.
3. Verify naming, structure, and clarity.
4. Submit a focused pull request with the reasoning behind the change.
