---
name: multi-cloud-hybrid-data-engineering
description: Adapts the core skills for hybrid and multi-cloud data platforms. Use when data systems span more than one cloud, mix cloud and on-prem components, or must avoid hard coupling to a single provider.
---

# Multi-Cloud Hybrid Data Engineering

## Overview

Use this preset when the platform crosses cloud boundaries or includes on-prem systems. The emphasis is portability, governance consistency, controlled data movement, and minimizing operational surprises caused by environment differences.

## Use When

- systems span more than one cloud
- there is a mix of cloud and on-prem data infrastructure
- regulatory, regional, or acquisition constraints require multiple platforms
- teams want portable table formats and execution layers

## Preferred Platform Services

- storage: object storage with portable conventions and open table formats where practical
- orchestration: an engine that can coordinate across environments
- compute: engines with clear packaging and environment isolation
- governance: centralized ownership, lineage, and policy mapping across platforms
- monitoring: consolidated observability and alert routing

## Design Rules

- Minimize cross-cloud data movement unless a business or regulatory reason justifies it.
- Keep contracts, lineage, and ownership consistent even when services differ.
- Prefer open formats and well-defined interfaces over provider-specific lock-in for shared layers.
- Make region, network, and egress cost part of architecture decisions, not post-launch tuning.
- Test backfills and recovery across boundary points where failures are hardest to diagnose.

## Verification

- [ ] System boundaries and cross-environment dependencies are explicit
- [ ] Contracts and governance rules remain consistent across platforms
- [ ] Egress, latency, and operational ownership are documented
- [ ] Recovery and replay plans account for cross-platform failure modes
