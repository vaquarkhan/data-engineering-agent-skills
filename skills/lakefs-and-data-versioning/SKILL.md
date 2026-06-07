---
name: lakefs-and-data-versioning
description: Guides agents through data versioning workflows using lakeFS or similar systems. Use when branching data, validating changes before publish, or controlling risky lakehouse operations with versioned data states.
---

# lakeFS And Data Versioning

## Overview

Use this skill when datasets need branch-like safety and controlled promotion. It helps agents treat data versioning as an operational control for risky changes, validation before publish, environment isolation, and safe rollback for lakehouse operations.

## When to Use

- validating data changes in isolation before merging to the main branch
- branching lake data for experiments, migrations, or schema changes
- promoting data states between environments (dev → staging → production)
- implementing safe rollback for risky pipeline changes
- running A/B comparisons between data versions
- creating reproducible dataset snapshots for compliance or debugging

Do not use this when the data platform has no concept of object-level versioning or when changes are small enough that point-in-time snapshots (Iceberg, Delta) provide sufficient safety.

## Workflow

1. Define the versioning goal and branch lifecycle.
   Include:
   - what operation needs safety? (schema migration, backfill, new pipeline, experiment)
   - what is the branch lifecycle? (short-lived feature branch vs long-lived environment branch)
   - who can create, merge, and delete branches?
   - what is the promotion path from branch to main?
   - how long do branches live before cleanup?

2. Design the branch strategy for your use case.
   - feature branches: isolate a single pipeline change, validate, then merge
   - environment branches: map to dev/staging/prod with controlled promotion
   - experiment branches: run alternative logic and compare outputs before committing
   - avoid long-lived branches that drift from main — define merge frequency
   - document naming conventions: `feature/`, `experiment/`, `migration/`

3. Attach validation and quality gates to branch operations.
   - run data quality checks on the branch before merge is allowed
   - compare branch output against main for reconciliation (row counts, aggregates, samples)
   - use pre-merge hooks to enforce contract compliance
   - produce evidence of validation as a merge prerequisite
   - block merges that fail quality gates — no manual overrides without review

4. Plan merge behavior and conflict resolution.
   - lakeFS merges are metadata-level — understand what "conflict" means for data
   - define what happens when the same path is modified on both branches
   - prefer short-lived branches that merge frequently to minimize conflicts
   - document the merge strategy: fast-forward, three-way, or manual resolution
   - test merge behavior with representative datasets before relying on it

5. Make rollback and recovery explicit.
   - every merge to main creates a commit that can be reverted
   - define the rollback procedure: revert commit vs restore from previous branch
   - test rollback before relying on it — does downstream infrastructure handle reverts?
   - document the impact of rollback on consumers who already read the bad state
   - define the communication plan when rollback is needed

6. Manage branch hygiene and operational overhead.
   - set TTL on branches to prevent orphaned experiments
   - monitor branch count and storage usage
   - automate stale branch cleanup
   - track which branches have pending merges and who owns them
   - budget for the storage overhead of maintaining multiple data versions

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We don't need data branching because we have table snapshots." | Snapshots provide point-in-time recovery but not isolated workspaces for testing changes before they affect production. Branching adds proactive safety. |
| "Branches are just for code — data doesn't need them." | Risky data operations (schema changes, backfills, migrations) benefit from the same isolation and validation workflow that code branches provide. |
| "We'll just roll back the table if something goes wrong." | Table rollback works for simple cases but becomes complex with downstream consumers, materialized views, and derived datasets. Versioned branches make rollback explicit. |
| "Branch management is too much overhead for data." | The overhead of branch management is small compared to the cost of a bad publish propagating through downstream systems. |

## Red Flags

- branches are created but never validated before merge
- no naming convention or lifecycle policy for branches
- long-lived branches that drift months behind main without reconciliation
- rollback has never been tested and the team assumes it works
- no quality gate between branch and main — anyone can merge freely
- storage growth from orphaned branches is not monitored
- downstream consumers are not considered during rollback planning
- merge conflicts are resolved by "whoever merges last wins" without review

## Verification

- [ ] Branch lifecycle (create, validate, merge, cleanup) is documented
- [ ] Quality gates and validation checks run before merges are allowed
- [ ] Branch output is reconciled against main before promotion
- [ ] Rollback procedure is documented and tested
- [ ] Branch naming convention and TTL policies are enforced
- [ ] Storage overhead and branch count are monitored
- [ ] Downstream consumer impact is considered in rollback and merge planning
