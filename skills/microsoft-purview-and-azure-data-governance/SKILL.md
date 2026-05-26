---
name: microsoft-purview-and-azure-data-governance
description: Guides agents through Microsoft Purview and Azure-native data governance workflows. Use when designing collections, scans, classifications, lineage, policy boundaries, and governed publishing across ADLS, Synapse, Data Factory, Azure Databricks, Fabric, and Azure analytics estates.
---

# Microsoft Purview And Azure Data Governance

## Overview

Use this skill when `Microsoft Purview` is the governance control plane for `Azure` data platforms. It helps agents design metadata collections, classification strategy, scan scope, lineage expectations, and governed publish behavior across Microsoft analytics surfaces.

## When to Use

- designing `Purview` collection and ownership structure
- defining scans, classifications, glossary, and lineage expectations
- governing datasets across `ADLS`, `Synapse`, `Data Factory`, `Azure Databricks`, or `Fabric`
- improving trusted discovery and certification for shared data products
- aligning Azure-native governance with privacy, security, and release controls

Do not assume `Purview` is only a catalog tool. It often becomes the platform evidence and policy surface for governed analytics.

## Workflow

1. Define governance scope.
   Clarify:
   - in-scope platforms
   - business domains
   - critical data products
   - stewardship and ownership model

2. Design the metadata operating model.
   Decide:
   - collections
   - glossary boundaries
   - classifications and sensitivity labels
   - scan cadence and ownership

3. Define trusted publish behavior.
   Require:
   - certification or endorsement rules
   - lineage completeness expectations
   - ownership visibility
   - ties to regulated-data controls where relevant

4. Align Azure services with governance.
   Check how `Purview` works with `ADLS`, `Synapse`, `Data Factory`, `Databricks`, and `Fabric` rather than treating each system separately.

5. Validate operational sustainability.
   Make sure scans, classifications, and lineage remain useful as assets, teams, and environments grow.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Scanning everything is the same as governing it." | Governance also needs ownership, trust signals, and useful boundaries for consumers. |
| "Purview can be added after pipelines are done." | Late governance usually means weak lineage, poor certification, and inconsistent discovery. |
| "Each Azure service team can manage metadata separately." | Fragmented governance weakens platform-wide trust and policy evidence. |

## Red Flags

- collections do not map to real ownership or domains
- scan scope is broad but lineage and certification are weak
- classifications are inconsistent across Azure services
- `Purview` is disconnected from publish or security decisions
- stewardship expectations depend on tribal knowledge

## Verification

- [ ] Governance scope and stewardship model are explicit
- [ ] Collections, scans, and classifications are intentionally designed
- [ ] Trusted publish behavior includes lineage and certification expectations
- [ ] Azure services align to one governance model
- [ ] The model stays sustainable as adoption grows
