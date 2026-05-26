#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"

echo "Schema change guard for $WORKSPACE"
echo

patterns=(
  "drop[[:space:]]+column"
  "rename[[:space:]]+column"
  "alter[[:space:]]+column"
  "replace[[:space:]]+table"
  "truncate[[:space:]]+table"
  "full-refresh"
)

hits=0

for pattern in "${patterns[@]}"; do
  if rg -n -i "$pattern" "$WORKSPACE" >/dev/null 2>&1; then
    echo "Risky pattern detected: $pattern"
    rg -n -i "$pattern" "$WORKSPACE" || true
    hits=1
    echo
  fi
done

if [[ $hits -eq 1 ]]; then
  echo "Breaking or destructive schema signals were found."
  echo "Use these skills before merging:"
  echo "- skills/schema-evolution-and-contract-migrations/SKILL.md"
  echo "- skills/data-contract-testing-with-schema-registry/SKILL.md"
  echo "- skills/data-sharing-and-publishing-contracts/SKILL.md"
  echo "Starter template: templates/schema-change-plan.yaml"
  exit 1
fi

echo "No obvious destructive schema patterns detected."
