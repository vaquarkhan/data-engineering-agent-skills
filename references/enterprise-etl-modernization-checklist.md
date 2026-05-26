# Enterprise ETL Modernization Checklist

Use this checklist when operating or migrating `Informatica`, `Talend`, `DataStage`, `SSIS`, `Matillion`, or similar ETL estates.

## Discovery

- [ ] Mappings, workflows, and dependencies are inventoried
- [ ] Parameter files, environment variables, and external scripts are captured
- [ ] Restart and reject-handling behavior is known

## Logic Recovery

- [ ] Hidden business rules inside transformations are documented
- [ ] SCD, deduplication, and surrogate-key behavior are explicit
- [ ] Quality and reject paths are visible

## Migration And Coexistence

- [ ] Legacy versus modern platform boundaries are defined
- [ ] Reconciliation and parity checks are planned
- [ ] Cutover and rollback are documented

## Operations

- [ ] Scheduling, lineage, and run metadata are observable
- [ ] Deployment and promotion paths are repeatable
- [ ] Manual dependencies are reduced or documented
