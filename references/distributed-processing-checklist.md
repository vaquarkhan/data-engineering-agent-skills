# Distributed Processing Checklist

Use this checklist when reviewing or implementing large-scale batch processing.

## Runtime Fit

- [ ] A distributed engine is actually required
- [ ] The runtime choice is explicit: `Spark`, `Glue`, `EMR`, or another engine
- [ ] Cost and latency expectations justify the choice

## Data Layout

- [ ] Input partitioning is defined
- [ ] File size and small-file risk are considered
- [ ] Join keys and skew risks are known
- [ ] Write semantics are explicit: append, overwrite, merge, or upsert

## Operations

- [ ] Retry behavior is safe for the write pattern
- [ ] Backfill behavior is defined
- [ ] Output contracts are validated before publish
- [ ] Monitoring exists for job failure, cost, and runtime degradation
