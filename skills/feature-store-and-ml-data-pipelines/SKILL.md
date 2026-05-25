---
name: feature-store-and-ml-data-pipelines
description: Guides agents through machine-learning data pipelines and feature serving workflows. Use when designing feature generation, offline and online consistency, training-serving parity, point-in-time correctness, or ML-oriented data product contracts.
---

# Feature Store And ML Data Pipelines

## Overview

Use this skill when the platform must support model training and inference safely. It helps agents design feature generation, point-in-time correctness, serving parity, and operational contracts for ML-focused data products.

## When to Use

- building training datasets
- designing feature stores or reusable features
- supporting online and offline feature access
- preventing leakage and training-serving mismatch
- publishing model-ready data products

Do not treat feature pipelines as ordinary marts with different names. ML pipelines have different correctness risks.

## Workflow

1. Define the feature contract.
   Include:
   - entity key
   - feature meaning
   - update cadence
   - online or offline use
   - freshness expectation

2. Protect point-in-time correctness.
   Training data must only include information available at prediction time.

3. Align offline and online logic.
   Reuse definitions and validation wherever possible to prevent training-serving drift.

4. Define feature lifecycle and ownership.
   Clarify:
   - producer
   - consumers
   - deprecation path
   - quality monitoring

5. Validate operational behavior.
   Models break when stale or missing features silently propagate.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can use the latest value for training." | That often introduces leakage and overstates model performance. |
| "Online parity is a model-team problem." | Feature consistency is a data pipeline responsibility too. |
| "Features are internal, so contracts are unnecessary." | Unclear feature meaning leads to misuse and drift. |

## Red Flags

- no point-in-time logic is defined
- offline and online definitions diverge
- stale features are not monitored
- feature ownership is unclear

## Verification

- [ ] Feature meaning, keys, and freshness are documented
- [ ] Point-in-time correctness is protected
- [ ] Offline and online parity expectations are explicit
- [ ] Monitoring exists for stale, missing, or drifting features
