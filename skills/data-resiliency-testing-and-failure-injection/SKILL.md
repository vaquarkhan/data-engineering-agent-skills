---
name: data-resiliency-testing-and-failure-injection
description: Guides agents through resiliency testing for data platforms. Use when designing or running failure drills, recovery validation, failover tests, replay-safety checks, dependency outage exercises, or fault injection for pipelines and publishes.
---

# Data Resiliency Testing And Failure Injection

## Overview

Use this skill when the goal is to prove that a data system recovers safely under failure, not only when everything goes right. It helps agents design controlled drills for retries, restarts, dependency outages, state recovery, duplicate prevention, backlog catch-up, and publish protection.

## When to Use

- hardening a production pipeline before broad rollout
- testing failover, restart, replay, or checkpoint recovery behavior
- validating that retries do not duplicate or corrupt data
- proving recovery objectives for orchestrators, jobs, streams, or warehouse publishes
- converting a past incident into a repeatable resilience drill

Do not treat resilience testing as random breakage. The point is to validate recovery behavior with explicit safety limits and evidence.

## Workflow

1. Define the failure modes that matter.
   Prioritize:
   - source outage or delayed upstream delivery
   - worker or task restart
   - orchestrator retry and timeout behavior
   - duplicate event or duplicate file delivery
   - checkpoint or incremental-state recovery
   - credential, secret, or network dependency failure
   - partial publish or downstream unavailability

2. Define the resilience objectives.
   Include:
   - acceptable data loss behavior
   - recovery time objective
   - replay or backlog catch-up expectation
   - duplicate-prevention requirement
   - publish block or quarantine behavior
   - alert and escalation expectation

3. Choose the safest drill environment.
   Prefer:
   - staging or isolated non-production
   - canary datasets or partitions
   - synthetic or masked test data
   - bounded windows and rollback-ready test scope

4. Inject one failure mode at a time.
   Use controlled exercises such as:
   - killing a task or worker
   - pausing an upstream dependency
   - delaying input arrival
   - replaying a duplicate input
   - forcing an expired secret or denied permission in a safe environment
   - simulating partial output and validating publish closure

5. Validate the recovery path.
   Check:
   - whether the system resumes or fails safely
   - whether alerts fire with useful context
   - whether duplicates are prevented
   - whether backlog catch-up stays bounded
   - whether publish remains blocked until validation passes

6. Record guardrails and automate the highest-value drills.
   The best resilience test is one the team can rerun after changes, not a one-time exercise that gets forgotten.

7. Load companion skills by failure mode.
   - replay or backfill drills: `safe-backfill-and-replay-orchestration`
   - Kafka lag, DLQ, or schema drift: `kafka-resilience-and-schema-evolution`
   - serverless Spark checkpoint recovery: `spark-serverless-reliability-and-state-management`
   - live diagnosis before drills: `mcp-data-observability-integration`
   - drill patterns: `references/data-resiliency-testing-patterns.md`

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "If the job retries, we are resilient enough." | Retry alone does not prove replay safety, duplicate prevention, or publish protection. |
| "We can test recovery during a real incident." | Real incidents are the worst time to discover the recovery path is unclear or unsafe. |
| "Failure injection is too risky for data systems." | Uncontrolled failure is riskier than bounded, reviewable drills in safe environments. |
| "The scheduler health page already proves resilience." | Scheduler status does not prove data correctness, backlog catch-up, or downstream safety. |

## Red Flags

- no list of prioritized failure modes exists
- retries are enabled without idempotency proof
- resilience drills have no rollback or blast-radius limits
- checkpoint or incremental-state recovery has never been tested
- alerts fire but recovery ownership is unclear
- a past incident has no corresponding regression drill

## Verification

- [ ] High-impact failure modes are named and prioritized
- [ ] Recovery objectives and acceptable failure behavior are explicit
- [ ] The drill scope is bounded and safe to run
- [ ] Recovery evidence covers alerts, replay safety, duplicate prevention, and publish protection
- [ ] At least one incident-derived failure mode is turned into a repeatable drill
