# Delta Lake Medallion Checklist

Use this checklist when designing or reviewing `Delta Lake` medallion architectures.

## Layering

- [ ] Bronze, silver, and gold responsibilities are explicit
- [ ] Validation and contract rules differ appropriately by layer
- [ ] Gold outputs are publish-ready rather than raw derivatives

## Delta Behavior

- [ ] Merge and mutation semantics are documented
- [ ] Schema enforcement and evolution policy is explicit
- [ ] Batch and streaming interactions are coordinated

## Maintenance

- [ ] Compaction and optimization are planned
- [ ] Retention and cleanup rules exist
- [ ] Recovery and replay behavior are understood
