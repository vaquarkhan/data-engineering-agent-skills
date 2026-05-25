# Spec: Databricks Delta Medallion

## Objective

Create a reusable `Databricks` medallion pattern that converts raw event and reference data into trusted gold datasets.

## Source Systems

- streaming event feed
- daily reference data loads

## Destination

- bronze raw Delta tables
- silver conformed Delta tables
- gold publish tables for analytics and activation

## Quality Rules

- silver tables enforce schema and key-level checks
- gold tables require explicit owner, grain, and freshness expectations

## Governance

- `Unity Catalog` manages permissions and discoverability
- medallion layer responsibilities must be documented

## Success Criteria

- bronze, silver, and gold boundaries are explicit
- merge and replay behavior are defined
- maintenance tasks such as compaction are planned
