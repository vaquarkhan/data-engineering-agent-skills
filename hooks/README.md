# Data Engineering Hooks

This directory contains lightweight operational hooks that make the repository feel more like a workflow system than a static library.

The hook logic now lives in `scripts/hook_runner.py` so the same checks can run from bash, PowerShell, CI, or plugin hook systems without depending on `rg`.

## Included Hooks

- `session-start.sh`  
  Detects likely repo type and recommends the right preset, starter pack, example, and next command.
- `contract-check-pre.sh`  
  Validates that contract files contain the minimum fields expected before planning or implementation.
- `pipeline-review-pre.sh`  
  Checks for basic delivery evidence such as tests, contracts, rollback notes, lineage, and quality gates.
- `incident-mode.sh`  
  Switches the session into incident-response posture and points the agent to the right skills and runbook.
- `backfill-guard.sh`  
  Adds safety questions and validation gates before replay, rerun, or cutover work.
- `schema-change-guard.sh`  
  Detects risky schema evolution patterns like breaking renames, drops, and destructive refreshes.
- `cost-check.sh`  
  Flags likely cost hotspots in SQL, dbt, Spark, and warehouse-oriented projects.
- `release-guard.sh`  
  Checks whether staged validation, reconciliation, publish control, observability, and rollback evidence exist before `/ship`.

## Usage

Run any hook from the repository root:

```bash
bash hooks/session-start.sh
bash hooks/contract-check-pre.sh
bash hooks/schema-change-guard.sh
bash hooks/release-guard.sh
```

PowerShell equivalents are also included:

```powershell
pwsh hooks/session-start.ps1
pwsh hooks/contract-check-pre.ps1
pwsh hooks/schema-change-guard.ps1
pwsh hooks/release-guard.ps1
```

All hooks accept an optional workspace path:

```bash
bash hooks/cost-check.sh /path/to/project
```

## Suggested Lifecycle Mapping

- session start: `session-start.sh`
- before `/plan` or `/build`: `contract-check-pre.sh`
- before `/review` or `/ship`: `pipeline-review-pre.sh`
- before replay or cutover work: `backfill-guard.sh`
- before contract or schema updates: `schema-change-guard.sh`
- before cost-sensitive changes are merged: `cost-check.sh`
- before `/ship` or release approval: `release-guard.sh`
- during incident response: `incident-mode.sh`

## Notes

- Hooks are advisory by default and print actionable next steps.
- Hooks that detect clearly risky states return a non-zero exit code.
- The `hooks.json` file provides a starter Claude-style hook mapping for session start.
- Use `templates/backfill-plan.yaml`, `templates/schema-change-plan.yaml`, and `templates/release-gate-evidence.yaml` when you want the hook advice to become structured evidence.
- `session-start` avoids broad self-matching when run inside this repository so documentation keywords do not overwhelm real stack detection.
