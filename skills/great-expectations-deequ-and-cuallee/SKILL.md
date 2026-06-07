---
name: great-expectations-deequ-and-cuallee
description: Guides agents through data-quality frameworks such as Great Expectations, Deequ, and Cuallee. Use when implementing framework-based validation suites, reusable checks, or evidence-driven data-quality enforcement.
---

# Great Expectations Deequ And Cuallee

## Overview

Use this skill when the team wants structured quality enforcement through a data-quality framework instead of ad hoc checks. It helps agents align contracts with expectation suites, route failures by severity, and produce reviewable validation evidence.

## When to Use

- implementing `Great Expectations` expectation suites or checkpoints
- adding `Deequ` analyzers and constraints to Spark pipelines
- using `Cuallee` for lightweight PySpark or Pandas validation
- standardizing reusable quality checks across datasets
- integrating framework-based quality gates into CI/CD or publish workflows
- producing validation evidence for audits or release gates

Do not use this when a few inline assertions are sufficient or when the team has no plan to reuse checks across datasets.

## Workflow

1. Ground the validation suite in a real contract.
   - start from the dataset contract: grain, freshness, allowed nulls, value ranges
   - do not invent checks that are not tied to a documented expectation
   - map each contract field to one or more framework checks
   - classify checks by severity: critical (blocks publish), warning (alert only), informational

2. Choose the right framework for the runtime context.
   - `Great Expectations`: best for warehouse/lake validation with rich documentation output
   - `Deequ`: best for Spark pipelines with compile-time constraint definitions
   - `Cuallee`: best for lightweight validation in PySpark or Pandas without heavy setup
   - consider execution environment: batch, streaming micro-batch, or CI tests
   - avoid framework lock-in by keeping contract definitions separate from framework syntax

3. Design expectation suites with maintenance in mind.
   - organize expectations by dataset and domain, not by framework capability
   - keep suites small and focused — one suite per dataset or model output
   - parameterize thresholds so they can be adjusted without code changes
   - version suites alongside the pipeline code that produces the data
   - document when and why each expectation was added

4. Integrate validation into the pipeline lifecycle.
   - run validation after transformation, before publish or downstream consumption
   - critical failures must block publish and trigger alerts
   - warning failures must be logged and visible but do not block
   - produce structured evidence output (JSON, HTML, or YAML) for each run
   - store validation results for historical trending and audit

5. Make evidence reviewable and actionable.
   - validation output should be human-readable, not just pass/fail
   - include row counts, failure percentages, and sample failing records
   - route evidence to dashboards, Slack, or incident workflows based on severity
   - link validation results to the specific pipeline run and data partition

6. Plan for expectation evolution and false positives.
   - as data changes, expectations need updates — budget for this work
   - define a process for reviewing and tuning noisy expectations
   - distinguish true data issues from expectation drift
   - retire expectations that no longer match the active contract

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We'll add expectations later when we have time." | Quality frameworks deliver value only when integrated during pipeline development. Retrofitting is harder and often abandoned. |
| "Every column needs an expectation." | Over-instrumented suites create noise. Expectations should be grounded in contract requirements, not framework capability. |
| "The framework handles severity for us." | Severity classification requires human judgment about business impact. Frameworks provide mechanics, not decisions. |
| "Validation passed so the data is correct." | Validation proves conformance to documented expectations. It cannot catch requirements that were never specified. |

## Red Flags

- expectation suites with no connection to a dataset contract
- all checks are critical severity with no triage or routing plan
- validation output is discarded after each run — no historical evidence
- suites are never updated when contracts change
- framework is chosen based on hype instead of runtime compatibility
- validation runs after publish, not before
- no plan for handling noisy or flapping expectations
- checks exist but nobody reviews failures or trends

## Verification

- [ ] Every expectation maps to a documented contract field or business rule
- [ ] Severity levels are defined: critical blocks publish, warning alerts, informational logs
- [ ] Framework choice matches the runtime context (Spark, warehouse, Pandas)
- [ ] Validation runs before publish and produces structured, stored evidence
- [ ] Evidence output includes row counts, failure rates, and sample records
- [ ] There is a process for reviewing, tuning, and evolving expectations over time
- [ ] Historical validation results are available for trend analysis and audit
