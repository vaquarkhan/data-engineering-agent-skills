# Security, Compliance, And Regulated Data Checklist

Use this checklist when data products handle `PII`, `PCI`, `HIPAA`, `PHI`, or other regulated data classes.

## Classification

- [ ] Sensitive fields are classified explicitly
- [ ] Regulatory or contractual scope is named clearly
- [ ] Data owners and control owners are identified

## Data Flow And Lineage

- [ ] Source-to-publish lineage is mapped
- [ ] Replication, caches, extracts, backups, and feature paths are included
- [ ] Downstream consumers of regulated data are identified

## Controls

- [ ] Encryption in transit and at rest is defined
- [ ] Masking, tokenization, or minimization is explicit where required
- [ ] Row-level or column-level access restrictions are documented and enforced
- [ ] Secrets and key-management expectations are defined

## Retention And Deletion

- [ ] Retention window is explicit per storage layer
- [ ] Deletion or erasure propagation is defined
- [ ] Legal hold or exception rules are documented

## Evidence And Release Gates

- [ ] Audit evidence exists for the control path
- [ ] Validation covers masking, access, and publish behavior
- [ ] Release approval path is explicit for regulated publish surfaces
- [ ] Incident and replay plans preserve compliance evidence
