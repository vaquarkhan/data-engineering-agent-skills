# Data Platform Security Checklist

Use this checklist when reviewing or implementing data platform security controls, even when the data is not under a named regulated-data regime.

## Identity And Access

- [ ] Owners and platform operators are identified
- [ ] Least-privilege roles are defined
- [ ] Human and service-account access are separated
- [ ] Break-glass access is controlled and auditable

## Secrets And Keys

- [ ] Secrets are not hard-coded
- [ ] Secrets rotation expectations are defined
- [ ] KMS or equivalent key-management requirements are explicit
- [ ] Sensitive tokens are scoped to the minimum required permissions

## Data Access Controls

- [ ] Row-level or column-level restrictions are applied where needed
- [ ] Shared datasets have explicit consumer boundaries
- [ ] Raw and publish layers do not expose the same data unnecessarily
- [ ] Sensitive extracts or exports are controlled

## Network And Environment Boundaries

- [ ] Environment separation is explicit
- [ ] Public endpoints are minimized
- [ ] Service-to-service boundaries are intentional
- [ ] Non-production access to production data is controlled

## Logging And Auditability

- [ ] Access and administrative changes are logged
- [ ] Logs preserve enough context for investigation
- [ ] Audit evidence is retained for security-relevant operations
- [ ] Sensitive values are not leaked into logs

## Operational Safety

- [ ] Schema and access changes have rollback plans
- [ ] Backfill or replay work does not bypass normal access boundaries
- [ ] Platform changes are reviewed together with governance and publish impact
- [ ] Incident response for security-relevant failures is documented
