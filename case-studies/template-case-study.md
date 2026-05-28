# Case Study: <title>

## Scenario

- **Business context:** <what matters to the business>
- **Trigger event:** <what went wrong or what change is required>
- **Blast radius:** <who and what is impacted>

## Target Outcome

- restore or deliver <specific data product outcome>
- protect downstream consumers from bad data
- capture reproducible evidence and rollback safety

## Stack And Scope

- **Platform:** <AWS/Azure/GCP/Databricks/Snowflake/etc>
- **Pipelines/components:** <jobs, models, streams, schedulers>
- **Data contracts:** <source + dataset + metric contracts involved>

## Skills, Presets, And Templates Used

- **Skills:** <list>
- **Presets:** <list>
- **Templates:** <list>

## Step-by-Step Execution

1. **Contain**
   - <containment actions>
2. **Assess**
   - <scope and impact analysis actions>
3. **Correct**
   - <implementation or replay actions>
4. **Validate**
   - <quality, reconciliation, freshness checks>
5. **Publish**
   - <staged release and consumer cutover actions>

## Evidence Required

- <contract validation output>
- <reconciliation/parity output>
- <ownership/approval record>
- <observability/post-release checks>

## Runbook Commands

```bash
# <containment command>
# <validation command>
# <reconciliation command>
# <publish or rollback command>
```

## Acceptance Thresholds

- **Contract checks:** <all required checks must pass>
- **Reconciliation tolerance:** <for example <= 0.1% metric delta>
- **Freshness threshold:** <for example max age 1 hour>
- **Duplicate/error threshold:** <for example 0 duplicate keys>
- **Approval requirement:** <named owner + approver recorded>

## Rollback Plan

- **Rollback trigger:** <clear threshold or condition>
- **Rollback action:** <exact command/process>
- **Rollback validation:** <proof that state is safe again>

## Definition Of Done

- [ ] Containment performed and blast radius documented
- [ ] Corrective change or replay completed for bounded scope only
- [ ] Contract, quality, and reconciliation thresholds met
- [ ] Publish performed in staged mode with monitoring checks
- [ ] Rollback path tested or validated
- [ ] Owner and approver sign-off recorded

## Common Failure Modes

- <failure mode 1>
- <failure mode 2>
- <failure mode 3>

## Adaptation Notes

- <how to adapt this case for other clouds or platforms>
