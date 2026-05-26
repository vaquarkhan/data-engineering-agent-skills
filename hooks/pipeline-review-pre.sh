#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"
shopt -s globstar nullglob

missing=()

has_any() {
  local pattern="$1"
  local matches=("$WORKSPACE"/$pattern)
  [[ ${#matches[@]} -gt 0 ]]
}

has_text() {
  local pattern="$1"
  rg -n -i "$pattern" "$WORKSPACE" >/dev/null 2>&1
}

has_any "tests/**/*" || has_any "test/**/*" || has_any "**/*test*.py" || has_any "**/*test*.sql" || missing+=("tests or validation queries")
has_any "**/*contract*.yaml" || has_any "**/*contract*.yml" || missing+=("contract artifacts")
has_text "lineage|openlineage|datahub|openmetadata|upstream|downstream" || missing+=("lineage notes or metadata wiring")
has_text "rollback|backout|restore|revert" || missing+=("rollback or recovery notes")
has_text "owner|ownership|oncall|pager" || missing+=("ownership or escalation notes")
has_text "quality|reconcile|reconciliation|not_null|unique|freshness" || missing+=("quality gates or reconciliation evidence")

echo "Pipeline review pre-check for $WORKSPACE"

if [[ ${#missing[@]} -eq 0 ]]; then
  echo "Pre-review evidence looks healthy."
  echo "Safe next step: /review"
  exit 0
fi

echo "Missing or weak review evidence:"
printf -- '- %s\n' "${missing[@]}"
echo
echo "Before /review or /ship, add evidence for reliability, lineage, quality, ownership, and rollback."
exit 1
