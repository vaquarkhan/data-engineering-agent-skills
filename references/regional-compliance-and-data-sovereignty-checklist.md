# Regional Compliance And Data Sovereignty Checklist

Use this checklist when a data platform spans multiple jurisdictions or supervisory regimes. This is an engineering guide, not legal advice.

## Jurisdiction Mapping

- [ ] Data-subject, customer, employee, or partner locations are identified
- [ ] Processing, storage, backup, and admin-access locations are mapped
- [ ] Sector overlays such as finance, health, or public-sector rules are named

## Control Design

- [ ] Residency and transfer boundaries are explicit
- [ ] Encryption, key ownership, and access restrictions match regional obligations
- [ ] Deletion, retention, and data-sharing controls are defined by jurisdiction

## Evidence

- [ ] Regional lineage and transfer evidence can be produced
- [ ] Control owners and approvers are named
- [ ] Breach, regulator, or audit response paths are documented

## Common Jurisdiction Signals

| Region | Typical compliance signals | Engineering focus |
| --- | --- | --- |
| `Europe` | `GDPR`, local privacy authorities, transfer restrictions, deletion rights | minimize data, track lineage, control cross-border transfer paths, prove retention and erasure behavior |
| `USA` | state privacy rules plus sector-specific regimes like `HIPAA`, `GLBA`, or `SOX` depending on the workload | segment controls by state and sector, protect audit evidence, avoid assuming a single national pattern |
| `India` | `DPDP` obligations and local disclosure or governance expectations by sector | consent and notice evidence, local handling rules, transfer structuring, breach-response readiness |
| `Saudi Arabia` | `PDPL`, `SDAIA/NDMO` guidance, and `SAMA` overlays for supervised institutions | residency and transfer review, customer-data protection, governance maturity, self-assessment and board-level evidence where required |

Always confirm the exact obligation set with legal, privacy, and compliance owners before shipping.
