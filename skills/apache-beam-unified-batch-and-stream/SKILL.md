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

## Verification

- [ ] Batch and streaming behavior are both understood
- [ ] Runner-specific assumptions are documented
- [ ] Time semantics and sink guarantees are explicit
