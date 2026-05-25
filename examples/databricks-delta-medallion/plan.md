# Plan: Databricks Delta Medallion

## Architecture

- raw events and snapshots land in bronze
- silver handles contract-aware cleanup, conformance, and CDC merge behavior
- gold serves business-friendly outputs with governance and observability

## Risks

- weak bronze-to-silver rules create contract drift
- uncontrolled merge patterns can create replay issues
- ignored maintenance leads to small-file and metadata pain

## Verification

- medallion responsibilities reviewed against the skill
- Delta maintenance and replay behavior documented
- gold publish tables validated for ownership and consumer readiness
