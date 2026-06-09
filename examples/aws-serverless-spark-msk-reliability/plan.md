# Plan: AWS Serverless Spark MSK Reliability

## Phase 1: Contracts And Layout

1. Define `contracts/aggregated-events-contract.yaml` at order_id + event_date grain.
2. Document staging, checkpoint, and publish prefixes in `config/checkpoint-layout.yaml`.
3. Document Kafka producer defaults in `config/kafka-producer-settings.yaml`.

## Phase 2: Serverless Batch Proof

1. Implement `jobs/checkpoint_batch_job.py` with manifest-driven resume.
2. Prove full run writes publish output only after manifest gate passes.
3. Simulate timeout via `--fail-after-partitions` and resume with same `run_id`.

## Phase 3: Operations And Replay

1. Add `jobs/orphan_cleanup.py` for abandoned staging detection.
2. Draft replay scope using `templates/backfill-plan.yaml` before any reprocessing.
3. Pair replay work with `skills/safe-backfill-and-replay-orchestration/SKILL.md`.

## Phase 4: Observability

1. Map symptoms to MCP templates using `references/mcp-data-observability-patterns.md`.
2. Capture lag and run-state evidence before proposing consumer or Spark changes.

## Verification

- `make smoke-test` passes locally
- contract validation passes on publish output
- resume path produces identical aggregates to full run
