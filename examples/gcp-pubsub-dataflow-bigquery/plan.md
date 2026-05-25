# Plan: GCP Pub/Sub Dataflow BigQuery

## Architecture

- ingest events from `Pub/Sub`
- process and enrich in `Dataflow`
- publish analytics-ready outputs in `BigQuery`

## Risks

- schema drift can break processors or sinks
- checkpoint and replay rules can be misunderstood
- query cost can rise if serving tables are not designed intentionally

## Verification

- event contract review
- streaming operational review
- `BigQuery` serving and freshness review
