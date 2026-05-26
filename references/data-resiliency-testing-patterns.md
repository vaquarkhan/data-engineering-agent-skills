# Data Resiliency Testing Patterns

Use this reference when defining failure drills and resilience evidence for data pipelines, batch jobs, streaming systems, publishes, and platform workflows.

## Why This Exists

Many data teams test correctness but do not test recovery. Real systems still fail because:

- retries create duplicates
- backlogs grow faster than recovery can catch up
- checkpoints or incremental state cannot resume cleanly
- publishes reopen before validation completes
- dependency outages turn into partial or stale data without clear containment

Resiliency testing should prove that failure is contained and recovery is safe.

## High-Value Failure Drills

### Task Or Worker Restart

Use when:

- the pipeline retries failed tasks
- workers can be preempted, restarted, or autoscaled
- orchestration retries are normal operations

Validate:

- idempotent writes
- resume point correctness
- duplicate prevention
- useful alert context

### Upstream Delay Or Outage

Use when:

- source feeds arrive late or intermittently
- the pipeline depends on external APIs, files, or CDC connectors
- consumer freshness expectations matter

Validate:

- backlog handling
- delayed-input alerts
- quarantine or wait behavior
- publish blocking for incomplete data

### Duplicate Input Delivery

Use when:

- file drops can be replayed
- events may be delivered more than once
- reruns are part of normal recovery

Validate:

- deduplication strategy
- merge or upsert behavior
- replay-safe metrics
- downstream consumer stability

### Checkpoint Or Incremental-State Recovery

Use when:

- stream processors use checkpoints
- batch jobs track watermarks or incremental cursors
- platform migration or restart can affect state continuity

Validate:

- resume-from-checkpoint behavior
- watermark correctness
- no skipped or double-processed windows
- state compatibility after code changes

### Publish Gate Under Partial Failure

Use when:

- data can load partially while pipeline tasks still appear successful
- publish outputs should remain closed until validation completes
- shared datasets or financial outputs are affected

Validate:

- publish remains blocked
- downstream consumers do not receive partial data
- recovery path includes reconciliation before reopen

### Credential, Secret, Or Access Failure

Use when:

- jobs depend on tokens, secrets, or temporary credentials
- permissions can drift after release
- cross-account or cross-project access is involved

Validate:

- failure is visible and actionable
- secrets rotate or expire without silent bad data
- recovery path is documented

### Backlog Catch-Up Drill

Use when:

- a delayed pipeline must catch up without flooding downstream systems
- large replay windows are realistic
- throughput and partitioning behavior matter operationally

Validate:

- catch-up rate
- concurrency safety
- cost boundaries
- controlled consumer impact

## Pattern By Platform Type

### Batch Pipelines

Prioritize:

- task restart
- duplicate-write prevention
- upstream delay
- publish gate under partial failure

### Streaming Systems

Prioritize:

- duplicate event delivery
- checkpoint recovery
- late-data backlog
- partition skew and replay safety

### Warehouse-Centric Platforms

Prioritize:

- incremental model reruns
- task or scheduler retry safety
- publish blocking and reconciliation
- warehouse concurrency and cost impact during catch-up

### Lakehouse Platforms

Prioritize:

- checkpoint or table-state recovery
- merge idempotency
- stream-to-table replay safety
- medallion-layer publish controls

## Good Test Design Rules

- inject one failure mode at a time
- use bounded time windows and datasets
- prefer synthetic or masked data
- define expected alert, containment, and recovery behavior before the drill
- treat recovery evidence as part of the test result
- convert real incidents into reusable drills

## Anti-Patterns

- random breakage with no hypothesis or safety limit
- only testing infrastructure restart while ignoring data correctness
- declaring success because the scheduler recovered
- skipping publish-block behavior for shared datasets
- running resilience drills with no owner, rollback, or blast-radius control

## Practical Checklist

- [ ] Which failure mode is being tested?
- [ ] What would safe containment look like?
- [ ] What recovery evidence proves success?
- [ ] How do we prove no duplicate or missing publish output?
- [ ] Is the drill repeatable after code or platform changes?
- [ ] Did we update runbooks, hooks, or validation checks from what we learned?

## Recommended Pairings In This Repo

- workflow skill: `skills/data-resiliency-testing-and-failure-injection/SKILL.md`
- observability: `skills/data-observability-and-sla-management/SKILL.md`
- recovery workflow: `skills/incident-triage-and-pipeline-recovery/SKILL.md`
- replay and cutover: `skills/orchestration-and-backfills/SKILL.md`
- test layers: `references/data-testing-patterns.md`
- starter pack: `starter-packs/resiliency-testing-starter.yaml`
