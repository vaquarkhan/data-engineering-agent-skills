# Plan: Multi-Cloud Warehouse Cutover

## Architecture

- run source and target warehouses in parallel
- validate reconciled outputs over a defined window
- migrate consumers in phases
- retire the old path only after stable adoption

## Risks

- consumers can depend on undocumented old behavior
- one-time validation can miss operational drift
- rollback can become impossible if old paths are retired too early

## Verification

- reconciliation review
- consumer migration review
- rollback and retirement review
