# API SaaS Ingestion Checklist

Use this checklist when extracting from APIs or SaaS platforms.

## Contract

- [ ] Pagination or cursor strategy is explicit
- [ ] Rate limits and retry behavior are defined
- [ ] Auth and token rotation are considered
- [ ] Incremental versus snapshot behavior is clear

## Safety

- [ ] Partial page failures are handled safely
- [ ] Backfills and reruns are idempotent or recoverable
- [ ] Raw response evidence is retained where useful

## Drift

- [ ] Source contract drift is monitored
- [ ] Extraction windows do not depend on undocumented assumptions
