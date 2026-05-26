#!/usr/bin/env bash
set -euo pipefail

echo "Incident mode enabled."
echo
echo "Load these skills first:"
echo "- skills/incident-triage-and-pipeline-recovery/SKILL.md"
echo "- skills/data-observability-and-sla-management/SKILL.md"
echo "- skills/orchestration-and-backfills/SKILL.md"
echo
echo "Use these references and templates:"
echo "- templates/incident-runbook.md"
echo "- references/incident-recovery-checklist.md"
echo "- references/observability-and-sla-checklist.md"
echo
echo "Immediate priorities:"
echo "1. contain bad publishes before broad reruns"
echo "2. preserve evidence before mutation"
echo "3. define the affected window, consumers, and metrics"
echo "4. choose rerun, replay, rollback, or partial correction intentionally"
echo "5. reopen publish only after reconciliation and freshness validation"
