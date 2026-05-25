---
name: lineage-pii-and-governance
description: Applies governance, lineage, ownership, and sensitive-data controls to data changes. Use when a pipeline touches published datasets, regulated information, or shared business metrics.
---

# Lineage, PII, And Governance

## Overview

Governance is an engineering concern, not a cleanup exercise. This skill ensures that every meaningful data change accounts for ownership, lineage, access, and sensitive-data handling before release.

## When to Use

- publishing a new table, model, or stream
- changing business-critical metrics
- handling personal, financial, health, or otherwise sensitive data
- modifying access controls or data-sharing patterns
- changing upstream or downstream lineage

## Workflow

1. Identify ownership and consumers.
   Every published dataset should have:
   - an owner
   - intended consumers
   - known downstream dependencies

2. Classify the data.
   Determine whether fields are:
   - public
   - internal
   - confidential
   - regulated or sensitive

3. Define required controls.
   Controls may include:
   - masking
   - tokenization
   - row-level restrictions
   - column-level restrictions
   - encryption requirements
   - retention or deletion rules

4. Update lineage and documentation.
   Record how the data flows from source to publish layer, including major transformations.

5. Verify policy enforcement in implementation.
   Do not stop at documentation. Check that access and masking rules are actually reflected in code or platform configuration.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is only internal data." | Internal datasets still create exposure, misuse, and compliance risk. |
| "We will document lineage later." | Lineage that is not updated during change work becomes stale immediately. |
| "Security will handle masking downstream." | Sensitive data should be controlled as close to production as possible. |

## Red Flags

- published data has no named owner
- sensitive fields are copied without classification
- lineage updates are missing for a shared metric
- access rules are assumed but not enforced

## Verification

- [ ] Dataset ownership and consumers are identified
- [ ] Sensitive fields are classified
- [ ] Required controls are implemented or explicitly planned
- [ ] Lineage and documentation reflect the change
- [ ] Governance checks are based on real enforcement, not comments alone
