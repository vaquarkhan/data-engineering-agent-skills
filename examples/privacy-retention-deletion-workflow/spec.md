# Spec: Privacy Retention Deletion Workflow

## Objective

Create an operational privacy workflow that classifies sensitive data, enforces retention, and propagates deletion actions through downstream data products.

## Source Systems

- operational sources containing personal data

## Destination

- governed transformed and published datasets with retention and deletion controls

## Quality Rules

- sensitive fields must be classified
- retention windows must be enforced
- deletion propagation must be auditable

## Success Criteria

- data copies are mapped
- deletion and retention behavior are documented
- audit evidence can be retained for review
