# Skill Anatomy

This document defines the recommended structure for data engineering skills.

## File Layout

Each skill lives in its own directory:

```text
skills/
  skill-name/
    SKILL.md
```

Add supporting files only when they keep the main skill focused.

## Required Frontmatter

```yaml
---
name: skill-name
description: Guides agents through a specific workflow. Use when the task matches clear trigger conditions.
---
```

Rules:

- `name` must match the directory name
- use lowercase hyphen-separated names
- `description` must say what the skill does and when to use it

## Recommended Sections

```markdown
# Skill Title

## Overview

## When to Use

## Workflow

## Common Rationalizations

## Red Flags

## Verification
```

## Writing Rules

- Treat skills as workflows, not essays.
- Keep instructions concrete and executable.
- State what evidence proves the work is done.
- Add rationalization rebuttals for steps agents often skip.
- Avoid stack-specific wording in shared skills unless unavoidable.

## Data Engineering Expectations

Good skills in this repository usually account for:

- source contracts
- schema evolution
- idempotency
- backfills
- data quality checks
- lineage and ownership
- access controls and sensitive data handling
- observability and failure recovery

## Exit Criteria

A strong skill should help an agent answer:

- What exactly should I do?
- When should I use this skill?
- What should I avoid?
- What evidence proves success?
