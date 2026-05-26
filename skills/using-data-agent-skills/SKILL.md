---
name: using-data-agent-skills
description: Provides a compatibility alias for the main data engineering entry skill. Use when an existing setup still points at the legacy start-here file.
---

# Using Data Agent Skills

## Overview

This legacy entry point remains for compatibility with older setups. The preferred start-here skill is `using-data-engineering-agent-skills`, which provides the current classification flow, preset mapping, example routing, and next-command guidance.

## When to Use

- loading an older project that still points to this skill
- triaging a request before switching to the current entry skill
- preserving compatibility for previously installed rule bundles

Do not use this as the long-term default. Switch to `skills/using-data-engineering-agent-skills/SKILL.md` once the session starts.

## Workflow

1. Redirect the session to `skills/using-data-engineering-agent-skills/SKILL.md`.
   - Treat that skill as the default router.
   - Use it to choose the platform preset, example, and next command.

2. Preserve older references safely.
   - If docs, rules, or prompts still mention `using-data-agent-skills`, do not fail the session.
   - Treat the old name as an alias, not a separate workflow.

3. Continue with the real task skill.
   - `data-specification` for unclear intent
   - `pipeline-planning-and-task-breakdown` for sequencing
   - `data-quality-and-contract-testing` for correctness and publish gates
   - `incident-triage-and-pipeline-recovery` for broken production behavior

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The old start-here skill is good enough." | The newer entry skill has the current routing logic, examples, and command mapping. |
| "We can keep using both as separate workflows." | Treat the old name as an alias so the repository does not drift into duplicate behavior. |
| "Renaming the start-here skill is risky." | Compatibility is preserved as long as this alias continues to redirect cleanly. |

## Red Flags

- the session keeps this alias loaded instead of the newer start-here skill
- docs or rules reference two different entry skills as if both are primary
- the agent skips preset or command selection after triage

## Verification

- [ ] The session has been redirected to `using-data-engineering-agent-skills`
- [ ] Older bundles still work without breaking changes
- [ ] The active workflow moved on to the real execution skill after triage
