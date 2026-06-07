---
name: openmetadata-datahub-and-openlineage
description: Guides agents through metadata platform and lineage workflows using OpenMetadata, DataHub, or OpenLineage-compatible systems. Use when improving discovery, lineage quality, metadata governance, or producer-to-catalog integration.
---

# OpenMetadata DataHub And OpenLineage

## Overview

Use this skill when metadata and lineage must be operationalized through open tooling such as `OpenMetadata`, `DataHub`, or `OpenLineage`. It helps agents align producers with catalog expectations, ensure lineage accuracy, and make discovery trustworthy rather than decorative.

## When to Use

- integrating metadata platforms into delivery workflows
- improving dataset discovery and trust signals
- capturing and validating lineage across pipelines
- publishing governed datasets into open catalog ecosystems
- connecting `OpenLineage` events from Spark, Airflow, or dbt to a catalog
- defining metadata governance policies for multi-team environments

Do not use this when the team has no shared catalog requirement or when lineage is handled entirely within a closed platform (e.g., Unity Catalog, Purview) with no open integration needs.

## Workflow

1. Define metadata ownership and minimum required fields.
   Include:
   - who owns each dataset's metadata (producing team, platform team, or steward)
   - minimum required fields: owner, description, classification, freshness, grain
   - which fields are auto-populated from lineage vs manually maintained
   - how metadata quality is measured and enforced
   - what "complete" means for a dataset to appear as discoverable

2. Connect lineage capture to actual execution surfaces.
   - `OpenLineage` integration with orchestrators (Airflow, Dagster)
   - `OpenLineage` integration with processing engines (Spark, dbt, Flink)
   - validate that lineage events fire correctly on job start, complete, and failure
   - test that column-level lineage propagates through transformation layers
   - monitor for gaps: jobs that run but produce no lineage events

3. Make discovery trustworthy through quality signals.
   - surface trust indicators: last validated, freshness, quality score, owner responsiveness
   - distinguish production-governed datasets from experimental or deprecated ones
   - tag datasets with classification levels (public, internal, restricted, sensitive)
   - ensure search relevance: descriptions, tags, and usage signals improve discoverability
   - retire stale assets — dead datasets in the catalog erode trust

4. Integrate metadata publishing into the pipeline lifecycle.
   - metadata should update when pipelines deploy, not in separate manual workflows
   - use CI/CD hooks to validate metadata completeness before release
   - publish schema changes to the catalog automatically through lineage events
   - trigger alerts when metadata freshness falls behind actual data freshness
   - make metadata a release-gate requirement: no catalog entry, no production access

5. Plan for multi-team governance and federated ownership.
   - define roles: data producer, data steward, platform admin, consumer
   - establish policies for who can modify metadata for shared datasets
   - create templates for common dataset types so teams start with good defaults
   - define escalation paths when metadata quality issues are found
   - audit metadata coverage regularly and report gaps per team

6. Handle lineage accuracy and drift.
   - lineage can become stale when pipelines change without updating integration
   - schedule lineage validation: compare catalog lineage with actual pipeline structure
   - alert when expected lineage events stop firing
   - plan for lineage in complex scenarios: dynamic tables, views, materialized CTEs
   - document lineage limitations: what the system captures vs what it cannot

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We'll add metadata later after the pipeline is stable." | Metadata added later is often wrong because context is lost. Capturing metadata during development is cheaper and more accurate. |
| "Lineage is automatic — we just need to install the integration." | Integrations capture lineage from supported execution paths only. Custom code, dynamic SQL, and non-instrumented tools create gaps that require explicit attention. |
| "The catalog is just for discovery — it doesn't need to be accurate." | An inaccurate catalog is worse than no catalog. Teams lose trust and stop using it, making the investment worthless. |
| "Metadata governance is overhead for small teams." | Small teams benefit most from metadata discipline because there's less institutional knowledge to fall back on when someone leaves. |

## Red Flags

- catalog has datasets with no owner, no description, or stale freshness indicators
- lineage graph has gaps for major pipelines or transformation layers
- metadata is manually maintained in a spreadsheet separate from the platform
- no process for retiring deprecated or stale datasets from the catalog
- lineage integration is installed but nobody validates its output
- teams publish data without any catalog entry or metadata requirement
- column-level lineage is claimed but never tested for accuracy
- metadata quality is never measured or reported

## Verification

- [ ] Metadata ownership is defined and minimum required fields are enforced
- [ ] Lineage events fire correctly from orchestrators and processing engines
- [ ] Column-level lineage is validated for critical transformation paths
- [ ] Discovery trust signals (freshness, quality, classification) are surfaced
- [ ] Metadata publishing is integrated into the pipeline CI/CD lifecycle
- [ ] Stale and deprecated assets are regularly retired from the catalog
- [ ] Lineage accuracy is audited and gaps are tracked per pipeline
