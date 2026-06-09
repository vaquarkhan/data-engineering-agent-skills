# Kafka Production Guardrails

Use this reference when production Kafka changes must not introduce breaking schemas, silent message loss, or unbounded poison pill retries.

## Producer Durability Baseline

Default production settings unless a named owner documents a waiver:

| Setting | Production default | Why |
| --- | --- | --- |
| `acks` | `all` | Survive leader failure without silent loss |
| `enable.idempotence` | `true` | Prevent duplicate publish on retries |
| `retries` | bounded with `delivery.timeout.ms` | Avoid infinite retry storms |
| `compression.type` | `lz4` or `zstd` | Throughput without sacrificing durability config review |

## Schema Evolution Rules

- production subjects never use `NONE` compatibility
- prefer additive optional fields with defaults
- use new subject or topic only when semantics truly fork
- run registry compatibility in CI before merge
- document deploy order: consumers first for backward additions, producers first only when forward-compatible path is proven

## Dead-Letter Queue Pattern

```
primary topic -> consumer -> success sink
                         \-> DLQ topic (deser / schema / rule failures)
```

DLQ requirements:

- retained long enough for replay and audit
- alert when DLQ rate exceeds baseline
- replay procedure uses same deduplication keys as primary sink
- no auto-skip of bad records without classification metadata

## Consumer Lag And Replay

Before offset reset or wide replay:

- inspect per-partition lag and DLQ volume
- pause downstream publish when replay can duplicate serving-layer rows
- load `safe-backfill-and-replay-orchestration` for publish-bound systems
- use `mcp/kafka.mcp.json` to capture lag evidence before and after recovery

## Red Flags In Agent-Proposed Changes

- decreasing `acks` to improve latency
- widening `max.poll.records` without memory analysis
- adding fields without compatibility check
- consumer catch-up by `seekToBeginning` on production groups without plan
