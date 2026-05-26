---
name: java-data-engineering-and-integration-services
description: Guides agents through Java-based data engineering services and processors. Use when building connectors, ingestion services, stream processors, metadata services, JVM batch tools, or operational integrations in Java.
---

# Java Data Engineering And Integration Services

## Overview

Use this skill when `Java` is the main implementation language for data-adjacent services or processing components. It helps agents design operationally safe JVM services for ingestion, metadata, contracts, stream handling, connectors, and control-plane style data tooling with deliberate resource, dependency, and concurrency management.

## When to Use

- building ingestion or connector services in `Java`
- implementing JVM-based stream processors or integration utilities
- exposing data-platform metadata, contract, or control services
- managing `Maven` or `Gradle` builds for data-related services
- debugging resource, thread, serialization, or connection-pool behavior in JVM services

Do not treat Java services as generic app code when they carry data-delivery, contract, or pipeline semantics.

## Workflow

1. Define the service role and operational boundary.
   Clarify:
   - request or event model
   - upstream and downstream systems
   - throughput and latency expectations
   - delivery guarantees
   - retry and failure behavior

2. Make contracts explicit.
   Include:
   - payload schemas
   - versioning behavior
   - idempotency rules
   - error model
   - compatibility with downstream consumers

3. Design resource and concurrency behavior deliberately.
   Review:
   - thread pools
   - blocking versus async paths
   - connection management
   - backpressure
   - graceful shutdown and restart behavior

4. Package and configure for operations.
   Decide:
   - `Maven` or `Gradle` conventions
   - dependency version strategy
   - environment configuration
   - secrets handling
   - observability and health signals

5. Validate service behavior under realistic load and failure conditions.
   Require:
   - contract checks
   - retry and timeout tests
   - connection and resource sanity
   - release and rollback readiness

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The framework defaults are good enough." | Defaults for thread pools, connection pools, and retries often fail under data-heavy or bursty workloads. |
| "It is just a connector wrapper." | Connectors still define contracts, error handling, retries, and downstream correctness. |
| "Java is verbose but safe by default." | JVM services still fail due to resource leaks, blocking calls, schema drift, and weak operational boundaries. |

## Red Flags

- retry behavior can duplicate writes or downstream side effects
- thread, connection, or shutdown behavior is undocumented
- service config and secrets are embedded in code or build files
- payload compatibility or schema evolution is undefined
- observability is limited to basic process health with no data-path evidence

## Verification

- [ ] The Java service role and delivery semantics are explicit
- [ ] Contract, retry, and idempotency behavior are defined
- [ ] Resource, concurrency, and shutdown behavior are reviewed
- [ ] Build, config, and observability expectations are operationally real
