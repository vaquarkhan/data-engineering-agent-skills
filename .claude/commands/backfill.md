# /backfill

Use replay-safe workflows before rerunning, replaying, or cutting over data.

Checklist:

1. load `orchestration-and-backfills`
2. load `data-migration-and-platform-cutover` for cutovers or dual-run changes
3. load `data-reconciliation-and-financial-controls` when correctness must be proven after replay
4. define the affected window, rollback path, and reconciliation gates before execution
