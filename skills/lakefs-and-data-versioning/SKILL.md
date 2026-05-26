---
name: lakefs-and-data-versioning
description: Guides agents through data versioning workflows using lakeFS or similar systems. Use when branching data, validating changes before publish, or controlling risky lakehouse operations with versioned data states.
---

# lakeFS And Data Versioning

## Overview

Use this skill when datasets need branch-like safety and controlled promotion. It helps agents treat data versioning as an operational control for risky changes, tests, and cutovers.

## When to Use

- validating data changes before publish
- branching lake data for experiments or cutovers
- promoting data states between environments

## Workflow

1. Define the versioning goal and branch lifecycle.
2. Separate experimental states from publish states.
3. Attach validation and promotion gates to version moves.
4. Make rollback and cleanup explicit.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The platform-specific feature is the whole design." | Platform features do not replace contract, compatibility, and operational planning. |
| "We can validate this after publish." | Late validation is expensive when downstream consumers already depend on the asset. |
| "Operations can figure out the edge cases later." | Replay, maintenance, and publish safety need to be explicit before adoption. |

## Red Flags

- downstream compatibility is assumed instead of documented
- publish or replay behavior is not explicit
- maintenance, rollback, or observability expectations are missing
## Verification

- [ ] Data versioning has a clear operational purpose
- [ ] Promotion and rollback behavior are documented
- [ ] Validation gates exist before publish
