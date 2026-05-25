# Warehouse Schema Design Checklist

Use this checklist when designing warehouse or mart schemas.

## Grain And Keys

- [ ] Each table has a clearly documented row grain
- [ ] Business and surrogate keys are used intentionally
- [ ] Change-over-time handling is defined where relevant

## Modeling

- [ ] The schema pattern matches the use case
- [ ] Fact and dimension boundaries are clear
- [ ] Normalization versus denormalization trade-offs are intentional

## Consumer Fit

- [ ] Analysts can understand and use the schema
- [ ] Performance implications are considered
- [ ] Metric and dashboard consumers are not forced to guess semantics
