# Tutorial: Regulated Data And Compliance Workflows

This tutorial explains how to design and deliver regulated-data changes so engineering, governance, and audit expectations stay aligned from ingestion through publish.

## Goal

By the end of this tutorial, you should be able to:

- classify regulated data and map its end-to-end flow
- define controls for access, masking, encryption, retention, deletion, and publish
- connect compliance evidence to release readiness
- handle incidents, replay, and lower-environment use without breaking obligations

## Step 1: Start With Classification

Clarify:

- whether the scope includes `PII`, `PCI`, `HIPAA`, `PHI`, or contractual controls
- which fields are sensitive
- what the allowed usage is
- what retention or deletion rules apply
- who owns the data and who owns the controls

Use:

- `skills/data-security-compliance-and-regulated-data/SKILL.md`
- `references/security-compliance-regulated-data-checklist.md`

Do not treat "internal analytics use" as a reason to skip classification.

## Step 2: Map The Data Flow End To End

Include:

- landing and ingestion zones
- transformation layers
- serving and publish layers
- dashboards, reverse ETL, extracts, and partner paths
- caches, backups, and feature stores
- replay, retention, and deletion paths

If the lineage stops before a publish surface, the compliance picture is incomplete.

## Step 3: Define The Control Model

Controls usually include:

- encryption at rest and in transit
- masking, tokenization, or minimization
- row-level or column-level access control
- secrets and key-management expectations
- environment separation
- publish restrictions
- retention and deletion enforcement
- audit logging and evidence capture

Useful supporting skills:

- `skills/lineage-pii-and-governance/SKILL.md`
- `skills/privacy-retention-and-right-to-delete/SKILL.md`
- `skills/lower-environment-data-masking-and-obfuscation/SKILL.md`

## Step 4: Align Policy With Actual Platform Behavior

Check that:

- SQL and pipeline code enforce the same control intent
- warehouse, lakehouse, or cloud-native access controls match the written policy
- non-production environments do not bypass masking or minimization expectations
- deletes and retention rules reach all material copies

Documentation is not enough if the platform config contradicts it.

## Step 5: Define The Evidence And Release Gates

Before publish, require:

- lineage updates
- ownership and escalation path
- masking or access validation
- retention and deletion proof where required
- release approval criteria for regulated publish paths

Useful supporting assets:

- `templates/data-compliance-controls.yaml`
- `templates/release-gate-evidence.yaml`
- `starter-packs/regulated-data-compliance-starter.yaml`

## Step 6: Plan For Incident And Replay Behavior

Regulated data failures need:

- containment path
- audit trail preservation
- replay and backfill safety
- communication path for control owners or affected consumers

Use:

- `skills/incident-triage-and-pipeline-recovery/SKILL.md`
- `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- `references/data-resiliency-testing-patterns.md`

If replay is undefined, the control model is unfinished.

## Step 7: Handle Lower Environments Safely

When regulated data appears in development, QA, or staging:

- define masking or synthetic-data rules
- limit who can access those environments
- document refresh process and retained fields
- prove usability and safety together

Use:

- `references/lower-environment-masking-checklist.md`
- `starter-packs/test-data-lower-environments-starter.yaml`

## Step 8: Review The Red Flags

Stop and redesign if:

- regulated fields are copied without an explicit control matrix
- lineage omits extracts, caches, or reverse-ETL paths
- retention or deletion rules stop at one storage layer
- access controls are described in docs but not enforced in the platform
- audit evidence depends on tribal knowledge instead of explicit artifacts

## Good Starting Assets

- `skills/data-security-compliance-and-regulated-data/SKILL.md`
- `references/security-compliance-regulated-data-checklist.md`
- `templates/data-compliance-controls.yaml`
- `starter-packs/regulated-data-compliance-starter.yaml`
- `examples/privacy-retention-deletion-workflow/`
- `examples/validation-and-security-review-foundation/`
