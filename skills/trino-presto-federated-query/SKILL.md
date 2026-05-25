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

## Verification

- [ ] Source boundaries and semantics are explicit
- [ ] Pushdown and performance expectations are understood
- [ ] Access and governance are accounted for
