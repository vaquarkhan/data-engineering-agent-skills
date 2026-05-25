---
name: privacy-retention-and-right-to-delete
description: Guides agents through privacy, retention, and deletion workflows in data systems. Use when handling personal data, retention limits, deletion requests, legal holds, or data minimization requirements across pipelines and published datasets.
---

# Privacy, Retention, And Right To Delete

## Overview

Use this skill when the data platform must respect privacy obligations as an engineering behavior, not a policy slide. It helps agents make retention, deletion, masking, and minimization explicit across storage, transformations, and publishes.

## When to Use

- handling personal or regulated data
- defining retention rules
- implementing deletion or erasure requests
- changing how sensitive fields are stored, copied, or published
- validating that downstream systems do not retain data longer than allowed

Do not assume masking alone satisfies retention or deletion obligations.

## Workflow

1. Classify the data and obligations.
   Clarify:
   - sensitive fields
   - retention limit
   - deletion trigger
   - legal hold exceptions
   - downstream replication paths

2. Map where the data lives.
   Include:
   - raw landing
   - transformed tables
   - serving layers
   - extracts
   - caches and feature stores

3. Define the enforcement path.
   Decide how the system will:
   - prevent unnecessary copies
   - enforce retention windows
   - process deletions
   - prove compliance actions happened

4. Validate downstream propagation.
   Deletion in one layer is not enough if copies remain elsewhere.

5. Record exceptions and audit evidence.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The source system already deleted it." | Downstream data products may still retain copies. |
| "We only use hashed identifiers." | Hashing does not eliminate all privacy or retention duties. |
| "We can clean up old data later." | Retention failures often become expensive compliance incidents. |

## Red Flags

- no retention schedule exists
- deletion requests stop at one system boundary
- old extracts and caches are ignored
- privacy controls rely on undocumented manual steps

## Verification

- [ ] Sensitive data and retention obligations are classified
- [ ] All material storage locations and copies are mapped
- [ ] Deletion and retention enforcement are explicit and testable
- [ ] Audit evidence or runbooks exist for compliance actions
