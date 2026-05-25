# Plan: Privacy Retention Deletion Workflow

## Architecture

- classify sensitive fields and owning domains
- map raw, transformed, and published copies
- enforce retention and deletion across all relevant layers

## Risks

- downstream copies can be forgotten
- deletions can stop at one system boundary
- compliance evidence can be too weak to review later

## Verification

- storage and lineage review
- retention and deletion coverage review
- runbook and audit-evidence review
