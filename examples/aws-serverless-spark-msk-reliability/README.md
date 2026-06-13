# AWS Serverless Spark MSK Reliability

> **Example type:** Runnable scaffold — local proof path via `make smoke-test` or README commands.

## Scenario

Build an AWS-native pipeline that ingests events from `MSK`, processes them with timeout-bound serverless Spark-style batch jobs, and publishes only after checkpoint manifests and reconciliation gates pass.

## Core Stack

- `MSK` (or `Kafka`-compatible broker)
- `S3` staging, checkpoints, and publish zones
- serverless or short-lived Spark execution (`Glue`, `Lambda`, or local proof harness)
- `MWAA` or event-driven orchestration for gated replay

## Skills To Apply

- `spark-serverless-reliability-and-state-management`
- `kafka-resilience-and-schema-evolution`
- `safe-backfill-and-replay-orchestration`
- `mcp-data-observability-integration`
- `aws-data-engineering`
- `data-reconciliation-and-financial-controls`

## Example Outcome

- Kafka producer settings documented with `acks=all` and idempotence
- staging and checkpoint layout separated from publish paths
- timeout simulation with safe resume and no duplicate publish
- orphan staging detection for abandoned runs
- backfill plan and reconciliation evidence before publish reopen

## Minimal Runnable Scaffold

Files included:

- `Makefile`
- `config/checkpoint-layout.yaml`
- `config/kafka-producer-settings.yaml`
- `contracts/aggregated-events-contract.yaml`
- `data/order-events.jsonl`
- `jobs/checkpoint_batch_job.py`
- `jobs/orphan_cleanup.py`
- `jobs/validate_resume.py`

## Example Commands

```bash
python jobs/checkpoint_batch_job.py --input data/order-events.jsonl --workdir build --run-id run-full
python ../../scripts/validate_dataset_contract.py --contract contracts/aggregated-events-contract.yaml --data build/publish/aggregated-events.jsonl
python jobs/validate_resume.py --input data/order-events.jsonl --workdir build --run-id run-resume --fail-after-partitions 1
python jobs/orphan_cleanup.py --workdir build --older-than-minutes 0 --dry-run
```

Or run the full local proof path:

```bash
make smoke-test
```

## MCP And Production Path

Before production changes:

1. Configure `mcp/kafka.mcp.json` for consumer lag inspection.
2. Configure `mcp/spark.mcp.json` for stage and OOM diagnosis.
3. Complete `templates/backfill-plan.yaml` before any bounded replay.
4. Use `references/kafka-production-guardrails.md` and `references/spark-serverless-reliability-patterns.md` as review checklists.
