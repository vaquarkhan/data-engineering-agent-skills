---
name: scala-data-engineering-on-jvm-runtimes
description: Guides agents through Scala-based data engineering on JVM runtimes. Use when building Spark, Flink, Kafka Streams, or other Scala data jobs that require explicit build, packaging, type, and runtime discipline.
---

# Scala Data Engineering On JVM Runtimes

## Overview

Use this skill when `Scala` is the implementation language for distributed or streaming data systems. It helps agents manage build compatibility, packaging, JVM dependency issues, typed data models, serialization behavior, and runtime assumptions that often cause production failures long after code compiles.

## When to Use

- building or modifying `Scala` `Spark` jobs
- implementing `Flink`, `Kafka Streams`, or JVM-native data processors in `Scala`
- managing `sbt` builds, shaded JARs, or runtime compatibility
- choosing typed datasets, encoders, or JVM serialization strategies
- debugging classpath, version, or packaging problems in distributed runtimes

Do not assume compile success means distributed runtime safety.

## Workflow

1. Define the runtime and compatibility surface.
   Include:
   - engine and version
   - `Scala` version
   - JVM level
   - cluster or container runtime
   - connector and library compatibility

2. Shape the data model intentionally.
   Choose:
   - typed case classes or schemas
   - serialization strategy
   - encoder behavior
   - where UDFs are truly needed
   - how nulls and optional fields are represented

3. Package for the real deployment target.
   Decide:
   - `sbt` or other build surface
   - fat-jar or shaded-jar approach
   - dependency conflict handling
   - resource and config loading behavior
   - how the job is launched and parameterized

4. Design for distributed execution, not driver-local convenience.
   Check:
   - partition behavior
   - skew
   - state growth
   - checkpoint or savepoint needs
   - accidental driver-side collection or closure capture

5. Validate with runtime realism.
   Require:
   - representative local or test-cluster execution
   - packaging verification
   - schema and compatibility checks
   - observability and failure handling expectations

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It compiles, so the job is fine." | Distributed classpath, serialization, and dependency issues often appear only at runtime. |
| "We can fix the JAR if deployment fails." | Packaging problems discovered at deploy time slow delivery and often hide deeper compatibility issues. |
| "A quick UDF is simpler." | Overusing UDFs can hide schema, optimizer, and performance problems in JVM data engines. |

## Red Flags

- `Scala`, engine, and connector versions are not pinned together intentionally
- driver-local collections or closures leak into distributed execution
- shading or dependency conflicts are discovered only after deployment
- type or null behavior is unclear across schemas and case classes
- runtime config is embedded in code instead of explicit launch parameters

## Verification

- [ ] Runtime, `Scala`, and library compatibility is explicit
- [ ] Packaging strategy matches the target execution environment
- [ ] Data model and serialization behavior are intentional
- [ ] Distributed execution risks are reviewed beyond compile success
