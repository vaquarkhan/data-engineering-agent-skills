---
name: data-platform-operating-model-and-service-ownership
description: Guides agents through data platform operating model and ownership design. Use when defining platform team responsibilities, service tiers, golden paths, escalation boundaries, onboarding flows, or handoffs between central platform teams and domain or product teams.
---

# Data Platform Operating Model And Service Ownership

## Overview

Use this skill when the hard problem is organizational and operational, not just technical. It helps agents define who owns platform capabilities, how teams onboard safely, what the golden paths are, and how support, escalation, and service boundaries work across a shared data platform.

## When to Use

- defining central platform-team responsibilities
- clarifying handoffs between platform and domain teams
- designing golden paths for new datasets, pipelines, or consumer onboarding
- documenting support tiers, ownership, and escalation paths
- reducing operational sprawl and unclear platform accountability

Do not assume a good architecture will operate well if the ownership model is vague.

## Workflow

1. Define the service catalog.
   List:
   - supported platform capabilities
   - approved golden paths
   - self-service versus managed services
   - support boundaries and exclusions

2. Assign ownership clearly.
   Clarify:
   - platform-team ownership
   - domain-team ownership
   - on-call or support expectations
   - approval and escalation paths

3. Define onboarding and lifecycle flows.
   Cover:
   - new source intake
   - dataset onboarding
   - access requests
   - incident routing
   - deprecation and retirement

4. Define service levels and guardrails.
   Include:
   - support tiers
   - change windows where relevant
   - escalation expectations
   - required contracts, validation, and operational evidence

5. Keep the model reviewable and executable.
   The operating model should be visible in docs, runbooks, and actual platform workflows, not just organization charts.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Everyone owns quality." | Shared responsibility with no explicit owner usually means no one acts quickly enough. |
| "The platform team can handle anything." | Undefined service boundaries create burnout, delays, and unsafe tribal processes. |
| "We can formalize the golden path later." | Without an explicit adoption path, teams create inconsistent local patterns that are harder to govern. |

## Red Flags

- support boundaries are vague or tribal
- domain teams and platform teams disagree on who owns incidents or changes
- onboarding depends on undocumented manual steps
- there is no explicit service catalog or golden path
- deprecation and retirement have no owner

## Verification

- [ ] Platform capabilities and support boundaries are documented
- [ ] Ownership and escalation paths are explicit for common workflows
- [ ] Golden paths exist for onboarding and routine delivery work
- [ ] Service levels and required guardrails are defined
- [ ] The operating model is reflected in real workflows, not only in abstract policy
