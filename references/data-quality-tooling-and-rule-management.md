# Data Quality Tooling And Rule Management

Use this guide when deciding how data-quality checks should operate across multiple tools and delivery stages.

## Common Tool Boundaries

- `dbt` tests: warehouse-native model checks and contract-adjacent assertions
- `Great Expectations`, `Deequ`, `Cuallee`, `Soda`: reusable framework-driven quality suites
- warehouse-native monitors: local freshness, anomaly, and platform health checks
- reconciliation-specific checks: financial or source-to-target parity proof

## Rule Categories

- contract and schema correctness
- completeness and freshness
- duplicates and uniqueness
- distribution or anomaly detection
- reconciliation and control totals
- governance or regulated-data enforcement

## Severity Model

- block publish: correctness, contract, reconciliation, or critical compliance failures
- warn and escalate: trend drift, weak signals, or early anomaly indicators
- observe only: exploratory signals not yet tied to publish risk

## Anti-Patterns

- one tool forced onto every workload
- no owner for failed rules
- blocking and non-blocking checks mixed together
- noisy checks left running without review

## Good Outcome

The best quality program has clear ownership, clear evidence, and clear enforcement, even when it uses more than one tool.
