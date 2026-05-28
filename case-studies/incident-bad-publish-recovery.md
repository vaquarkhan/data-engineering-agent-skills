# Case Study: Bad Publish Recovery

## Scenario

- **Business context:** Daily revenue dashboards and finance extracts depend on curated publish tables.
- **Trigger event:** A transformation change introduced incorrect revenue aggregation and was published.
- **Blast radius:** Executive dashboard, finance reporting, and reverse ETL consumers.

## Target Outcome

- stop further bad publishes quickly
- restore trusted published outputs
- re-open publish only after reconciliation and sign-off

## Stack And Scope

- **Platform:** warehouse plus `dbt` model layer
- **Pipelines/components:** staging model, mart model, publish view
- **Data contracts:** dataset contract for published mart and metric assumptions for revenue

## Skills, Presets, And Templates Used

- **Skills:** `incident-triage-and-pipeline-recovery`, `data-reconciliation-and-financial-controls`, `data-platform-ci-cd-and-release-management`, `data-observability-and-sla-management`
- **Presets:** platform-specific warehouse preset
- **Templates:** `templates/incident-runbook.md`, `templates/release-gate-evidence.yaml`
- **Repo anchors:** `examples/dbt-warehouse-marts/README.md`, `examples/dbt-warehouse-marts/Makefile`, `examples/dbt-warehouse-marts/contracts/fct_daily_revenue-contract.yaml`

## Step-by-Step Execution

1. **Contain**
   - disable or gate publish step to prevent additional consumer impact
   - keep affected window bounded and visible in incident notes
2. **Assess**
   - identify impacted tables, views, dashboards, and feeds
   - compare pre-change baseline metrics against current output
3. **Correct**
   - revert to last known good model logic or view definition
   - run model rebuild only for the affected window
4. **Validate**
   - run contract checks and data tests
   - reconcile totals and key metrics against trusted baseline
5. **Publish**
   - re-enable publish in staged mode first
   - reopen downstream consumption only after owner approval

## Evidence Required

- contract validation output for restored dataset
- reconciliation report with metric parity
- incident timeline with owner and approver sign-off
- post-release observability confirmation (freshness and error signals)

## Runbook Commands

```bash
cd examples/dbt-warehouse-marts
python -c "from pathlib import Path; Path('build').mkdir(exist_ok=True)"
dbt seed --project-dir . --profiles-dir profiles
dbt run --project-dir . --profiles-dir profiles
dbt test --project-dir . --profiles-dir profiles
python ../../scripts/validate_dataset_contract.py --contract contracts/fct_daily_revenue-contract.yaml --duckdb build/dbt_warehouse_marts.duckdb --query "select * from fct_daily_revenue order by order_date"
```

## Acceptance Thresholds

- **Contract checks:** dataset contract passes without warnings that impact publish safety
- **Reconciliation tolerance:** key publish metrics differ by no more than 0.1% versus last known good baseline
- **Freshness threshold:** latest publish timestamp remains within 1 hour of expected schedule
- **Quality threshold:** all `dbt test` checks pass
- **Approval requirement:** release owner and business approver sign-off captured in incident evidence

## Rollback Plan

- **Rollback trigger:** reconciliation mismatch or critical metric deviation remains above agreed threshold
- **Rollback action:** restore prior publish artifact (view/table pointer) and keep publish gated
- **Rollback validation:** consumers see last known good values and freshness remains within SLA

## Definition Of Done

- [ ] Publish path was contained before broad consumer impact expanded
- [ ] Corrective logic applied only to affected window/scope
- [ ] Contract, test, and reconciliation thresholds passed
- [ ] Staged publish re-enabled with owner approval
- [ ] Rollback path validated in release-gate evidence

## Common Failure Modes

- rerunning full history without bounding the affected window
- reopening publish before downstream parity checks are complete
- relying on row counts only while business metrics remain wrong

## Adaptation Notes

- for streaming paths, replace publish gate with consumer cutover control and checkpoint-aware replay
- for lakehouse paths, validate both table data and catalog-level exposure controls
