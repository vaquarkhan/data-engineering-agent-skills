# ETL ELT Modernization Checklist

Use this checklist when choosing between `ETL`, `ELT`, or hybrid transformation boundaries.

## Workload Fit

- [ ] Latency, volume, complexity, and security constraints are explicit
- [ ] The chosen execution boundary matches where transformations should really run
- [ ] Pre-load controls are defined when sensitive data must be protected before landing

## Current-State Recovery

- [ ] Existing transformation logic is inventoried across tools
- [ ] Duplicate business rules across ETL jobs, Spark, and warehouse SQL are identified
- [ ] Hidden scheduler, parameter, or manual dependencies are documented

## Modernization

- [ ] A phased target-state path is defined
- [ ] Parity, reconciliation, and cost review are part of the plan
- [ ] Cutover and rollback are operationally real

## Operability

- [ ] Lineage and observability continue across the new boundary
- [ ] Ownership and on-call expectations are clear
- [ ] Old transformation paths have a retirement plan
