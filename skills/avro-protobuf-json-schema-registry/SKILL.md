---
name: avro-protobuf-json-schema-registry
description: Guides agents through schema-registry-backed event contracts. Use when managing Avro, Protobuf, or JSON Schema for event streams, compatibility policies, producer and consumer evolution, or contract enforcement in messaging systems.
---

# Avro Protobuf JSON Schema Registry

## Overview

Use this skill when schema management for events must be explicit and enforceable. It helps agents coordinate producer changes, consumer compatibility, registry policy, and versioned contracts.

## When to Use

- event schema registry adoption
- producer or consumer schema changes
- compatibility policy definition
- multi-team event contract governance

## Workflow

1. Define schema ownership and compatibility policy.
2. Choose the schema representation intentionally.
3. Validate producer and consumer change paths.
4. Tie registry policy to release and incident workflows.

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

- [ ] Schema ownership and compatibility policy are explicit
- [ ] Change paths for producers and consumers are documented
- [ ] Registry behavior is part of release safety
