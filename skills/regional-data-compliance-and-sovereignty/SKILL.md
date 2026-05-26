---
name: regional-data-compliance-and-sovereignty
description: Guides agents through region-specific data compliance, residency, sovereignty, and transfer design. Use when data products must operate across jurisdictions such as Europe, the USA, India, Saudi Arabia, or regulated sectors with local supervisory overlays like SAMA.
---

# Regional Data Compliance And Sovereignty

## Overview

Use this skill when data obligations differ by jurisdiction, sector, or supervisory authority. It helps agents translate legal and policy requirements into engineering decisions for storage location, transfer boundaries, access, retention, deletion, and audit evidence. This skill is not legal advice; it is the engineering planning layer that should work with legal, privacy, and compliance owners.

## When to Use

- operating across `Europe`, the `USA`, `India`, `Saudi Arabia`, or other multi-jurisdiction footprints
- handling data residency, sovereignty, or cross-border transfer constraints
- designing controls for `GDPR`, `PDPL`, `DPDP`, state privacy, or sector-specific obligations
- working in regulated sectors where local supervisors such as `SAMA` add extra controls
- preparing localized retention, deletion, consent, or breach-evidence paths

Do not assume one global control pattern satisfies every jurisdiction.

## Workflow

1. Name the jurisdiction and sector overlays.
   Include:
   - where data subjects or customers are located
   - where data is stored and processed
   - sector overlays such as finance, health, or public-sector controls
   - supervisory bodies or internal policy owners

2. Map cross-border and intra-region data flows.
   Identify:
   - ingestion location
   - replication and backup paths
   - support and admin access paths
   - analytics, ML, and partner-sharing paths
   - logs and telemetry containing regulated data

3. Convert obligations into engineering controls.
   Controls may include:
   - regional storage boundaries
   - localized encryption and key ownership
   - access restrictions by geography or role
   - data minimization and masking
   - transfer approvals and evidence
   - retention and deletion policies by jurisdiction

4. Design the operating model.
   Decide:
   - what can be centralized
   - what must stay local
   - how regional exceptions are versioned and reviewed
   - how incidents and regulator-facing evidence are handled

5. Validate the design with local proof.
   Require:
   - lineage of regulated regional flows
   - evidence for residency and transfer controls
   - ownership and escalation paths
   - review by legal, privacy, or compliance stakeholders

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Our global standard should be enough everywhere." | Jurisdictions often differ on transfer controls, evidence, localization, and supervisory expectations. |
| "The cloud region solves sovereignty automatically." | Region choice alone does not control support access, backups, logs, exports, or downstream copies. |
| "It is only analytics data." | Analytics copies still create residency, deletion, and transfer obligations. |

## Red Flags

- jurisdiction-specific controls exist only in policy documents, not engineering paths
- support, admin, or backup access crosses borders without review
- localized deletion, retention, or transfer evidence is missing
- `SAMA`, `GDPR`, `DPDP`, or similar obligations are mentioned with no named control owner

## Verification

- [ ] Jurisdiction and sector overlays are named explicitly
- [ ] Cross-border flows, copies, and admin paths are mapped
- [ ] Residency, transfer, access, and deletion controls are engineered, not only described
- [ ] Regional evidence, ownership, and review paths are defined
