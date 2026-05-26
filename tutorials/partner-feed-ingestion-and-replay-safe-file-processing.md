# Partner Feed Ingestion And Replay-Safe File Processing

Use this tutorial when a dataset is delivered as files by a partner, vendor, or source team and the main design question is how to ingest it safely.

## What You Will Do

1. Define the feed contract
2. Design a landing and quarantine boundary
3. Add completeness and control checks
4. Make replay and corrected-file behavior explicit
5. Protect downstream publish until validation passes

## Step 1: Define The Feed Contract

Start with:

- format and schema
- naming convention
- delivery window
- ownership and escalation path
- manifest, checksum, or control-total expectations

If the feed producer cannot define those basics, treat the ingestion as high-risk from the start.

## Step 2: Design Landing Before Transformation

Separate:

- raw landing
- quarantine or exception handling
- validated staging
- published outputs

This keeps duplicate, late, partial, or corrected files from contaminating downstream layers.

## Step 3: Validate Arrival And Content

At minimum, validate:

- schema shape
- required fields
- row counts or control totals
- file freshness and expected arrival
- duplicate delivery behavior

Pair this tutorial with `references/file-ingestion-checklist.md`.

## Step 4: Make Replay Safe

Document how the system behaves when:

- the same file arrives twice
- a corrected version arrives later
- one file in a batch is missing
- a downstream rerun is required

The point is not only to rerun, but to rerun without breaking correctness.

## Step 5: Block Publish Until Ready

Do not open publish paths because a file landed successfully. Gate publish on:

- successful validation
- duplicate handling
- completeness checks
- downstream readiness

## Recommended Companion Assets

- `skills/file-and-partner-feed-ingestion/SKILL.md`
- `skills/source-reliability-and-extraction-resilience/SKILL.md`
- `references/file-ingestion-checklist.md`
- `templates/source-contract.yaml`
