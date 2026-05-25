---
name: warehouse-performance-and-cost-optimization
description: Guides agents through warehouse performance and cost decisions. Use when optimizing BigQuery, Snowflake, Redshift, Athena, Synapse, or lakehouse query patterns, storage layout, and workload isolation.
---

# Warehouse Performance And Cost Optimization

## Overview

Use this skill when data is correct but too slow or too expensive. It helps agents treat performance and cost as measurable design concerns rather than guesswork.

## When to Use

- slow warehouse queries
- runaway compute or scan cost
- poor partitioning or clustering choices
- overloaded workloads competing on shared compute
- repeated complaints about expensive marts or dashboards

Do not optimize blindly. Start from observed cost or performance signals.

## Workflow

1. Identify the real bottleneck.
   Measure:
   - scan volume
   - slot or warehouse usage
   - partition pruning
   - join behavior
   - concurrency patterns

2. Classify the problem.
   Common buckets:
   - physical design
   - SQL pattern
   - workload isolation
   - storage layout
   - refresh frequency

3. Fix the cheapest high-impact issue first.
   Examples:
   - partitioning
   - clustering
   - pre-aggregation
   - materialization change
   - compute right-sizing

4. Keep business correctness stable while optimizing.

5. Record the trade-off.
   Faster is not always cheaper, and cheaper is not always acceptable.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We just need a bigger warehouse." | More compute often hides poor layout or query design. |
| "Optimization can wait until later." | Cost debt compounds quickly in shared platforms. |
| "The query only runs once a day." | Expensive daily jobs can still be major recurring waste. |

## Red Flags

- performance work starts with no baseline measurement
- cost issues are blamed on the platform alone
- optimizations change business logic without validation
- the same expensive pattern repeats across many models

## Verification

- [ ] Baseline cost or performance metrics exist
- [ ] The bottleneck category is identified
- [ ] The change preserves correctness while improving performance or cost
- [ ] The resulting trade-off is documented
