---
name: mainframe-modernization-and-data-offload
description: Guides agents through mainframe data modernization and offload workflows. Use when migrating or exposing data from COBOL, JCL, VSAM, IMS, DB2 for z/OS, or batch-oriented mainframe estates into modern lakes, warehouses, streaming systems, and governed data products.
---

# Mainframe Modernization And Data Offload

## Overview

Use this skill when a modernization effort involves mainframe systems, batch schedules, and legacy data structures rather than only modern ETL tooling. It helps agents design offload, replication, contract mapping, coexistence, reconciliation, and cutover paths for mainframe-origin data.

## When to Use

- modernizing `COBOL`, `JCL`, `VSAM`, `IMS`, or `DB2 for z/OS` data flows
- offloading mainframe data to lakes, warehouses, or downstream APIs
- mapping copybooks and legacy record layouts into modern contracts
- designing coexistence between batch mainframe outputs and modern platforms
- planning phased cutover, replay, and reconciliation for legacy estates

Do not treat mainframe modernization as only a transport problem. Semantics, batch windows, restart behavior, and operational dependencies matter.

## Workflow

1. Inventory the legacy behavior.
   Capture:
   - source systems
   - copybooks or record layouts
   - batch schedules
   - restart and rerun behavior
   - downstream consumers

2. Define the modernization target.
   Decide:
   - offload versus replication versus coexistence
   - target storage and serving platforms
   - contract and schema mapping
   - latency and batch-window expectations

3. Design parity and reconciliation.
   Require:
   - source-to-target field mapping
   - control totals and reconciliation
   - correction and replay behavior
   - cutover acceptance criteria

4. Plan coexistence and cutover.
   Cover:
   - dual-run period
   - dependent consumer migrations
   - backout plan
   - ownership and incident routing during cutover

5. Validate operational readiness.
   Check restart, failure recovery, performance windows, and support responsibilities before moving critical consumers.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "We only need to copy the files out." | Mainframe jobs often encode business rules, restart behavior, and sequencing that must be preserved or redesigned. |
| "Schema mapping is straightforward once we read the copybook." | Field semantics, packed decimals, dates, and code tables often require careful domain translation. |
| "We can switch consumers after one successful run." | Mainframe modernization usually needs parity evidence and a deliberate coexistence period. |

## Red Flags

- copybook or record semantics are not mapped explicitly
- restart and batch-window behavior are ignored
- reconciliation relies on spot checks instead of control evidence
- consumer cutover sequencing is vague
- there is no backout or coexistence plan

## Verification

- [ ] Legacy source behavior and dependencies are inventoried
- [ ] Target contracts and platform boundaries are explicit
- [ ] Reconciliation and parity evidence are designed before cutover
- [ ] Coexistence and backout behavior are documented
- [ ] Operational support and failure recovery are clear
