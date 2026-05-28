# Case Study: Replay-Safe Backfill After Corruption

## Scenario

- **Business context:** A streaming-to-warehouse pipeline feeds operational and analytics consumers.
- **Trigger event:** Logic bug corrupted 30 days of aggregate output.
- **Blast radius:** Derived marts, alert thresholds, and downstream ML feature consumption.

## Target Outcome

- replay only corrupted windows
- avoid duplicate or conflicting writes during backfill
- prove parity against expected baseline before publish cutover

## Stack And Scope

- **Platform:** Kafka/stream processor + warehouse sink
- **Pipelines/components:** topic ingestion, stream aggregation job, sink table
- **Data contracts:** source event schema contract and windowed aggregate dataset contract

## Skills, Presets, And Templates Used

- **Skills:** `orchestration-and-backfills`, `streaming-and-messaging-systems`, `data-reconciliation-and-financial-controls`, `schema-evolution-and-contract-migrations`
- **Presets:** `presets/apache-kafka-streaming/PRESET.md`, `presets/apache-flink-stream-processing/PRESET.md`
- **Templates:** `templates/backfill-plan.yaml`, `templates/release-gate-evidence.yaml`
- **Repo anchors:** `examples/kafka-flink-streaming/README.md`, `examples/kafka-flink-streaming/Makefile`, `examples/kafka-flink-streaming/contracts/windowed-orders-contract.yaml`

## Step-by-Step Execution

1. **Contain**
   - pause publish-facing consumer or view swap stage
   - preserve current checkpoints and offsets for forensic comparison
2. **Assess**
   - define exact affected partitions/time windows
   - document downstream dependencies and SLA risk
3. **Correct**
   - patch transformation logic
   - replay bounded partitions with idempotent sink semantics
4. **Validate**
   - run contract validation on replayed sink output
   - run reconciliation across counts, sums, and key business metrics
5. **Publish**
   - switch consumer visibility to corrected dataset in staged rollout
   - monitor lag, freshness, and error rates during cutover

## Evidence Required

- backfill plan with affected window and owner approval
- checkpoint/offset records before and after replay
- contract validation output for replayed sink
- reconciliation report confirming metric parity
- release gate evidence showing staged cutover and rollback readiness

## Runbook Commands

```bash
cd examples/kafka-flink-streaming
python src/producer.py --input sample/order-events.jsonl --topic-log build/topic/order-events.jsonl --reset
python src/stream_job.py --input build/topic/order-events.jsonl --output build/sink/windowed-orders.jsonl --checkpoint-output build/checkpoints/state.json
python ../../scripts/validate_dataset_contract.py --contract contracts/windowed-orders-contract.yaml --data build/sink/windowed-orders.jsonl
python src/validate_sink.py --sink build/sink/windowed-orders.jsonl --checkpoint build/checkpoints/state.json
python src/replay.py --input sample/order-events.jsonl --topic-log build/topic/order-events.jsonl
python src/stream_job.py --input build/topic/order-events.jsonl --output build/sink/windowed-orders.jsonl --checkpoint-output build/checkpoints/state.json
python src/validate_sink.py --sink build/sink/windowed-orders.jsonl --checkpoint build/checkpoints/state.json
```

## Acceptance Thresholds

- **Contract checks:** windowed output contract passes
- **Reconciliation tolerance:** replayed aggregate metrics differ by no more than 0.1% from trusted baseline
- **Duplicate threshold:** zero duplicate `event_id` values in checkpoint dedup state
- **Freshness threshold:** sink output timestamp within 15 minutes of expected pipeline watermark
- **Approval requirement:** backfill plan signed by platform owner and affected consumer owner

## Rollback Plan

- **Rollback trigger:** parity failure, duplicate detection, or freshness degradation beyond SLA
- **Rollback action:** revert consumer visibility to prior trusted publish and halt replay pipeline
- **Rollback validation:** downstream consumers return to known-good state and lag normalizes

## Definition Of Done

- [ ] Affected replay window explicitly bounded and approved
- [ ] Replay completed with checkpoint evidence captured
- [ ] Contract and reconciliation thresholds passed
- [ ] Staged publish cutover completed with monitoring
- [ ] Rollback action remains immediately executable

## Common Failure Modes

- replaying unbounded history and causing unnecessary cost and risk
- skipping checkpoint evidence, making replay correctness unverifiable
- publishing corrected output before reconciling duplicate delivery edge cases

## Adaptation Notes

- for batch-only systems, replace offset/checkpoint evidence with partition watermark and rerun metadata
- for managed cloud streaming services, map replay controls to native retention and seek primitives
