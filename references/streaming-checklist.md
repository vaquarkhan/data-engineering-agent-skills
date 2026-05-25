# Streaming Checklist

Use this checklist when designing or reviewing event-driven pipelines.

## Event Contract

- [ ] Event keys are defined
- [ ] Schema versioning rules exist
- [ ] Ordering expectations are explicit
- [ ] Retention and replay policy are defined

## Processing Semantics

- [ ] Windowing and watermark behavior are defined where needed
- [ ] Delivery guarantees are explicit
- [ ] Deduplication strategy exists
- [ ] State and checkpoint behavior are defined

## Operations

- [ ] Consumer lag is observable
- [ ] Dead-letter or poison-message handling exists
- [ ] Replay can be executed intentionally
- [ ] Recovery steps exist for failed processors or bad deployments
