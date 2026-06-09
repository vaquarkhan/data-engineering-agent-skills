# Tutorial: Production Reliability And MCP Observability

This tutorial walks through the production reliability skill bundle: safe backfills, serverless Spark state, Kafka guardrails, and MCP-backed diagnosis before mutation.

## Goal

By the end of this tutorial, you should be able to:

- load the production reliability starter pack without over-scoping the agent
- draft a backfill plan before any replay execution
- apply serverless Spark checkpoint and rollback patterns
- enforce Kafka producer and schema guardrails
- query live signals through MCP templates before proposing fixes

## Step 1: Load The Production Reliability Bundle

Start with:

- `starter-packs/production-reliability-starter.yaml`
- `skills/using-data-engineering-agent-skills/SKILL.md`

Core skills in the bundle:

- `safe-backfill-and-replay-orchestration`
- `spark-serverless-reliability-and-state-management`
- `kafka-resilience-and-schema-evolution`
- `mcp-data-observability-integration`

Supporting templates and references:

- `templates/backfill-plan.yaml`
- `templates/incident-runbook.md`
- `templates/release-gate-evidence.yaml`
- `references/spark-serverless-reliability-patterns.md`
- `references/kafka-production-guardrails.md`
- `references/mcp-data-observability-patterns.md`

MCP templates to configure read-only:

- `mcp/spark.mcp.json`
- `mcp/kafka.mcp.json`
- `mcp/airflow.mcp.json`

## Step 2: Diagnose Before Mutation With MCP

When lag rises, a Spark stage fails, or a DAG turns red:

1. Pick the smallest MCP template from `references/mcp-data-observability-patterns.md`.
2. Validate connectivity outside the agent session using `mcp/README.md`.
3. Capture evidence: consumer lag per partition, failed task logs, or Spark stage skew.
4. Only then propose code, infra, or replay changes.

Load `skills/mcp-data-observability-integration/SKILL.md` for the full diagnostic sequence.

## Step 3: Run A Safe Backfill With `/backfill`

Never execute wide replay without a written plan.

1. Run `hooks/backfill-guard.sh` or `hooks/backfill-guard.ps1`.
2. Load `skills/safe-backfill-and-replay-orchestration/SKILL.md`.
3. Complete `templates/backfill-plan.yaml` with owner, window, rollback, and reconciliation gates.
4. Pause publish and notify downstream owners.
5. Prove on a single partition or day before expanding the window.
6. Reopen publish only after reconciliation passes.

Pair with:

- `skills/orchestration-and-backfills/SKILL.md` for schedule and dependency semantics
- `skills/data-reconciliation-and-financial-controls/SKILL.md` when metrics must match
- `skills/data-migration-and-platform-cutover/SKILL.md` for dual-run cutovers

Walkthrough example: `case-studies/replay-safe-backfill-after-corruption.md`

## Step 4: Harden Serverless Spark State

For `AWS Lambda`, serverless `Glue`, or any Spark job with hard runtime ceilings:

1. Load `skills/spark-serverless-reliability-and-state-management/SKILL.md`.
2. Separate staging prefixes from publish paths.
3. Write checkpoint manifests with `run_id`, partition progress, and status.
4. Implement timeout rollback that quarantines incomplete staging output.
5. Schedule orphan cleanup for abandoned prefixes.

Reference: `references/spark-serverless-reliability-patterns.md`

Runnable proof: `examples/aws-serverless-spark-msk-reliability/`

## Step 5: Enforce Kafka Production Guardrails

Before changing topics, producers, or schemas:

1. Load `skills/kafka-resilience-and-schema-evolution/SKILL.md`.
2. Require `acks=all` and idempotent producers unless a named owner documents a waiver.
3. Set schema compatibility per subject — not `NONE` in production.
4. Mandate DLQ routing for deserialization and schema failures.
5. Inspect consumer lag with `mcp/kafka.mcp.json` before offset resets or replay.

Reference: `references/kafka-production-guardrails.md`

## Step 6: Pair With The Kafka Flink Example

Use `examples/kafka-flink-streaming/` to practice:

- replay-safe sink validation
- checkpoint recovery
- contract checks on windowed output

Apply the production reliability skills on top of that example when moving from local proof to production hardening.

## Step 7: Review And Ship With Evidence

Before `/ship`:

- load `agents/data-platform-reliability-reviewer.md`
- confirm backfill or replay evidence exists when historical repair was involved
- confirm MCP findings were captured when diagnosis drove the change
- record release evidence in `templates/release-gate-evidence.yaml`

## Red Flags

Stop and rework if:

- replay starts without `templates/backfill-plan.yaml`
- agents propose cluster scaling before reading Spark stage evidence
- Kafka schema changes ship without compatibility CI
- MCP credentials are write-capable by default
- publish reopens before reconciliation gates pass

## Next Steps

- `tutorials/streaming-architecture-patterns.md` for broader event design
- `tutorials/data-resiliency-testing-patterns.md` for turning incidents into drills
- `examples/aws-serverless-spark-msk-reliability/` for AWS serverless + MSK proof path
