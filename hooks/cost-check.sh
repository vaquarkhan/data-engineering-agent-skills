#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"

echo "Cost check for $WORKSPACE"
echo

warnings=0

check_pattern() {
  local label="$1"
  local pattern="$2"
  if rg -n -i "$pattern" "$WORKSPACE" >/dev/null 2>&1; then
    echo "Potential cost hotspot: $label"
    rg -n -i "$pattern" "$WORKSPACE" || true
    echo
    warnings=1
  fi
}

check_pattern "SELECT * in SQL models" "select[[:space:]]+\*"
check_pattern "cross joins" "cross[[:space:]]+join"
check_pattern "destructive dbt full refresh usage" "dbt[[:space:]]+run.*full-refresh|full-refresh"
check_pattern "Spark repartition or coalesce usage" "repartition\(|coalesce\("
check_pattern "explode-heavy transformations" "explode\("
check_pattern "missing incremental hints" "materialized:[[:space:]]*incremental|is_incremental\("

if [[ $warnings -eq 1 ]]; then
  echo "Review these skills before shipping:"
  echo "- skills/warehouse-performance-and-cost-optimization/SKILL.md"
  echo "- skills/spark-and-distributed-processing/SKILL.md"
  echo "- skills/data-observability-and-sla-management/SKILL.md"
  exit 1
fi

echo "No obvious high-cost patterns were detected."
