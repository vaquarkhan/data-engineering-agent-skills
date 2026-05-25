---
name: terraform-and-data-platform-infrastructure
description: Guides agents through infrastructure as code for data platforms. Use when provisioning or modifying storage, roles, secrets, networking, orchestration resources, catalogs, compute, or environment-specific data platform foundations.
---

# Terraform And Data Platform Infrastructure

## Overview

Use this skill when data engineering work depends on platform infrastructure, not just SQL or code. It helps agents make environment setup reproducible, reviewable, and promotion-safe.

## When to Use

- provisioning buckets, warehouses, jobs, roles, or secrets
- changing network or access boundaries
- creating environment-specific data platform resources
- standardizing dev, staging, and production infrastructure

Do not treat manual console changes as equivalent to managed infrastructure.

## Workflow

1. Identify the platform boundary.
   Decide which resources belong in infrastructure code versus application or transformation code.

2. Model environments explicitly.
   Capture:
   - naming rules
   - isolation boundaries
   - secrets strategy
   - promotion path

3. Keep access and governance in the same review surface as infrastructure.

4. Validate change safety before apply.
   Watch for:
   - destructive resource replacement
   - role drift
   - environment coupling
   - hidden manual dependencies

5. Document day-two operations.
   Provisioning is only part of the lifecycle.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is faster to click this in the console." | Manual changes drift quickly and are hard to review or reproduce. |
| "We only need Terraform for production." | Lower environments drift first and make promotion less trustworthy. |
| "Security can update roles separately." | Infra and access changes often need one coordinated review. |

## Red Flags

- resource names and environments are inconsistent
- secrets handling is unclear
- destructive changes are not reviewed explicitly
- manual prerequisites are undocumented

## Verification

- [ ] Infrastructure boundaries and environment model are explicit
- [ ] Access, secrets, and governance are reviewed with the infra change
- [ ] Apply risk is understood before rollout
- [ ] Day-two operations are documented where relevant
