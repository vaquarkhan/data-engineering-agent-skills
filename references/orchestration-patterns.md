# Agent Composition And Entry Patterns

Use this reference when deciding how skills, personas, commands, hooks, and parallel reviews in this repository should work together. For data-pipeline scheduler and cloud orchestration choices, use `references/pipeline-orchestration-patterns.md`.

## Why This Exists

This repository has several different layers:

- `skills/` define the workflow
- `agents/` define a viewpoint or reviewer role
- commands such as `/spec` and `/review` are entry points
- `hooks/` are pre-flight or session-start guardrails

These layers should not compete with each other.

## Composition Model

### Skill

A skill is the step-by-step workflow.

Examples:

- `data-specification`
- `dbt-and-analytics-engineering`
- `incident-triage-and-pipeline-recovery`

Use a skill when you need the agent to follow a repeatable process.

### Persona

A persona is a single point of view with a specific review role.

Examples:

- `analytics-engineer-reviewer`
- `data-platform-reliability-reviewer`
- `data-security-and-compliance-auditor`

Use a persona when you want a specific lens on the current work.

### Command

A command is the user-facing entry point.

Examples:

- `/spec`
- `/validate`
- `/review`
- `/ship`

Use a command when the user should not have to remember the exact skill bundle.

### Hook

A hook is a lightweight pre-flight or session-start check.

Examples:

- `session-start.sh`
- `schema-change-guard.sh`
- `backfill-guard.sh`

Use a hook when you want to detect risky states or route the session before the main workflow begins.

## Recommended Patterns

### Direct Skill Invocation

Use when the task is clear and the main need is workflow discipline.

Examples:

- contract definition -> `data-specification`
- schema migration -> `schema-evolution-and-contract-migrations`
- replay work -> `safe-backfill-and-replay-orchestration` + `orchestration-and-backfills`

### Direct Persona Invocation

Use when the task is a review from one perspective.

Examples:

- review metric logic -> `analytics-engineer-reviewer`
- review replay safety -> `data-platform-reliability-reviewer`
- review regulated-data handling -> `data-security-and-compliance-auditor`

### Command-Led Sequential Flow

Use when the work depends on ordering.

Recommended sequence:

```text
/spec -> /plan -> /build -> /validate -> /review -> /ship
```

This is the default pattern for most non-trivial changes.

### Command-Led Parallel Review

Use this only when the investigations are genuinely independent.

Good pattern:

```text
/ship
  ├── analytics-engineer-reviewer
  ├── data-platform-reliability-reviewer
  └── data-security-and-compliance-auditor
```

Why this works:

- each reviewer uses a different perspective
- they can inspect the same change independently
- the merge step is small and can stay in the main session

## Anti-Patterns

### Persona And Skill Duplication

Bad pattern:

- persona repeats the full workflow already defined in a skill

Better pattern:

- persona defines the lens and output format
- skill remains the source of truth for the process

### Ambiguous Routing

Bad pattern:

- a skill and a persona both claim to be the same primary entry point

Better pattern:

- command or entry docs define when to use the persona versus the skill

### Meta-Orchestrator Persona

Bad pattern:

- one persona exists only to decide which other persona to call

Why it fails:

- adds routing overhead without new domain value
- increases drift and ambiguity
- duplicates what commands and start-here skills should already do

### Hooks Replacing Skills

Bad pattern:

- using hooks as the main execution logic

Better pattern:

- hooks route or guard the work
- skills still define the process

## Practical Mapping For This Repo

- start with `using-data-engineering-agent-skills`
- use one preset
- pick one workflow skill
- use hooks only for guardrails
- use personas mainly for `/review`, `/validate`, and `/ship`

## Decision Matrix

```text
Is the task mainly "how should the work be done"?
├── Yes -> use a skill
└── No -> Is it "from what perspective should this be judged"?
         ├── Yes -> use a persona
         └── No -> Is it a common lifecycle step for users?
                  ├── Yes -> use a command
                  └── No -> use a hook only if it is a pre-flight or routing problem
```
