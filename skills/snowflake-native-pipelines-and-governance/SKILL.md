---
name: snowflake-native-pipelines-and-governance
description: Guides agents through Snowflake-native pipeline and governance workflows. Use when building or reviewing Snowflake pipelines with Streams, Tasks, Dynamic Tables, Snowpipe, Snowpark, masking policies, row access, secure sharing, and warehouse-native operational controls.
---

# Snowflake Native Pipelines And Governance

## Overview

Use this skill when `Snowflake` is not just the storage target but the primary pipeline and governance surface. It helps agents reason about native ingestion, incremental patterns, task orchestration, governance controls, warehouse sizing, and secure publish paths inside Snowflake.

## When to Use

- building warehouse-native incremental pipelines in `Snowflake`
- designing with `Streams`, `Tasks`, or `Dynamic Tables`
- evaluating `Snowpipe`, `Snowpark`, or external orchestration boundaries
- defining masking, row access, tags, and secure sharing in the same workflow
- reviewing publish readiness for Snowflake-native data products

Do not assume Snowflake-native is automatically the right answer for every compute and orchestration step.

## Workflow

1. Define the execution boundary.
   Decide what should stay inside `Snowflake` versus what belongs in upstream landing, external orchestration, or other compute services.

2. Choose the incremental pattern.
   Consider:
   - `Streams`
   - `Tasks`
   - `Dynamic Tables`
   - `Snowpipe`
   - external orchestration when boundaries are broader than Snowflake alone

3. Design governance and access together.
   Include:
   - roles
   - masking policies
   - row access policies
   - tags and classification
   - secure publish or sharing boundaries

4. Make warehouse operations explicit.
   Cover:
   - warehouse sizing
   - concurrency and isolation
   - cost controls
   - retry and rerun behavior
   - validation before publish

5. Define publish and recovery behavior.
   Require:
   - reconciliation or validation gates
   - controlled reopen after failure
   - rollback or forward-fix plan for warehouse-native publishes

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Because the data is in Snowflake, the pipeline should also live there." | Some landing, preprocessing, orchestration, or resilience controls still belong outside the warehouse. |
| "Tasks prove the pipeline is production-ready." | Task success alone does not prove contract correctness, reconciliation, or secure publish behavior. |
| "Masking can be added after the model is stable." | Governance controls are part of the design, not cleanup after delivery. |

## Red Flags

- Snowflake-native execution is chosen without explicit boundary reasoning
- incremental behavior is vague across `Streams`, `Tasks`, or `Dynamic Tables`
- warehouse cost and concurrency implications are not documented
- secure-sharing or publish controls are undefined
- governance is described in docs but not reflected in Snowflake-native policies

## Verification

- [ ] The Snowflake execution boundary is explicit and justified
- [ ] Incremental and orchestration behavior is designed intentionally
- [ ] Governance and access controls are defined with the pipeline design
- [ ] Warehouse sizing, cost, and isolation considerations are documented
- [ ] Publish, recovery, and validation behavior are explicit
