---
name: apache-beam-unified-batch-and-stream
description: Guides agents through Apache Beam pipelines that unify batch and streaming logic. Use when designing Beam transforms, windowing, runners, replay behavior, or portability across execution backends.
---

# Apache Beam Unified Batch And Stream

## Overview

Use this skill when `Apache Beam` is the abstraction layer for both batch and streaming data processing. It helps agents preserve portability without hiding time semantics or runner-specific constraints.

## When to Use

- building `Apache Beam` pipelines for batch, streaming, or unified workloads
- targeting multiple runners such as `Dataflow`, `Flink`, `Spark`, or `Direct Runner`
- sharing transform logic across batch and streaming modes
- managing windowing, watermarks, triggers, and late data handling
- designing portable pipelines that must run across environments

Do not use this when the workload is locked to a single runner and Beam portability is not a goal.

## Workflow

1. Define the pipeline contract and time semantics.
   Include:
   - input PCollections and their bounded or unbounded nature
   - event-time versus processing-time expectations
   - output schema, grain, and freshness requirements
   - delivery guarantees expected by downstream consumers

2. Separate portable pipeline logic from runner-specific deployment.
   - keep transforms, DoFns, and combiners runner-agnostic
   - isolate runner configuration (parallelism, autoscaling, resource hints) into pipeline options
   - document which runners are supported and tested
   - avoid runner-specific APIs unless portability is explicitly sacrificed

3. Design windowing and trigger strategy explicitly.
   Account for:
   - fixed, sliding, session, or global windows
   - trigger behavior: when to emit, accumulate, or discard
   - allowed lateness and late data routing
   - watermark advancement assumptions per source

4. Handle state and side inputs carefully.
   - stateful DoFns bind to a specific key space — document key cardinality
   - side inputs can become bottlenecks at scale — prefer bounded and small
   - timers must account for watermark-driven versus processing-time semantics
   - state cleanup must be explicit for unbounded pipelines

5. Make testing and local validation part of the workflow.
   - use `DirectRunner` for correctness tests
   - validate windowing behavior with synthetic watermark progression
   - test exactly-once semantics through pipeline drains and restarts
   - confirm output idempotency for at-least-once runners

6. Plan deployment, scaling, and operational observability.
   - define autoscaling boundaries and cost limits per runner
   - expose transform-level metrics for latency, throughput, and backlog
   - plan drain and update strategies for streaming pipelines
   - document rollback: can the pipeline be redeployed at an earlier version safely?

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Beam is portable so we don't need to think about runners." | Runner differences in autoscaling, state backends, shuffle behavior, and fusion affect correctness and cost. Testing on a single runner is not proof of portability. |
| "We can use the same pipeline for batch and streaming without changes." | Bounded and unbounded PCollections behave differently with respect to windowing, triggers, and watermarks. Unified does not mean identical. |
| "DirectRunner tests are enough." | DirectRunner does not expose parallelism, shuffle, or scaling issues. Integration tests on the target runner are required for production confidence. |
| "Late data can be handled later." | Late data handling must be part of the initial window and trigger design. Retrofitting allowed lateness after consumers depend on outputs is breaking. |

## Red Flags

- pipeline runs on DirectRunner only and has never been tested on the production runner
- windowing strategy is undefined or uses global windows for unbounded sources
- no documentation of which runners are supported or tested
- stateful DoFns have no key cardinality analysis or state cleanup plan
- pipeline updates require full reprocessing because no drain or savepoint strategy exists
- side inputs are unbounded or grow without limit
- no metrics or observability beyond runner-provided defaults

## Verification

- [ ] Pipeline contract defines inputs, outputs, time semantics, and delivery guarantees
- [ ] Windowing, triggers, and allowed lateness are explicitly designed and tested
- [ ] Runner-specific configuration is isolated from portable transform logic
- [ ] State and side inputs are bounded and have cleanup or eviction plans
- [ ] Pipeline has been tested on the target production runner, not just DirectRunner
- [ ] Drain, update, and rollback strategies are documented
- [ ] Operational metrics cover latency, throughput, backlog, and error rates per transform
