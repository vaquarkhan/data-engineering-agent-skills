# /backfill

Use replay-safe workflows before rerunning, replaying, or cutting over data.

Checklist:

1. load `safe-backfill-and-replay-orchestration` first — draft `templates/backfill-plan.yaml` before any execution
2. run `hooks/backfill-guard.sh` or `hooks/backfill-guard.ps1` when available
3. load `orchestration-and-backfills` for schedule, retry, and dependency semantics
4. load `data-migration-and-platform-cutover` for cutovers or dual-run changes
5. load `data-reconciliation-and-financial-controls` when correctness must be proven after replay
6. load `mcp-data-observability-integration` when live lag or run state should inform the replay window
7. define the affected window, rollback path, and reconciliation gates before execution
