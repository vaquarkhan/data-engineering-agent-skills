---
name: data-platform-disaster-recovery-and-business-continuity
description: Guides agents through disaster recovery and business continuity planning for data platforms. Use when defining region or account failover, backup and restore, RTO or RPO targets, control-plane recovery, or restore drills for pipelines, warehouses, lakehouses, and publish surfaces.
---

# Data Platform Disaster Recovery And Business Continuity

## Overview

Use this skill when the question is how the data platform survives major failure, not only how one incident is handled. It helps agents design recovery objectives, backup and restore paths, control-plane recovery, failover decisions, and repeatable restore drills for data systems.

## When to Use

- defining `RTO` and `RPO` for critical datasets or platform services
- planning region, account, or environment failover
- validating backup and restore behavior for warehouses, lakes, or stateful processors
- designing business continuity for shared data products and critical publish paths
- running recovery drills before a real outage forces them

Do not confuse incident handling with disaster recovery planning. Disaster recovery is the plan for major platform loss or sustained unavailability.

## Workflow

1. Classify the critical services and data products.
   Identify:
   - critical datasets
   - control-plane dependencies
   - orchestration and metadata services
   - downstream consumer and business impact

2. Define recovery objectives.
   Include:
   - `RTO`
   - `RPO`
   - acceptable degraded mode
   - mandatory publish protections during failover

3. Map recovery assets and dependencies.
   Cover:
   - backups and snapshots
   - checkpoint or incremental state
   - orchestration definitions
   - secrets and access paths
   - lineage and metadata services
   - validation and reconciliation controls after restore

4. Choose the recovery strategy.
   Options may include:
   - restore in place
   - warm standby
   - cold standby
   - cross-region or cross-account failover
   - consumer-facing degraded mode with blocked publish

5. Prove the recovery path.
   Run drills for:
   - restore time
   - checkpoint continuity
   - publish blocking and reopen criteria
   - reconciliation after restore
   - ownership and escalation behavior

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The cloud provider already handles availability." | Provider uptime does not replace dataset restore, metadata recovery, or publish-safe failover design. |
| "We have backups, so we are covered." | Untested backups and undefined restore ownership do not prove business continuity. |
| "We can work out the failover steps during an outage." | Major outages are the worst time to discover recovery dependencies or missing permissions. |

## Red Flags

- no named `RTO` or `RPO` exists for critical data products
- backup inventory ignores metadata, orchestration, or incremental state
- failover is described without validation or reconciliation after restore
- publish behavior during degraded mode is undefined
- recovery drills have never been executed

## Verification

- [ ] Critical data products and services have explicit recovery objectives
- [ ] Backup, restore, and dependency recovery paths are documented
- [ ] Recovery strategy matches business impact and platform constraints
- [ ] Restore drills validate time, correctness, and publish protection
- [ ] Ownership and escalation paths are clear during major outage scenarios
