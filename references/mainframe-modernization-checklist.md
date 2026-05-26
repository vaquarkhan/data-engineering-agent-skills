# Mainframe Modernization Checklist

Use this checklist when modernizing mainframe-origin data into modern data platforms.

## Source Inventory

- [ ] Source systems such as `COBOL`, `JCL`, `VSAM`, `IMS`, or `DB2 for z/OS` are identified
- [ ] Copybooks or record layouts are collected
- [ ] Batch schedules and restart behavior are documented
- [ ] Downstream consumers and reports are known

## Target Design

- [ ] Offload, replication, or coexistence strategy is explicit
- [ ] Target storage and serving platforms are defined
- [ ] Field mapping and data-contract translation are documented
- [ ] Latency and batch-window expectations are clear

## Parity And Cutover

- [ ] Reconciliation and control totals are designed
- [ ] Dual-run or coexistence period is planned
- [ ] Consumer migration sequencing is documented
- [ ] Backout path exists

## Operations

- [ ] Failure recovery and rerun behavior are defined
- [ ] Support ownership is explicit
- [ ] Cutover evidence is reviewable
- [ ] Post-cutover monitoring is planned
