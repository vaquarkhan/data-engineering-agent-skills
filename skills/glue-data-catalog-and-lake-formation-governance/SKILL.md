---
name: glue-data-catalog-and-lake-formation-governance
description: Guides agents through AWS-native data catalog and lake governance workflows. Use when designing or reviewing Glue Data Catalog, Lake Formation permissions, governed sharing, metadata quality, and access boundaries for S3, Athena, Redshift, EMR, or Glue pipelines.
---

# Glue Data Catalog And Lake Formation Governance

## Overview

Use this skill when `AWS` governance is anchored in `Glue Data Catalog` and `Lake Formation`, not only in generic metadata tools. It helps agents design catalog structure, access controls, governed sharing, and publish-safe dataset access across lake and warehouse workflows.

## When to Use

- designing `Glue Data Catalog` database or table organization
- defining `Lake Formation` permissions, tag-based access, or sharing boundaries
- reviewing governed access for `S3`, `Athena`, `Glue`, `EMR`, or `Redshift`
- improving metadata quality for AWS-native data discovery
- aligning platform-native governance with regulated-data and publish controls

Do not treat `Lake Formation` and the catalog as only platform-admin setup. They are part of delivery design.

## Workflow

1. Define the governed asset boundary.
   Clarify which datasets, tables, zones, and consumers need AWS-native governance.

2. Design the catalog structure.
   Decide:
   - database boundaries
   - table naming and ownership
   - metadata quality expectations
   - partition and location conventions

3. Define the access model.
   Include:
   - principals and roles
   - tag-based access where appropriate
   - row or column restrictions when required
   - cross-account or consumer sharing behavior

4. Align publish behavior with governance.
   Require:
   - certified versus raw asset distinctions
   - explicit publish approval or validation gates where needed
   - lineage and ownership visibility for shared assets

5. Validate operational behavior.
   Check how permissions, schema evolution, new partitions, and cross-service access behave under real delivery conditions.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "IAM alone is enough." | Dataset governance often needs finer-grained sharing, tagging, and lake access patterns than broad service-level IAM. |
| "We can clean up catalog metadata later." | Poor metadata and unclear ownership make governed data hard to discover and trust. |
| "Lake Formation is only for the platform team." | Producers still need to design publish boundaries and access assumptions around it. |

## Red Flags

- database and table ownership are unclear
- `Lake Formation` permissions are bolted on after publish design
- catalog metadata does not distinguish trusted and experimental assets
- cross-account sharing or consumer access paths are undocumented
- schema and partition changes are not validated against governance behavior

## Verification

- [ ] Catalog structure and ownership are intentionally designed
- [ ] `Lake Formation` permissions and sharing boundaries are explicit
- [ ] Metadata quality supports discovery and governance
- [ ] Publish and access behavior are aligned
- [ ] Operational behavior is validated for schema and access changes
