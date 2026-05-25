# Preset Anatomy

This document defines the recommended structure for stack-specific presets.

## File Layout

Each preset lives in its own directory:

```text
presets/
  preset-name/
    PRESET.md
```

## Required Frontmatter

```yaml
---
name: preset-name
description: Adapts the core skills for a specific platform. Use when the team runs on a defined cloud, lakehouse, or warehouse stack.
---
```

Rules:

- `name` must match the directory name
- use lowercase hyphen-separated names
- the description must say what the preset covers and when to use it

## Recommended Sections

```markdown
# Preset Title

## Overview

## Use When

## Preferred Platform Services

## Design Rules

## Verification
```

## Writing Rules

- Keep workflow logic in shared skills when possible.
- Use presets to map decisions to platform-native services and constraints.
- Call out operational, governance, and cost trade-offs.
- Mention alternatives only when they change the implementation path.
- Keep the preset useful for agents making architecture and implementation decisions.

## Typical Topics

Good presets usually cover:

- storage and table formats
- ingestion and streaming services
- orchestration choices
- compute and transformation engines
- governance, secrets, and access controls
- observability, cost, and recovery expectations
