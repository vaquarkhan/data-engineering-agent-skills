# Reverse ETL Operational Serving Checklist

Use this checklist when sending data into operational systems.

## Contract

- [ ] Destination system and audience are defined
- [ ] Key mapping is explicit
- [ ] Sync cadence and freshness are defined
- [ ] Deletes or unsync behavior are documented

## Safety

- [ ] Side effects of replay and retries are understood
- [ ] Destination API or rate-limit constraints are considered
- [ ] Failure handling and divergence monitoring exist

## Readiness

- [ ] Business impact of a bad sync is understood
- [ ] Operational visibility exists before launch
