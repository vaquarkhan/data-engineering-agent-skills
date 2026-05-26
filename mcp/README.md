# MCP Config Templates

This directory contains template MCP configuration files for common data engineering systems.

These are starting points, not vendor-locked binaries. Replace the placeholder commands and environment variables with the MCP server implementation you actually use.

Each template now includes:

- a short purpose description
- service-specific arguments that show intended operating mode
- environment variables beyond the bare minimum so scope and defaults are explicit
- metadata with validation commands and best-fit use cases

## How To Use These Templates

1. Pick the closest template for the service you want the agent to access.
2. Replace the placeholder `command` with the MCP server binary or wrapper script you actually run.
3. Fill the referenced environment variables in your shell, secret manager, or IDE launch configuration.
4. Test the MCP server outside the agent first so connection and auth issues are visible before agent sessions start.

## Common Setup Notes

- `github.mcp.json`
  Set `GITHUB_TOKEN` to a token with the repo scopes you need for pull requests, checks, and issue access.
- `postgres.mcp.json`
  Set `POSTGRES_DSN` to a full DSN such as `postgresql://user:password@host:5432/dbname`.
- `snowflake.mcp.json`
  Set account, user, password, warehouse, database, and role values in the environment expected by your server.
- `bigquery.mcp.json`
  Point the server at a service account key or workload identity configuration with read-only access unless writes are required.
- `databricks.mcp.json`
  Provide host and token values scoped to the workspace and cluster or SQL warehouse the agent should reach.
- `dbt-cloud.mcp.json`
  Use an API token with metadata and job-run access only when the agent truly needs deployment surfaces.
- `airflow.mcp.json`
  Prefer a service account limited to DAG discovery, run state, and task log access.
- `kafka.mcp.json`
  Set bootstrap servers, security protocol, and SASL values if your cluster is not plaintext.
- `terraform.mcp.json`
  Point the server at the Terraform binary and provider credentials already validated in the target environment.
- `slack-jira-incidents.mcp.json`
  Provide tokens that can read incidents and comments without broader workspace admin scopes when possible.

Included templates:

- `github.mcp.json`
- `postgres.mcp.json`
- `snowflake.mcp.json`
- `bigquery.mcp.json`
- `databricks.mcp.json`
- `dbt-cloud.mcp.json`
- `airflow.mcp.json`
- `kafka.mcp.json`
- `terraform.mcp.json`
- `slack-jira-incidents.mcp.json`
