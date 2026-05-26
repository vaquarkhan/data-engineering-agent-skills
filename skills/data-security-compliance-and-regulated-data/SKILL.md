---
name: data-security-compliance-and-regulated-data
description: Guides agents through regulated-data security and compliance workflows for PII, PCI, HIPAA, PHI, and similar obligations. Use when data products handle sensitive fields, regulated records, control evidence, or audit-bound publish paths.
---

# Data Security, Compliance, And Regulated Data

## Overview

Use this skill when the data platform handles regulated or highly sensitive data and the change must satisfy engineering, governance, and audit expectations together. It helps agents treat controls, lineage, access, retention, deletion, evidence, and publish safety as one delivery surface.

## When to Use

- handling `PII`, `PCI`, `HIPAA`, `PHI`, or other regulated data classes
- moving sensitive data between raw, curated, serving, and partner-facing layers
- designing masking, tokenization, encryption, or access controls
- proving that published data meets audit or policy requirements
- changing lineage, retention, deletion, or evidence paths for regulated assets
- preparing a system for compliance review, internal audit, or control sign-off

Do not treat regulated-data handling as a documentation-only exercise.

## Workflow

1. Classify the data and obligations.
   Clarify:
   - what fields are sensitive
   - whether the scope includes `PII`, `PCI`, `HIPAA`, `PHI`, or contractual controls
   - what the allowed usage, retention, and deletion rules are
   - which teams own the control and audit evidence

2. Map the data flow end to end.
   Include:
   - ingestion and landing zones
   - transformation and quality layers
   - serving, BI, feature, reverse-ETL, and extract paths
   - replication, caching, backup, and replay surfaces
   - lineage and consumer touchpoints

3. Define the required controls explicitly.
   Controls may include:
   - encryption at rest and in transit
   - tokenization or masking
   - row-level and column-level access
   - environment separation
   - secrets and key management
   - restricted publish paths
   - retention and deletion enforcement
   - audit logging and evidence capture

4. Align implementation with policy and platform behavior.
   Verify that code, SQL, orchestration, and platform configuration all enforce the same control intent.

5. Define compliance evidence and release gates.
   Require:
   - lineage updates
   - ownership and escalation path
   - test or validation evidence for masking, access, and deletion behavior
   - publish approval criteria when regulated data leaves the producing boundary

6. Plan for incidents and replay.
   Regulated data failures need:
   - containment path
   - audit trail preservation
   - replay or backfill safety
   - communication path for impacted consumers or control owners

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The warehouse already encrypts everything." | Encryption alone does not satisfy access, minimization, retention, lineage, or audit evidence obligations. |
| "This is only internal analytics data." | Internal use does not remove obligations for `PII`, `PCI`, `HIPAA`, or contractual data-handling controls. |
| "The source system already handles compliance." | Downstream copies, extracts, feature stores, and dashboards create new control surfaces. |
| "We can document the control evidence later." | Missing evidence often turns routine changes into release blockers or audit findings. |

## Red Flags

- regulated fields are copied without a control matrix
- lineage is incomplete for a sensitive publish path
- retention or deletion rules stop at one storage layer
- replay or backfill behavior for sensitive data is undefined
- access controls are described in docs but not enforced in code or platform config
- compliance approval depends on tribal knowledge instead of explicit evidence

## Verification

- [ ] Sensitive fields and regulatory scope are classified explicitly
- [ ] End-to-end lineage and storage locations are mapped
- [ ] Access, masking, encryption, retention, and deletion controls are implemented or clearly planned
- [ ] Audit evidence and release gates are defined for the regulated-data path
- [ ] Incident, replay, and rollback paths preserve both correctness and compliance obligations
