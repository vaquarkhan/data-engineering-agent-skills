# Data Platform DR And BCP Checklist

Use this checklist when defining disaster recovery and business continuity for critical data services.

## Recovery Objectives

- [ ] Critical datasets and services are identified
- [ ] `RTO` and `RPO` are defined
- [ ] Degraded-mode expectations are explicit
- [ ] Publish behavior during failover is defined

## Recovery Dependencies

- [ ] Backup and snapshot inventory is current
- [ ] Metadata, orchestration, and secret dependencies are included
- [ ] Checkpoint or incremental state recovery is covered
- [ ] Cross-region or cross-account dependencies are documented

## Recovery Strategy

- [ ] Restore-in-place, standby, or failover strategy is explicit
- [ ] Ownership and escalation paths are defined
- [ ] Validation and reconciliation after restore are part of the plan
- [ ] Consumer communication path exists for major outages

## Drills

- [ ] Recovery drills have been run
- [ ] Restore time was measured
- [ ] Correctness after restore was validated
- [ ] Results were recorded and used to improve the recovery plan
