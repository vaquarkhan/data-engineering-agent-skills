# CDC Incremental Loading Checklist

Use this checklist when implementing or reviewing incremental pipelines.

## Contract

- [ ] Business key is defined
- [ ] Change ordering field or sequence is defined
- [ ] Delete behavior is documented
- [ ] Duplicate handling is explicit

## Execution

- [ ] Watermark logic is explicit
- [ ] Late-arriving data handling is defined
- [ ] Merge, append, or replace semantics are clear
- [ ] Replay and backfill procedures exist

## Safety

- [ ] Incremental runs are idempotent or safely recoverable
- [ ] Validation exists for missed or duplicate changes
- [ ] Operational state can be inspected when incidents occur
