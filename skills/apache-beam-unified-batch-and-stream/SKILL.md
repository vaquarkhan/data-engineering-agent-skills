---
name: apache-beam-unified-batch-and-stream
description: Guides agents through Apache Beam pipelines that unify batch and streaming logic. Use when designing Beam transforms, windowing, runners, replay behavior, or portability across execution backends.
---

# Apache Beam Unified Batch And Stream

## Overview

Use this skill when `Apache Beam` is the abstraction layer for both batch and streaming data processing. It helps agents preserve portability without hiding time semantics or runner-specific constraints.

## When to Use

- building `Apache Beam` pipelines
- targeting multiple runners
- sharing logic across batch and streaming modes
- managing windowing, watermarks, and runner compatibility

## Workflow

1. Define the contract and time semantics first.
2. Separate portable pipeline logic from runner-specific deployment details.
3. Validate windowing, triggers, and replay behavior explicitly.
4. Confirm sink guarantees and operational observability.

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

- [ ] Batch and streaming behavior are both understood
- [ ] Runner-specific assumptions are documented
- [ ] Time semantics and sink guarantees are explicit
