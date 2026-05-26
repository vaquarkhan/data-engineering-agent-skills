# Lower Environment Masking Checklist

Use this checklist before promoting production-like data into development, QA, or staging.

## Classification

- [ ] Sensitive and regulated fields are identified
- [ ] Re-identification risk through joins or quasi-identifiers is reviewed
- [ ] Datasets that inherit masked keys are mapped

## Masking Strategy

- [ ] The masking method preserves only the behaviors that are actually needed
- [ ] Deterministic masking is used only where referential integrity is required
- [ ] Irreversible masking or synthetic replacement is preferred where possible

## Controls

- [ ] Access to lower-environment masked data is scoped and reviewed
- [ ] Refresh jobs and secrets are audited
- [ ] Unmasked intermediate extracts are not retained

## Operations

- [ ] Refresh cadence and retention are defined
- [ ] Validation confirms masked data is still usable for tests
- [ ] Incident response covers accidental lower-environment exposure
