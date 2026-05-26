#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"
shopt -s globstar nullglob

contract_files=(
  "$WORKSPACE"/**/*contract*.yaml
  "$WORKSPACE"/**/*contract*.yml
  "$WORKSPACE"/contracts/**/*.yaml
  "$WORKSPACE"/contracts/**/*.yml
)

unique_files=()
for file in "${contract_files[@]}"; do
  [[ -f "$file" ]] || continue
  unique_files+=("$file")
done

if [[ ${#unique_files[@]} -eq 0 ]]; then
  echo "No contract files found."
  echo "Create one from templates/source-contract.yaml, templates/dataset-contract.yaml, or templates/metric-contract.yaml before planning or build work."
  exit 1
fi

errors=0

check_key() {
  local file="$1"
  local key="$2"
  if ! rg -n "^[[:space:]]*$key:" "$file" >/dev/null 2>&1; then
    echo "Missing required key '$key' in $file"
    errors=$((errors + 1))
  fi
}

for file in "${unique_files[@]}"; do
  echo "Checking $file"

  if rg -n "^[[:space:]]*source_contract:" "$file" >/dev/null 2>&1; then
    check_key "$file" "name"
    check_key "$file" "owner"
    check_key "$file" "cadence"
    check_key "$file" "schema"
    check_key "$file" "quality"
    check_key "$file" "security"
  elif rg -n "^[[:space:]]*dataset_contract:" "$file" >/dev/null 2>&1; then
    check_key "$file" "name"
    check_key "$file" "owner"
    check_key "$file" "grain"
    check_key "$file" "schema"
    check_key "$file" "freshness"
    check_key "$file" "quality"
    check_key "$file" "compatibility"
  elif rg -n "^[[:space:]]*metric_contract:" "$file" >/dev/null 2>&1; then
    check_key "$file" "name"
    check_key "$file" "owner"
    check_key "$file" "definition"
    check_key "$file" "freshness"
    check_key "$file" "quality"
    check_key "$file" "compatibility"
  else
    echo "Could not identify contract type for $file"
    echo "Expected one of: source_contract, dataset_contract, metric_contract"
    errors=$((errors + 1))
  fi
done

if [[ $errors -gt 0 ]]; then
  echo
  echo "Contract validation failed with $errors issue(s)."
  echo "Use /spec to define missing ownership, schema, freshness, quality, and compatibility details before implementation."
  exit 1
fi

echo
echo "Contract validation passed."
echo "Safe next step: /plan or /build if the contract is approved."
