---
name: data-observability-and-sla-management
description: Guides agents through data observability and service-level management. Use when defining or improving freshness, completeness, anomaly detection, alerting, lag tracking, run metadata, and ownership for production data products.
---

# Data Observability And SLA Management

## Overview

Use this skill when the pipeline must be operated as a service, not just executed as code. It helps agents define what healthy looks like and how teams know when the system drifts away from that state.

## When to Use

- launching or hardening a production data product
- defining freshness or completeness SLAs
- improving alerting and anomaly detection
- adding operational metadata and health visibility
- reducing noisy or low-signal incident response

## Workflow

1. Define the service promises.
   Include:
   - freshness SLA
   - completeness expectations
   - acceptable latency
   - owner and escalation path

2. Identify health signals.
   Common signals:
   - run success rate
   - task duration drift
   - volume anomalies
   - schema drift
   - consumer lag
   - data freshness

3. Design alerts for actionability.
   Alerts should route to someone who can act, with enough context to investigate quickly.

4. Capture run metadata and failure context.

5. Review alert quality.
   Noisy alerts damage trust just as much as missing alerts.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The scheduler already tells us if it fails." | Task failure alone does not measure stale, partial, or bad data. |
| "More alerts are safer." | Alert fatigue makes real incidents easier to miss. |
| "The business will tell us if something is wrong." | That means the system failed before the team noticed. |

## Red Flags

- no named owner or escalation path
- freshness is assumed but not measured
- alerts fire without run context or impact clues
- anomaly detection exists with no response playbook

## Verification

- [ ] SLAs and ownership are defined
- [ ] Health signals exist for freshness, completeness, and reliability
- [ ] Alerts are actionable and routed correctly
- [ ] Run metadata supports fast diagnosis
