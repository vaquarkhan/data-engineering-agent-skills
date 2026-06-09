# Spec: AWS Serverless Spark MSK Reliability

## Objective

Demonstrate production-grade reliability for an AWS pipeline that combines `MSK` ingestion with timeout-bound Spark batch processing and gated publish.

## Source Systems

- order events from `MSK` topic `order-events`
- optional replay from bounded historical windows

## Destination

- `S3` publish zone `aggregated-events` consumed by analytics and operational dashboards

## Quality Rules

- producer durability uses `acks=all` and idempotence
- schema compatibility is enforced before rollout
- serverless Spark writes to staging only until manifest status is `ready_to_publish`
- replay requires completed `templates/backfill-plan.yaml`
- reconciliation must pass before publish reopen

## Success Criteria

- full batch run produces contract-valid publish output
- simulated timeout resumes without duplicate rows at target grain
- orphan cleanup identifies abandoned staging prefixes
- Kafka and checkpoint configuration is documented and reviewable
