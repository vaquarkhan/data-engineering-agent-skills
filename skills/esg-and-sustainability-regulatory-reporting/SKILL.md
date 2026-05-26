---
name: esg-and-sustainability-regulatory-reporting
description: Guides agents through ESG, sustainability, and regulatory reporting data products. Use when building governed metrics, traceable evidence, and audit-ready data pipelines for frameworks such as CSRD/ESRS, BRSR, climate disclosures, or similar sustainability reporting obligations.
---

# ESG And Sustainability Regulatory Reporting

## Overview

Use this skill when sustainability reporting becomes a governed data-engineering problem instead of a spreadsheet exercise. It helps agents build traceable data pipelines, materiality and methodology records, value-chain inputs, approval paths, and assurance-ready evidence for ESG or sustainability disclosures.

## When to Use

- building data products for `CSRD`, `ESRS`, `BRSR`, climate, or investor-facing sustainability disclosures
- managing emissions, workforce, supplier, governance, or value-chain metrics
- preparing ESG datasets for audit, assurance, or board reporting
- replacing spreadsheet-driven sustainability reporting with governed pipelines
- aligning sustainability metrics with finance, ERP, procurement, and operational source systems

Do not treat ESG reporting as presentation-layer work only.

## Workflow

1. Define the reporting perimeter and framework.
   Clarify:
   - reporting framework and audience
   - legal entity and consolidation scope
   - materiality or relevance process
   - required disclosures, KPIs, and narrative dependencies

2. Map each disclosure to source systems and owners.
   Include:
   - source documents and systems
   - transformation logic
   - estimation or proxy rules
   - approvers and accountable owners
   - value-chain or supplier-supplied data

3. Make methodology versioned and reviewable.
   Record:
   - calculation rules
   - emission factors or external reference sets
   - thresholds and materiality criteria
   - change logs
   - exception handling

4. Build controls and evidence around the data product.
   Require:
   - lineage to source evidence
   - approval workflow
   - segregation of duties where needed
   - reconciliation and reasonableness checks
   - locked reporting snapshots

5. Design for assurance and publication.
   Confirm:
   - every datapoint can be traced
   - reported outputs can be regenerated
   - narrative and metric versions are aligned
   - publication format and archival requirements are known

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The ESG team owns this, not engineering." | Sustainability reporting becomes an engineering problem once metrics, lineage, controls, and assurance matter. |
| "We only need annual reporting, so spreadsheets are fine." | Annual disclosures still require traceability, version control, and repeatable evidence. |
| "We can clean the data before audit." | Assurance failures usually come from weak source mapping and methodology control, not last-minute cleanup. |

## Red Flags

- ESG metrics have no accountable data owner
- source evidence and published values cannot be traced end to end
- methodology changes are made with no version history
- value-chain or supplier inputs are used with no provenance or confidence rating
- reporting scope and financial consolidation boundaries do not match

## Verification

- [ ] Reporting framework, scope, and materiality logic are explicit
- [ ] Each KPI is mapped to sources, methodology, and owners
- [ ] Lineage, controls, and approval evidence exist
- [ ] The reporting output is assurance-ready and reproducible
