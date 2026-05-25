---
name: data-lake-and-zone-architecture
description: Guides agents through data lake and zone architecture design. Use when defining raw, refined, curated, or publish layers; storage organization; retention; and operational boundaries for a data lake.
---

# Data Lake And Zone Architecture

## Overview

Use this skill when the storage platform needs structure before pipelines scale into chaos. It helps agents design clear lake zones, dataset boundaries, ownership, lifecycle rules, and publish-safe storage conventions.

## When to Use

- designing a new data lake
- reorganizing raw, staging, refined, or curated zones
- defining object storage layout and lifecycle rules
- separating landing, transformation, and publish responsibilities
- reducing data swamp behavior in shared lake storage

Do not use this to justify creating extra layers with no operational purpose.

## Workflow

1. Define the lake purpose and consumers.
   Clarify:
   - source landing needs
   - internal producer teams
   - publish consumers
   - compliance and retention expectations

2. Define the zone model intentionally.
   Typical zones include:
   - raw or landing
   - standardized or staging
   - refined or modeled
   - publish or serving

3. Assign responsibilities to each zone.
   Decide:
   - who writes to it
   - who reads from it
   - what quality guarantees exist
   - whether mutation is allowed

4. Design storage conventions.
   Include:
   - path or catalog naming
   - partition strategy
   - retention lifecycle
   - file-size expectations
   - ownership tags and metadata

5. Keep publish rules separate from lake convenience.
   Not every dataset in the lake is ready for shared consumption.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can dump everything into one bucket or container and organize later." | That is how data lakes turn into data swamps. |
| "More zones always means better governance." | Extra layers without distinct purpose add complexity and slow teams down. |
| "If the file exists in the lake, it is available for analytics." | Raw landing data rarely has the quality or contract guarantees needed for shared use. |

## Red Flags

- zone meanings overlap or are undocumented
- ownership is unclear at the dataset or zone level
- publish and landing data are mixed together
- retention, cleanup, or lifecycle policy is absent

## Verification

- [ ] The zone model has clear purposes and boundaries
- [ ] Ownership, read/write expectations, and quality guarantees are explicit
- [ ] Storage conventions and lifecycle rules are documented
- [ ] Shared publish datasets are separated from raw landing data
