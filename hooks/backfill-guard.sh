#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"

echo "Backfill guard for $WORKSPACE"
echo
echo "Answer these before replay or cutover work:"
echo "- what exact time window or partition range is affected?"
echo "- is the job idempotent and safe to rerun?"
echo "- which downstream datasets, dashboards, and SLAs will move?"
echo "- what metric reconciliation proves the replay is correct?"
echo "- what is the rollback or re-close strategy if the replay is wrong?"
echo

missing=0

if ! rg -n -i "backfill|replay|rerun|cutover|reconcile|rollback" "$WORKSPACE" >/dev/null 2>&1; then
  echo "No replay or rollback notes were found in the workspace."
  missing=1
fi

if ! rg -n -i "time window|partition|date range|affected window" "$WORKSPACE" >/dev/null 2>&1; then
  echo "No affected window or partition range was found."
  missing=1
fi

if ! rg -n -i "reconcile|reconciliation|row count|metric" "$WORKSPACE" >/dev/null 2>&1; then
  echo "No reconciliation evidence was found."
  missing=1
fi

echo
echo "Recommended skills:"
echo "- skills/orchestration-and-backfills/SKILL.md"
echo "- skills/data-migration-and-platform-cutover/SKILL.md"
echo "- skills/data-reconciliation-and-financial-controls/SKILL.md"
echo "Starter template: templates/backfill-plan.yaml"

if [[ $missing -ne 0 ]]; then
  echo
  echo "Backfill guard failed. Capture the missing replay details before execution."
  exit 1
fi

echo
echo "Backfill guard passed."
