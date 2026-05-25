# Kafka Flink Streaming

## Scenario

Build a real-time data pipeline that ingests events through `Kafka`, processes them with `Flink`, and publishes validated outputs for downstream analytics and operational consumers.

## Core Stack

- `Kafka`
- `Flink`
- schema-aware event contracts
- streaming observability and replay controls

## Skills To Apply

- `streaming-and-messaging-systems`
- `cdc-and-incremental-loading`
- `data-observability-and-sla-management`
- `incident-triage-and-pipeline-recovery`

## Example Outcome

- governed topic contracts
- stateful stream processing with replay strategy
- validated sink behavior
- operational visibility for lag and failures

## Minimal Runnable Scaffold

Files included:

- `docker-compose.yml`
- `schemas/order-events.avsc`
- `config/flink-job.yaml`
- `src/stream_job.py`

## Example Commands

```bash
docker compose up -d
python src/stream_job.py --input sample/order-events.jsonl --output build/enriched-events.jsonl
```
