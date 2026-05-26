---
name: file-and-partner-feed-ingestion
description: Guides agents through file-based and partner-feed ingestion workflows. Use when landing data from SFTP, managed file transfer, shared buckets, recurring flat files, manifests, or externally supplied feeds that need validation, replay safety, and publish discipline.
---

# File And Partner Feed Ingestion

## Overview

Use this skill when ingestion depends on externally delivered files rather than APIs or CDC streams. It helps agents design landing, validation, late-file handling, checksum or manifest controls, replay safety, and publish boundaries for partner-managed feeds.

## When to Use

- onboarding `SFTP`, MFT, or shared-bucket file feeds
- ingesting recurring `CSV`, `JSON`, `XML`, or columnar extracts from external partners
- validating manifests, checksums, control totals, or arrival windows
- handling late, duplicate, partial, or corrected file deliveries
- defining replay-safe landing and publish behavior for externally supplied data

Do not assume file ingestion is simple just because the payload arrives in a batch.

## Workflow

1. Define the feed contract.
   Clarify:
   - file format and expected schema
   - naming convention
   - arrival schedule or SLA
   - manifest, checksum, or control-total expectations
   - ownership and contact path for the partner or source team

2. Design the landing boundary.
   Decide:
   - where raw files land
   - what metadata is captured
   - how duplicates are detected
   - how partial or corrupt deliveries are quarantined

3. Validate before publish.
   Include:
   - schema and required-field checks
   - checksum or manifest validation
   - row-count or control-total validation
   - late-file and missing-file detection

4. Make replay behavior explicit.
   Decide how:
   - corrected files are handled
   - duplicate files are ignored or reconciled
   - replay windows are bounded
   - downstream publishes stay protected until validation passes

5. Define failure and escalation behavior.
   Document:
   - who gets alerted
   - what blocks publish
   - how the partner is contacted
   - how recovery evidence is recorded

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It is just a file drop." | File-based feeds often fail through late arrival, partial delivery, duplicate upload, or silent schema drift. |
| "We can validate after loading." | Weak landing controls let corrupt or incomplete partner data flow too far downstream. |
| "If the partner resends the file, we are fine." | Resends without replay-safe handling can create duplicate or conflicting publishes. |

## Red Flags

- file naming and arrival expectations are undocumented
- manifest, checksum, or control totals are ignored
- duplicate and corrected file behavior is undefined
- late or missing files do not create actionable alerts
- downstream publish opens before the landing validations complete

## Verification

- [ ] The feed contract defines format, arrival, and ownership expectations
- [ ] Landing, quarantine, and duplicate-handling rules are explicit
- [ ] Validation covers schema, completeness, and control totals where relevant
- [ ] Replay and corrected-file behavior are documented before go-live
- [ ] Failure handling and partner escalation paths are operationally clear
