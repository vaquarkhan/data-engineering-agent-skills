---
name: data-migration-and-platform-cutover
description: Guides agents through data migration and platform cutover workflows. Use when moving pipelines, tables, contracts, orchestration, or workloads between systems, clouds, warehouses, lakehouses, or serving layers.
---

# Data Migration And Platform Cutover

## Overview

Use this skill when the system is changing platforms or major architectural boundaries. It helps agents plan parallel runs, compatibility layers, validation, and safe cutover rather than treating migration as a one-day switch.

## When to Use

- migrating from one warehouse or lakehouse to another
- moving pipelines between orchestration or compute systems
- replatforming storage formats or table engines
- performing major serving-layer cutovers

Do not start cutover work without a rollback and validation path.

## Workflow

1. Define the migration scope.
   Include:
   - source platform
   - target platform
   - affected datasets and jobs
   - compatibility expectations
   - cutover window

2. Choose the migration pattern.
   Common patterns:
   - parallel run
   - shadow validation
   - phased consumer cutover
   - bulk migration plus freeze window

3. Define validation gates.
   Typical gates:
   - row counts
   - metric reconciliation
   - freshness parity
   - schema compatibility
   - performance or cost acceptance

4. Make rollback real.
   Rollback should be executable, not a sentence in a plan.

5. Retire the old path deliberately after confidence is established.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can switch everything at once during a quiet window." | Hidden downstream dependencies often make big-bang cutovers fragile. |
| "If the data matches once, we are done." | Cutovers also need sustained operational parity and recovery confidence. |
| "We can keep the old path around indefinitely just in case." | Zombie dual paths create confusion and extra risk unless retired deliberately. |

## Red Flags

- rollback is not executable
- consumer cutover is assumed rather than coordinated
- validation is limited to a one-time row count
- the old and new systems are both considered source-of-truth after cutover

## Verification

- [ ] Migration scope and target behavior are explicit
- [ ] The cutover pattern and validation gates are documented
- [ ] Rollback is real and tested where practical
- [ ] Old-path retirement is planned after stable adoption
