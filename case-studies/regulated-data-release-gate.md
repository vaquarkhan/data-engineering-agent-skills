# Case Study: Regulated Data Release Gate

## Scenario

- **Business context:** A new customer behavior dataset with sensitive attributes is being prepared for broad analyst access.
- **Trigger event:** Team wants to ship quickly, but governance controls are not fully evidenced.
- **Blast radius:** Potential `PII` leakage, policy violations, and audit exceptions.

## Target Outcome

- publish sensitive-data outputs only with enforceable controls
- retain clear audit evidence for release approval
- keep rollback available if compliance checks fail

## Stack And Scope

- **Platform:** lakehouse/warehouse with governed publish layer
- **Pipelines/components:** conformance pipeline, masking policies, publish views
- **Data contracts:** dataset contract, compliance controls template, lineage records

## Skills, Presets, And Templates Used

- **Skills:** `data-security-compliance-and-regulated-data`, `lineage-pii-and-governance`, `data-sharing-and-publishing-contracts`, `data-platform-ci-cd-and-release-management`
- **Presets:** cloud governance preset matching platform (`Glue/Lake Formation`, `Unity Catalog`, `Purview`, or `Dataplex`)
- **Templates:** `templates/data-compliance-controls.yaml`, `templates/release-gate-evidence.yaml`
- **Repo anchors:** `templates/data-compliance-controls.yaml`, `references/platform-native-governance-patterns.md`, `starter-packs/regulated-data-compliance-starter.yaml`

## Step-by-Step Execution

1. **Classify**
   - identify sensitive columns and map obligations (`PII/PCI/HIPAA` as applicable)
   - assign explicit owners and approvers for controls
2. **Enforce**
   - apply masking/tokenization and access policies at publish boundary
   - ensure lower-environment copies use masked data path
3. **Validate**
   - run contract checks, quality checks, and access-control verification
   - verify lineage covers downstream extracts, BI, and API consumers
4. **Approve**
   - attach control evidence, sign-off record, and release rationale
   - ensure incident contacts and revocation process are documented
5. **Publish**
   - release through staged visibility toggle
   - monitor audit and access logs after publish

## Evidence Required

- completed compliance controls template
- policy/masking enforcement proof
- lineage map including downstream copies
- release approval artifacts with named approver
- post-release monitoring confirmation for access/freshness anomalies

## Runbook Commands

```bash
python scripts/validate_dataset_contract.py --contract examples/aws-s3-glue-athena-iceberg/contracts/customers-contract.yaml --data examples/aws-s3-glue-athena-iceberg/build/customers.ndjson --reference-time 2026-05-02T00:00:00Z
bash hooks/release-guard.sh
python scripts/check-links.py
```

## Acceptance Thresholds

- **Control coverage:** all required controls in `templates/data-compliance-controls.yaml` are filled and marked implemented
- **Access threshold:** no unapproved role can read sensitive fields in publish layer
- **Lineage threshold:** downstream copies and extracts are documented for all sensitive columns
- **Audit threshold:** release evidence includes named approver, timestamp, and change reference
- **Monitoring threshold:** no unauthorized-access alerts for 24 hours after staged publish

## Rollback Plan

- **Rollback trigger:** failed control verification, unauthorized access signal, or missing audit evidence
- **Rollback action:** disable publish visibility and revoke broad access grants
- **Rollback validation:** only approved restricted roles retain access and prior trusted publish remains active

## Definition Of Done

- [ ] Sensitive field classification and ownership are explicit
- [ ] Masking/access controls verified technically, not only documented
- [ ] Lineage includes all meaningful downstream copies
- [ ] Release approval and audit evidence captured
- [ ] Rollback and access revocation steps validated

## Common Failure Modes

- relying on policy documents without technical enforcement checks
- forgetting downstream extracts and cache copies in lineage evidence
- granting broad access before approval artifacts are complete

## Adaptation Notes

- apply regional control overlays for sovereignty requirements
- for multi-cloud paths, enforce equivalent control evidence across each platform boundary
