# MCP Data Observability Patterns

Use this reference to map symptoms to the smallest useful MCP template before agents propose pipeline mutations.

## Symptom To MCP Template

| Symptom | Start with | Inspect |
| --- | --- | --- |
| Spark OOM or stage failure | `mcp/spark.mcp.json` or `mcp/databricks.mcp.json` | stage list, shuffle bytes, spill, task duration skew |
| Kafka consumer falling behind | `mcp/kafka.mcp.json` | group lag per partition, topic retention, DLQ rate |
| DAG red but root cause unclear | `mcp/airflow.mcp.json` | failed task logs, upstream sensor state, retry count |
| Warehouse freshness breach | `mcp/snowflake.mcp.json`, `mcp/bigquery.mcp.json`, or `mcp/postgres.mcp.json` | last load timestamp, row counts, blocking locks |
| Release regression after dbt deploy | `mcp/dbt-cloud.mcp.json` + `mcp/github.mcp.json` | job run result, test failures, changed models |

## Read-Only Setup Checklist

1. Pick template from `mcp/`.
2. Replace placeholder `command` with your MCP server binary.
3. Scope credentials to read-only roles.
4. Set allowlists for topics, catalogs, or repos.
5. Run template `metadata.validation` commands manually.
6. Only then attach MCP to the agent session.

## Investigation Order

1. Confirm the SLA or symptom (`data-observability-and-sla-management`).
2. Pull live metadata via MCP.
3. Classify: infra, code, data volume, contract, or consumer stall.
4. Choose safety skill before mutation:
   - replay -> `safe-backfill-and-replay-orchestration`
   - streaming -> `kafka-resilience-and-schema-evolution`
   - serverless Spark -> `spark-serverless-reliability-and-state-management`
   - active incident -> `incident-triage-and-pipeline-recovery`
5. Re-query MCP after fix to close the loop.

## Anti-Patterns

- using admin warehouse credentials in IDE MCP config
- triggering backfill because a single Airflow task is red without log review
- scaling Spark clusters before reading shuffle skew evidence
- closing incidents without capturing MCP findings in runbooks or backfill evidence
