# Progressive Data Release Patterns

Use this reference when the change is too risky for deploy-and-publish in one step. These patterns help data teams promote code, contracts, and dataset behavior with staged evidence and controlled downstream visibility.

## Deploy Versus Publish Separation

Deploy the change first, then publish only after validation succeeds.

Use this pattern when:

- pipelines can run without immediately changing downstream-visible outputs
- dataset swaps, view changes, or publish flags are possible
- rollback of published data is harder than rollback of code

Watch for:

- a single step that both deploys code and mutates published outputs
- no point where reconciliation can happen before consumers see the change

## Shadow Validation

Run the new logic in parallel and compare outcomes without replacing the current publish path.

Use this pattern when:

- `dbt`, Spark, or warehouse logic changes are material
- schema evolution or migration needs proof before cutover
- streaming sink behavior is changing and needs confidence first

Watch for:

- shadow outputs existing with no defined comparison rules
- shadow validation checking only row counts when business metrics also matter

## Canary Publish

Expose the new output to a bounded slice of consumers or partitions first.

Use this pattern when:

- consumer groups can be segmented
- one region, tenant, topic, or downstream domain can absorb early risk
- rollback should be low-blast-radius

Watch for:

- canaries that are too small to reveal real behavior
- no clear rule for expanding from canary to full publish

## Dual-Run And Reconciliation Window

Operate old and new paths together for a fixed validation window.

Use this pattern when:

- warehouse cutover or ETL modernization is in progress
- finance, billing, or regulatory outputs need parity evidence
- historical backfills can diverge from current-state outputs

Watch for:

- indefinite dual-run with no exit criteria
- disagreements found during the window with no decision owner

## Consumer Cutover Toggle

Make downstream adoption explicit instead of assuming all consumers move instantly.

Use this pattern when:

- shared datasets, tables, or topics have many consumers
- contract changes require coordination
- the team needs rollback without immediate data mutation

Watch for:

- hidden consumer dependencies
- contract changes announced but not enforced

## Rollback Window And Forward-Fix Boundaries

State clearly when rollback is still safe and when forward-fix is the only realistic option.

Use this pattern when:

- the release mutates datasets, state stores, or topic history
- repair cost rises quickly after publish
- downstream consumers cache or copy results

Watch for:

- "rollback supported" with no time boundary or restore method
- no procedure for reconciling outputs after rollback or forward-fix

## Recommended Pairings In This Repo

- release workflow: `data-platform-ci-cd-and-release-management`
- cutover and dual-run work: `data-migration-and-platform-cutover`
- parity proof: `data-reconciliation-and-financial-controls`
- publish safety: `data-sharing-and-publishing-contracts`
- hook support: `hooks/release-guard.sh`
