# /ship

Use release and operational workflows before publish:

- `data-platform-ci-cd-and-release-management`
- `data-sharing-and-publishing-contracts`
- `data-observability-and-sla-management`
- `mcp-data-observability-integration` for post-release lag, freshness, and run-state checks
- `bash hooks/release-guard.sh` for pre-flight release evidence

Do not treat deployment and publish as the same step unless the workflow explicitly allows it.

For replay-bound releases, confirm `templates/backfill-plan.yaml` and reconciliation evidence exist before publish reopen.
