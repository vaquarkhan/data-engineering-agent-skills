---
name: avro-protobuf-json-schema-registry
description: Guides agents through schema-registry-backed event contracts. Use when managing Avro, Protobuf, or JSON Schema for event streams, compatibility policies, producer and consumer evolution, or contract enforcement in messaging systems.
---

# Avro Protobuf JSON Schema Registry

## Overview

Use this skill when schema management for events must be explicit and enforceable. It helps agents coordinate producer changes, consumer compatibility, registry policy, and versioned contracts across teams sharing event streams.

## When to Use

- adopting a schema registry for event-driven systems
- defining or modifying Avro, Protobuf, or JSON Schema definitions
- setting compatibility policies for topics or subjects
- coordinating producer schema changes across multiple consumers
- enforcing contract governance for multi-team event ecosystems

Do not use this when schemas are managed purely through application code with no shared registry or when the system has a single producer-consumer pair with no evolution concerns.

## Workflow

1. Define schema ownership and subject naming.
   Include:
   - who owns each schema subject (team, service, domain)
   - subject naming strategy: `TopicNameStrategy`, `RecordNameStrategy`, or `TopicRecordNameStrategy`
   - where schemas are stored: Confluent Schema Registry, AWS Glue Schema Registry, Apicurio, or equivalent
   - schema source of truth: registry-first or code-first with CI sync

2. Choose the schema format intentionally.
   - `Avro`: strong ecosystem support, compact binary, requires registry for deserialization
   - `Protobuf`: excellent for multi-language teams, supports nested messages and services
   - `JSON Schema`: human-readable, looser typing, easier adoption but weaker guarantees
   - consider: serialization size, language support, tooling maturity, and team familiarity
   - do not mix formats within a single domain unless isolation is absolute

3. Define and enforce compatibility policies.
   - `BACKWARD`: new schema can read old data (safe for consumer-first evolution)
   - `FORWARD`: old schema can read new data (safe for producer-first evolution)
   - `FULL`: both backward and forward compatible (safest, most restrictive)
   - `NONE`: no compatibility checking (use only for development or isolated topics)
   - set policy per subject, not globally — different topics have different evolution needs
   - test compatibility in CI before publishing schema changes

4. Plan producer and consumer evolution paths.
   - additive changes (new optional fields): safe under backward compatibility
   - field removal or rename: breaking under most policies — requires migration
   - type changes: generally breaking — prefer new fields over type modifications
   - document the upgrade order: which side deploys first (producer or consumer)?
   - use default values explicitly to support backward reading

5. Integrate schema validation into the release workflow.
   - validate schema compatibility in CI using registry API or CLI tools
   - block releases that break compatibility policy
   - version schemas alongside service code — not independently
   - produce evidence of compatibility checks for release gates
   - define rollback plan: can a previous schema version be re-registered safely?

6. Handle multi-team governance and schema discovery.
   - publish schema documentation alongside event catalog or data catalog
   - make consumer dependency visible — who reads which schema versions?
   - define deprecation process for old schema versions
   - plan for schema registry availability as a critical path dependency

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can evolve schemas freely since it's just adding fields." | Even additive changes can break consumers if default values are missing or field semantics change without notice. |
| "The registry is just for serialization, not governance." | The registry is the enforcement point for cross-team contracts. Treating it as a utility ignores its governance value. |
| "JSON Schema is easier so we'll use it everywhere." | JSON Schema provides weaker guarantees and no binary efficiency. Format choice should match the system's durability, performance, and typing needs. |
| "Compatibility can be set to NONE during development and tightened later." | Teams rarely tighten compatibility retroactively. Setting policies early prevents breaking changes from accumulating. |

## Red Flags

- no compatibility policy defined on production subjects
- schemas are modified directly in the registry without CI validation
- producer and consumer deploy simultaneously with no coordination order
- no documentation of which consumers depend on which schema versions
- schema registry is a single point of failure with no availability plan
- field semantics change without version bumps or consumer notification
- deprecated schema versions are never cleaned up or documented
- format was chosen without considering cross-language or performance needs

## Verification

- [ ] Schema ownership and subject naming strategy are documented
- [ ] Format choice (Avro, Protobuf, JSON Schema) is justified for the use case
- [ ] Compatibility policies are set per subject and tested in CI
- [ ] Producer and consumer evolution order is defined for breaking changes
- [ ] Schema validation is part of the release workflow with blocking on incompatibility
- [ ] Consumer dependencies on schema versions are visible and tracked
- [ ] Schema registry availability and rollback procedures are planned
