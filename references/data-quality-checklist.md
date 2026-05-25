# Data Quality Checklist

Use this checklist when reviewing or implementing data pipelines and published datasets.

## Contracts

- [ ] Required fields are defined
- [ ] Types are explicit
- [ ] Primary or business keys are identified
- [ ] Null handling rules are documented
- [ ] Schema evolution expectations are known

## Correctness

- [ ] Uniqueness checks exist where needed
- [ ] Referential integrity is validated where relevant
- [ ] Accepted values are constrained
- [ ] Source-to-target reconciliation exists for critical metrics

## Freshness

- [ ] Update cadence is defined
- [ ] Freshness SLA is defined
- [ ] Late-arriving data behavior is defined
- [ ] Stale-data alerting path is known

## Publish Readiness

- [ ] Ownership is assigned
- [ ] Downstream consumers are identified
- [ ] Backfill behavior is understood
- [ ] Validation evidence is captured
