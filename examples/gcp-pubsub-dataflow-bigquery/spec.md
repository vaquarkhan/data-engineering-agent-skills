# Spec: GCP Pub/Sub Dataflow BigQuery

## Objective

Deliver a real-time GCP streaming pattern that converts event traffic into trustworthy `BigQuery` serving tables.

## Source Systems

- application events published to `Pub/Sub`

## Destination

- curated `BigQuery` tables

## Quality Rules

- event contract and keys must be explicit
- lag and freshness must be measurable
- replay behavior must avoid silent duplication

## Success Criteria

- processor, sink, and replay semantics are documented
- serving tables support analytics consumers
- operational visibility exists for lag and failures
