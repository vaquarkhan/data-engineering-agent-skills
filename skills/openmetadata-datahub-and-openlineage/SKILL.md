---
name: openmetadata-datahub-and-openlineage
description: Guides agents through metadata platform and lineage workflows using OpenMetadata, DataHub, or OpenLineage-compatible systems. Use when improving discovery, lineage quality, metadata governance, or producer-to-catalog integration.
---

# OpenMetadata DataHub And OpenLineage

## Overview

Use this skill when metadata and lineage must be operationalized through open tooling such as `OpenMetadata`, `DataHub`, or `OpenLineage`. It helps agents align producers, lineage events, and discovery quality.

## When to Use

- integrating metadata platforms into delivery workflows
- improving lineage and discovery quality
- publishing governed datasets into open catalog ecosystems

## Workflow

1. Define metadata ownership and minimum required fields.
2. Connect lineage capture to actual execution surfaces.
3. Publish trust signals and ownership with the asset.
4. Review metadata quality whenever contracts change.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The platform-specific feature is the whole design." | Platform features do not replace contract, compatibility, and operational planning. |
| "We can validate this after publish." | Late validation is expensive when downstream consumers already depend on the asset. |
| "Operations can figure out the edge cases later." | Replay, maintenance, and publish safety need to be explicit before adoption. |

## Red Flags

- downstream compatibility is assumed instead of documented
- publish or replay behavior is not explicit
- maintenance, rollback, or observability expectations are missing
## Verification

- [ ] Ownership, lineage, and discovery metadata are captured
- [ ] Metadata is tied to real execution and publish events
- [ ] Consumers can distinguish trusted from experimental assets
