---
name: snowflake-modern-data-platform
description: Adapts the core skills for Snowflake-centered data platforms. Use when the team standardizes on Snowflake for storage, compute, governance, sharing, and warehouse-centric analytics engineering.
---

# Snowflake Modern Data Platform

## Overview

Use this preset when `Snowflake` is the primary data platform across one or more clouds. It maps core workflows to Snowflake databases, warehouses, tasks, streams, dynamic tables, governance features, and secure data-sharing patterns.

Pair this preset with `skills/snowflake-native-pipelines-and-governance/SKILL.md` when the pipeline logic, governance controls, and publish paths are primarily Snowflake-native.

## Use When

- `Snowflake` is the core storage and compute platform
- transformations are warehouse-centric
- governance and data sharing rely on Snowflake-native features
- batch and near-real-time processing are modeled around tasks, streams, or partner ingestion paths

## Preferred Platform Services

- storage and compute: `Snowflake`
- orchestration: `Snowflake Tasks` or external orchestrators
- change tracking: `Streams`, `Dynamic Tables`
- governance: roles, masking policies, row access policies, tags
- sharing: secure data sharing, listings where relevant
- monitoring: account usage views, query history, external observability

## Common Architecture Patterns

- warehouse-centric architecture with staged ingestion, modeled transforms, and semantic or BI serving inside `Snowflake`
- incremental architecture using `Streams`, `Tasks`, and `Dynamic Tables` for warehouse-native change processing
- external landing plus internal warehouse modeling when raw ingestion begins in cloud storage but governed serving stays in `Snowflake`
- secure-sharing architecture where publish outputs are designed explicitly for internal or external consumers
- Load `references/cloud-data-engineering-architecture-patterns.md` when deciding whether the warehouse should stay the primary platform boundary or participate in a hybrid architecture

## Design Rules

- Make role design, masking, and row access part of delivery, not a later review.
- Use warehouse sizing and workload isolation intentionally to manage cost and concurrency.
- Distinguish raw ingestion, modeled layers, and published semantic outputs clearly.
- Be explicit when orchestration belongs inside Snowflake versus an external scheduler.

## Verification

- [ ] Security policies and role boundaries are designed
- [ ] Compute isolation and cost considerations are documented
- [ ] Incremental or change-data strategies are explicit
- [ ] Sharing and publish expectations are defined for downstream consumers
