---
name: trino-presto-federated-query
description: Guides agents through Trino and Presto federated query design. Use when querying across heterogeneous systems, planning semantic consistency, or managing performance and governance in federated analytics.
---

# Trino Presto Federated Query

## Overview

Use this skill when `Trino` or `Presto` sits across multiple data systems. It helps agents reason about federation boundaries, pushdown limits, consistency, and governed consumption.

## When to Use

- querying across multiple stores with `Trino` or `Presto`
- defining governed federated analytics access
- managing performance, semantics, and access across systems

## Workflow

1. Define the federation boundary and use case.
2. Identify consistency and pushdown assumptions.
3. Make performance and access trade-offs explicit.
4. Prefer curated published datasets when federation becomes operationally risky.

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

- [ ] Source boundaries and semantics are explicit
- [ ] Pushdown and performance expectations are understood
- [ ] Access and governance are accounted for
