# Incident Runbook: [Incident Name]

## Summary

- Owner:
- Severity:
- Started at:
- Current status:

## Affected Assets

- datasets:
- pipelines:
- downstream consumers:

## Immediate Containment

- [ ] pause or isolate bad publishes if needed
- [ ] notify owners and affected consumers
- [ ] preserve evidence before broad reruns

## Impact

- type of issue: stale / missing / duplicate / incorrect
- affected time window:
- business impact:

## Recovery Options

1. rerun
2. replay
3. rollback
4. partial correction
5. full backfill

Chosen option:

## Validation Gates

- [ ] row count or partition reconciliation
- [ ] metric reconciliation
- [ ] freshness restored
- [ ] publish reopened only after validation

## Root Cause

Document the actual trigger and contributing factors.

## Guardrails Added

- [ ] new validation
- [ ] alerting update
- [ ] runbook update
- [ ] contract or code change
