# Source Reliability Extraction Checklist

Use this checklist when upstream reliability is a major concern.

## Failure Modes

- [ ] Known upstream failure patterns are documented
- [ ] Timeout and partial-response behavior are defined
- [ ] Late-source handling is explicit

## Behavior

- [ ] Retry and backoff strategy is deliberate
- [ ] Partial data publish behavior is explicit
- [ ] Recovery and catchup steps are documented

## Observability

- [ ] Source health is measurable
- [ ] Upstream incidents are distinguishable from downstream failures
