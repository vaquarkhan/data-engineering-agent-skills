---
name: superset-and-metrics-serving
description: Guides agents through Superset and metrics-serving workflows. Use when publishing governed metrics to Superset, defining semantic consistency for dashboards, or managing chart-ready analytical datasets.
---

# Superset And Metrics Serving

## Overview

Use this skill when `Apache Superset` or a similar BI serving surface is the final consumer layer. It helps agents keep chart-ready data aligned with governed metrics and dataset contracts.

## When to Use

- publishing datasets into `Superset`
- aligning dashboard logic with shared metrics
- preventing BI-layer drift from governed definitions

## Workflow

1. Define the serving dataset and metric contract.
2. Keep dashboard-facing logic aligned with centralized definitions.
3. Separate exploratory assets from governed publish assets.
4. Validate access, freshness, and semantic consistency.

## Verification

- [ ] Serving datasets have explicit ownership and grain
- [ ] Metrics align with centralized definitions
- [ ] Exploratory and governed assets are distinguishable
