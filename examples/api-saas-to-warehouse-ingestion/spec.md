# Spec: API SaaS To Warehouse Ingestion

## Objective

Create a resilient ingestion pattern for a SaaS API that supports pagination, rate limits, incremental syncs, and publish-safe warehouse outputs.

## Source Systems

- one SaaS API with paginated endpoints and token-based auth

## Destination

- raw response landing
- warehouse staging tables
- curated publish dataset

## Quality Rules

- no silent page loss
- retries must not create duplicate records
- incremental sync windows must be explicit

## Success Criteria

- auth, pagination, and rate-limit behavior are documented
- extraction is replay-safe
- curated tables have validation rules
