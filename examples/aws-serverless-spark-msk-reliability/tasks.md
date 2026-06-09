# Tasks: AWS Serverless Spark MSK Reliability

## Setup

- [ ] Review `config/checkpoint-layout.yaml` and align prefixes with your `S3` bucket layout
- [ ] Review `config/kafka-producer-settings.yaml` against your `MSK` cluster policy
- [ ] Load `starter-packs/production-reliability-starter.yaml`

## Build

- [ ] Run full batch: `python jobs/checkpoint_batch_job.py --input data/order-events.jsonl --workdir build --run-id run-full`
- [ ] Validate contract on publish output
- [ ] Run timeout resume proof: `python jobs/validate_resume.py --input data/order-events.jsonl --workdir build --run-id run-resume --fail-after-partitions 1`

## Operate

- [ ] Dry-run orphan cleanup: `python jobs/orphan_cleanup.py --workdir build --older-than-minutes 0 --dry-run`
- [ ] Draft `templates/backfill-plan.yaml` for a sample replay window
- [ ] Configure read-only `mcp/kafka.mcp.json` and `mcp/spark.mcp.json` for your environment

## Release

- [ ] Run `agents/data-platform-reliability-reviewer.md` checklist
- [ ] Record evidence in `templates/release-gate-evidence.yaml` before publish reopen
