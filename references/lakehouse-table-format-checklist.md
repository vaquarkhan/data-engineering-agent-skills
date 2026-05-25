# Lakehouse Table Format Checklist

Use this checklist when selecting or operating `Iceberg`, `Delta`, or `Hudi` tables.

## Table Design

- [ ] Grain and keys are explicit
- [ ] Read and write patterns are known
- [ ] Mutation model is defined
- [ ] Partition strategy is documented

## Lifecycle

- [ ] Snapshot retention policy exists
- [ ] Compaction or file maintenance is planned
- [ ] Schema evolution expectations are documented
- [ ] Cross-engine compatibility is understood

## Operations

- [ ] Batch and stream writers are coordinated
- [ ] Recovery behavior is documented
- [ ] Cleanup and maintenance jobs are planned
- [ ] Publish contracts are validated before downstream use
