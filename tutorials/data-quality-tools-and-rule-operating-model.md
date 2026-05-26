# Data Quality Tools And Rule Operating Model

Use this tutorial when the team needs a sustainable quality program instead of only adding more checks.

## What You Will Do

1. Define rule ownership and severity
2. Group quality rules by purpose
3. Choose tool boundaries
4. Connect quality output to publish and incident flows

## Step 1: Define Rule Ownership

Clarify:

- who writes rules
- who approves blocking rules
- who triages failures
- what evidence is required before publish

## Step 2: Group Rules By Purpose

Typical groups:

- contract checks
- completeness and freshness
- reconciliation
- anomaly detection
- regulated-data controls

## Step 3: Choose Tool Boundaries

Examples:

- `dbt` tests for warehouse models
- `Great Expectations`, `Deequ`, `Cuallee`, or `Soda` for reusable suites
- platform-native monitors for local health and drift signals

## Step 4: Make Results Actionable

Every quality result should have:

- severity
- owner
- publish behavior
- incident or escalation path

## Recommended Companion Assets

- `skills/data-quality-platforms-and-rule-management/SKILL.md`
- `skills/data-quality-and-contract-testing/SKILL.md`
- `skills/great-expectations-deequ-and-cuallee/SKILL.md`
- `references/data-quality-tooling-and-rule-management.md`
