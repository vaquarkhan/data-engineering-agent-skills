# Data Engineering Anti-Patterns

Use this reference when reviewing a design, migration, pipeline, or operational change for common failure modes that look convenient early and expensive later.

## Validation Anti-Patterns

- treating "the job succeeded" as proof the data is correct
- testing only happy-path samples
- fixing incidents without first reproducing them as a failing check
- skipping replay or rerun tests for pipelines that will be rerun in production

## Modeling And Storage Anti-Patterns

- mixed-grain tables presented as a single clean dataset
- choosing `MySQL` or `NoSQL` by trend instead of access-pattern fit
- using a warehouse or lakehouse as an operational request store
- using a cache as the only source of truth

## Pipeline Design Anti-Patterns

- one giant DAG or monolithic job with many unrelated business responsibilities
- hidden manual steps outside version control
- duplicated transformation logic across ETL, Spark, warehouse SQL, and BI layers
- publish and deploy coupled with no staged validation

## Governance And Security Anti-Patterns

- copying production data into lower environments without masking strategy
- documenting security controls without implementing them in platform config or code
- lineage that stops before shared extracts, dashboards, or reverse-ETL destinations
- relying on a global policy while ignoring country or sector-specific obligations

## Operations Anti-Patterns

- "we can always backfill later" as a design strategy
- indefinite dual-run paths with no retirement plan
- rollback mentioned but not operationally executable
- alerting on pipeline failure only, not on bad-data behavior

## Healthy Counter-Patterns

- validate contracts, quality, and replay behavior before publish
- keep execution units small enough to reason about and recover
- choose storage based on workload fit and operational trade-offs
- treat security, lineage, and regional compliance as implementation concerns
- define cutover, rollback, and retirement plans before modernization starts
