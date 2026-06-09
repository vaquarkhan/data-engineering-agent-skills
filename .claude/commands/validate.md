# /validate

Use validation skills and references to prove the change is safe to publish.

Checklist:

1. load `data-quality-and-contract-testing`
2. add `data-reconciliation-and-financial-controls` when counts or metrics must match
3. add `schema-evolution-and-contract-migrations` for contract or schema changes
4. add `safe-backfill-and-replay-orchestration` when replay or historical repair is in scope
5. add `kafka-resilience-and-schema-evolution` when Kafka schema or durability settings changed
6. add `spark-serverless-reliability-and-state-management` when serverless Spark checkpoint behavior changed
7. gather evidence for quality, freshness, reconciliation, and publish safety
