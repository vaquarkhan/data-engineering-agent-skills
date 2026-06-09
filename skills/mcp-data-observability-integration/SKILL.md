---
name: mcp-data-observability-integration
description: Guides agents to wire Model Context Protocol servers for live data platform observability including Spark execution plans, OOM diagnosis, Kafka consumer lag, and orchestration run state. Use when agents need cluster metrics, streaming lag, or job diagnostics instead of blind code changes.
---

# MCP Data Observability Integration

## Overview

Agents that cannot see production signals guess at fixes — scaling clusters blindly, rerunning jobs that OOM for structural reasons, or changing Kafka consumers without checking lag. This skill pairs MCP server templates with safe read-only observability workflows so diagnosis precedes mutation.

## When to Use

- diagnosing Spark OOM, shuffle skew, or stage failures
- inspecting Kafka consumer group lag before replay or consumer changes
- reviewing Airflow DAG run state, task duration drift, or failed retries
- validating warehouse publish state before reopening downstream consumers
- setting up IDE-integrated observability for data engineering agents

Do not use MCP write capabilities for destructive fixes during incident triage unless explicitly approved and scoped.

## Workflow

1. Choose the smallest MCP surface for the question.
   - Spark plans and stage metrics: `mcp/spark.mcp.json` or `mcp/databricks.mcp.json`
   - Kafka lag and topic metadata: `mcp/kafka.mcp.json`
   - Orchestration run state: `mcp/airflow.mcp.json`
   - Warehouse inspection: `mcp/snowflake.mcp.json`, `mcp/bigquery.mcp.json`, or `mcp/postgres.mcp.json`
   - Release and job metadata: `mcp/dbt-cloud.mcp.json`, `mcp/github.mcp.json`

2. Configure read-only first.
   From `mcp/README.md`:
   - replace placeholder `command` with the MCP server binary in use
   - scope credentials to read-only inspection roles
   - set allowlists (`topic`, catalog, schema) to minimum necessary scope
   - validate connectivity outside the agent session before relying on tool output

3. Establish the diagnostic sequence.
   Typical order:
   - confirm symptom (lag, failure rate, freshness breach)
   - pull live metadata (consumer lag, last successful run, stage skew)
   - compare against baseline or SLA from `data-observability-and-sla-management`
   - form hypothesis before proposing code or infra changes
   - record findings in incident or backfill evidence templates when action follows

4. Apply platform-specific investigation patterns.
   - **Spark OOM or timeout**: inspect stage breakdown, shuffle read/write bytes, spill metrics, and partition counts; prefer physical plan fixes over blind scale-up
   - **Kafka lag**: inspect group lag per partition, DLQ rate, and retention headroom; pause replay until lag root cause is classified
   - **Orchestration failures**: inspect task logs, retry history, and upstream sensors; do not trigger wide backfills from a single red task without plan gates

   Load `references/mcp-data-observability-patterns.md` for tool-to-symptom mapping.

5. Pair observability with safety skills.
   - replay or repair: `safe-backfill-and-replay-orchestration`
   - streaming hardening: `kafka-resilience-and-schema-evolution`
   - serverless Spark: `spark-serverless-reliability-and-state-management`
   - incident response: `incident-triage-and-pipeline-recovery`

6. Close the loop after changes.
   Re-query MCP signals to confirm lag recovery, run success, or freshness restoration before publish reopen.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We can infer the problem from logs alone." | Logs without lag, plan, and run metadata miss systemic causes like skew and consumer stall. |
| "MCP access should use admin credentials for speed." | Over-scoped tokens increase blast radius when agents suggest broad changes. |
| "Observability is only for on-call humans." | Agents without live signals replicate dangerous guesswork at machine speed. |
| "One MCP server is enough for every stack." | Multi-platform estates need focused templates per system, not one mega-connection. |

## Red Flags

- agents propose infra or code changes without querying live signals
- MCP templates use write-capable credentials by default
- no allowlists on Kafka topics or warehouse schemas
- lag or run failure is acknowledged but not tied to an owner or SLA
- observability findings are not linked to backfill or incident evidence

## Verification

- [ ] The correct MCP template is selected and validated read-only
- [ ] Live signals were queried before structural changes were proposed
- [ ] Findings map to a named safety skill when replay or publish is involved
- [ ] Post-change signals confirm recovery before publish reopen
