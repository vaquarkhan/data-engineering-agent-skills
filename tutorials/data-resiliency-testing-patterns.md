# Tutorial: Running Data Resiliency Testing

This tutorial explains how to design and run resilience drills for data platforms so recovery behavior is proven before a real incident forces the test.

## Goal

By the end of this tutorial, you should be able to:

- choose the highest-value failure modes to test
- design bounded resilience drills for batch, streaming, warehouse, and lakehouse systems
- validate restart, retry, replay, checkpoint, backlog, and partial-publish behavior
- turn incidents into repeatable resilience tests

## Step 1: Start With The Failure Modes That Matter

Choose failure modes that are both realistic and operationally important:

- task or worker restart
- upstream outage or late delivery
- duplicate input delivery
- checkpoint or incremental-state recovery
- partial publish
- secret, credential, or access failure
- backlog catch-up after delay

Use `references/data-resiliency-testing-patterns.md` as the main guide.

## Step 2: Define What Success Looks Like

For each drill, define:

- expected alert behavior
- expected containment behavior
- whether publish should stay blocked
- how duplicate or missing output will be prevented
- how long recovery or catch-up is allowed to take

If these expectations are not written down first, the drill will not produce useful evidence.

## Step 3: Choose The Safest Drill Scope

Prefer:

- staging or isolated non-production
- synthetic or masked datasets
- bounded partitions or small time windows
- rollback-ready changes and named owners

Avoid broad unsupervised breakage. The goal is controlled proof, not surprise.

## Step 4: Pick The Pattern By Platform Type

### Batch Pipelines

Prioritize:

- task restart
- duplicate-write prevention
- upstream delay handling
- publish blocking for incomplete loads

### Streaming Systems

Prioritize:

- duplicate event delivery
- checkpoint recovery
- late-data backlog
- replay-safe sinks

### Warehouse-Centric Platforms

Prioritize:

- incremental reruns
- scheduler retry safety
- partial publish and reconciliation behavior
- concurrency or cost impact during catch-up

### Lakehouse Platforms

Prioritize:

- checkpoint or table-state recovery
- merge idempotency
- stream-to-table replay safety
- publish controls between bronze, silver, and gold outputs

## Step 5: Pair The Drill With The Right Skills

Load:

- `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- `skills/safe-backfill-and-replay-orchestration/SKILL.md`
- `skills/mcp-data-observability-integration/SKILL.md`
- `skills/data-observability-and-sla-management/SKILL.md`
- `skills/incident-triage-and-pipeline-recovery/SKILL.md`
- `skills/orchestration-and-backfills/SKILL.md`

Use:

- `templates/incident-runbook.md`
- `templates/backfill-plan.yaml`
- `templates/release-gate-evidence.yaml`

This ensures the drill covers operations, replay, and publish controls together.

## Step 6: Run One Failure Mode At A Time

Examples:

- kill one worker and verify restart behavior
- delay an upstream feed and observe freshness and backlog controls
- replay a duplicate file or event and confirm deduplication
- simulate a broken secret and validate alert routing
- force partial output and confirm publish remains closed

Do not combine several failure modes into one test unless the single-mode behavior is already well understood.

## Step 7: Capture The Evidence

A good resilience result should include:

- the failure mode tested
- the drill scope
- the expected versus actual recovery behavior
- alert evidence
- duplicate or missing-output proof
- any guardrails added afterward

Without written evidence, resilience testing becomes folklore instead of a repeatable control.

## Step 8: Convert Incidents Into Regression Drills

After a real incident:

1. summarize the failure mode
2. identify the missing control
3. add or update a resilience drill
4. connect it to the runbook or validation path

The same incident should not surprise the team twice.

## Recommended Reading

- `references/data-resiliency-testing-patterns.md`
- `references/data-testing-patterns.md`
- `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- `skills/incident-triage-and-pipeline-recovery/SKILL.md`
