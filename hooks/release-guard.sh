#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"
shopt -s globstar nullglob

missing=()

has_text() {
  local pattern="$1"
  rg -n -i "$pattern" "$WORKSPACE" >/dev/null 2>&1
}

has_text "rollback|backout|restore|revert|forward-fix" || missing+=("rollback or forward-fix notes")
has_text "shadow|canary|dual-run|dual read|dual-write|staged validation|progressive release" || missing+=("staged validation or progressive-release evidence")
has_text "reconcile|reconciliation|parity|row count|metric parity" || missing+=("reconciliation or parity evidence")
has_text "publish|consumer cutover|visibility toggle|feature flag|dataset swap|view swap" || missing+=("publish separation or consumer-cutover plan")
has_text "monitor|observability|alert|sla|lag|checkpoint|freshness" || missing+=("post-release observability notes")
has_text "owner|approver|approval|oncall|pager" || missing+=("release ownership or approval path")

echo "Release guard for $WORKSPACE"

if [[ ${#missing[@]} -eq 0 ]]; then
  echo "Release evidence looks healthy."
  echo "Safe next step: /ship"
  exit 0
fi

echo "Missing or weak release evidence:"
printf -- '- %s\n' "${missing[@]}"
echo
echo "Before /ship, capture staged validation, publish control, reconciliation, observability, ownership, and rollback evidence."
echo "Starter template: templates/release-gate-evidence.yaml"
exit 1
