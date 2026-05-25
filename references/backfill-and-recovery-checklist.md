# Backfill And Recovery Checklist

Use this checklist before historical reprocessing or major orchestration changes.

## Before Execution

- [ ] The reprocessing window is explicitly bounded
- [ ] Idempotency behavior is known
- [ ] Duplicate prevention is in place
- [ ] Cost and concurrency impact are estimated
- [ ] Downstream consumers are aware of replay effects

## During Execution

- [ ] Progress can be monitored
- [ ] Partial failures can be isolated
- [ ] A stop or pause procedure is defined
- [ ] Publish gating exists where needed

## After Execution

- [ ] Row counts or business totals are reconciled
- [ ] Failed partitions or windows are identified
- [ ] Recovery notes are updated
- [ ] Any temporary controls are removed
