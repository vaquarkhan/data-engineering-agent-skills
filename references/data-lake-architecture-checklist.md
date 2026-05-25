# Data Lake Architecture Checklist

Use this checklist when designing or reviewing a data lake.

## Zone Design

- [ ] Each zone has a distinct purpose
- [ ] Read and write expectations are explicit
- [ ] Publish-ready data is separated from raw landing data

## Storage Conventions

- [ ] Naming, partitioning, and ownership metadata are defined
- [ ] Retention and cleanup rules exist
- [ ] File-size and lifecycle expectations are considered

## Governance

- [ ] Dataset ownership is clear
- [ ] Shared consumption rules are explicit
- [ ] The lake is not being treated as an undocumented catch-all store
