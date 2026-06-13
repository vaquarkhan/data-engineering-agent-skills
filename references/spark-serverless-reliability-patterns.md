# Spark Serverless Reliability Patterns

Use this reference when Spark runs under hard time or memory ceilings — `AWS Lambda`, serverless `Glue`, or similar — and silent partial failure is unacceptable.

## Staging And Publish Separation

Write to a staging prefix first. Open publish only after a manifest proves completeness.

```text
s3://lake/staging/{dataset}/{run_id}/partitions/...
s3://lake/publish/{dataset}/...          # promoted only after gate passes
s3://lake/checkpoints/{dataset}/{run_id}/manifest.json
```

Watch for:

- agents writing directly to publish paths
- manifests that list partitions without byte or row checksums when contracts require them
- concurrent runs sharing the same staging prefix without run id isolation

## Checkpoint Manifest

Minimum manifest fields:

- `run_id`, `started_at`, `updated_at`
- `partition_range` or `offset_range`
- `completed_partitions` list
- `status`: `in_progress`, `rolled_back`, `ready_to_publish`
- `staging_prefix` and `target_relation`

Resume logic must read manifest status before continuing — never assume empty staging means a fresh run.

## Timeout-Aware Rollback

Before the runtime ceiling:

1. Flush in-flight writes to staging only.
2. Mark manifest `rolled_back` with last completed partition.
3. Delete or quarantine incomplete staging objects for the current run id.
4. Block orchestration from opening publish sensors.

## Orphan Detection

Schedule a janitor job or hook that:

- lists staging and checkpoint prefixes older than the SLA window
- excludes prefixes with `in_progress` heartbeats newer than N minutes
- alerts before deletion when ambiguity exists
- records cleanup actions for audit

## IceGuard-Style Translation

When adapting checkpoint libraries such as IceGuard:

- map library checkpoint keys to orchestration `run_id`
- expose rollback hooks to the agent workflow, not only application code
- prove resume on a single partition before wide replay
- pair with `safe-backfill-and-replay-orchestration` when recomputation spans historical windows
