# File Ingestion Checklist

Use this checklist when onboarding file-based or partner-managed feeds.

## Contract

- [ ] File format and schema are explicit
- [ ] Naming convention and arrival SLA are defined
- [ ] Partner or source owner is identified
- [ ] Manifest, checksum, or control-total expectations are documented where relevant

## Landing

- [ ] Raw landing location is defined
- [ ] Arrival metadata is captured
- [ ] Duplicate and corrected file behavior are explicit
- [ ] Corrupt or partial deliveries can be quarantined safely

## Validation

- [ ] Schema validation exists
- [ ] Required-field and completeness checks exist
- [ ] Row counts, checksums, or control totals are validated where needed
- [ ] Missing-file and late-file behavior is observable

## Replay And Publish

- [ ] Replay behavior is bounded and documented
- [ ] Corrected file handling is defined
- [ ] Duplicate prevention is explicit
- [ ] Publish remains blocked until validation passes
