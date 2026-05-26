---
name: data-quality-platforms-and-rule-management
description: Guides agents through data-quality operating models and tool selection. Use when designing rule portfolios, severity levels, ownership, evidence, and enforcement across dbt tests, Great Expectations, Deequ, Cuallee, Soda, warehouse-native checks, and platform monitoring workflows.
---

# Data Quality Platforms And Rule Management

## Overview

Use this skill when the question is not only what checks to write, but how the quality program should operate across tools, teams, and publish stages. It helps agents design rule ownership, severity, evidence, and enforcement across multiple quality frameworks.

## When to Use

- selecting or combining data-quality tools
- designing rule portfolios and severity models
- aligning `dbt` tests, `Great Expectations`, `Deequ`, `Cuallee`, `Soda`, or warehouse-native checks
- deciding what blocks publish versus what raises warnings
- improving long-term maintainability of data-quality controls

Do not assume more checks automatically improve quality. The operating model matters as much as the framework.

## Workflow

1. Define the quality operating model.
   Clarify:
   - who owns rules
   - who triages failures
   - what blocks publish
   - what becomes an alert or trend signal

2. Group rules by purpose.
   Typical groups:
   - contract correctness
   - completeness and freshness
   - distribution and anomaly checks
   - reconciliation and financial controls
   - governance or regulated-data controls

3. Choose tools intentionally.
   Decide where each type of rule belongs:
   - `dbt` tests for warehouse-native model validation
   - `Great Expectations`, `Deequ`, `Cuallee`, or `Soda` for reusable framework-based checks
   - warehouse-native monitors for platform-local health signals

4. Define evidence and routing.
   Require:
   - actionable output
   - severity and ownership
   - trend visibility
   - links to incident and publish workflows

5. Control portfolio growth.
   Review overlapping, stale, noisy, or low-value checks so quality stays credible and maintainable.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We should standardize on one tool for everything." | Different rule types often fit different execution surfaces and operating models. |
| "If a rule fails, we can decide the impact later." | Publish and incident behavior must already be defined when the rule is introduced. |
| "More rules always mean better quality." | Noisy or duplicate checks reduce trust and slow triage. |

## Red Flags

- rule ownership and triage paths are unclear
- tools are chosen by preference instead of workload fit
- blocking and non-blocking checks are mixed without severity logic
- evidence is hard to review or trend over time
- stale, overlapping, or low-signal rules accumulate unchecked

## Verification

- [ ] The quality operating model defines ownership and severity clearly
- [ ] Rule groups map to real delivery risks and publish stages
- [ ] Tool choices fit execution surfaces and maintenance needs
- [ ] Evidence and routing are reviewable and actionable
- [ ] Portfolio sprawl is controlled over time
