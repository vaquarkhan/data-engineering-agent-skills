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

- `Makefile`
- `docker-compose.yml`
- `schemas/order-events.avsc`
- `config/flink-job.yaml`
- `contracts/windowed-orders-contract.yaml`
- `src/producer.py`
- `src/produce_to_kafka.py`
- `src/replay.py`
- `src/replay_to_kafka.py`
- `src/stream_job.py`
- `src/kafka_to_postgres.py`
- `src/validate_sink.py`
- `src/validate_postgres_sink.py`
- `sample/order-events.jsonl`

## Example Commands

```bash
docker compose up -d
python src/producer.py --input sample/order-events.jsonl --topic-log build/topic/order-events.jsonl --reset
python src/stream_job.py --input build/topic/order-events.jsonl --output build/sink/windowed-orders.jsonl --checkpoint-output build/checkpoints/state.json
python ../../scripts/validate_dataset_contract.py --contract contracts/windowed-orders-contract.yaml --data build/sink/windowed-orders.jsonl
python src/validate_sink.py --sink build/sink/windowed-orders.jsonl --checkpoint build/checkpoints/state.json
python src/replay.py --input sample/order-events.jsonl --topic-log build/topic/order-events.jsonl
python src/stream_job.py --input build/topic/order-events.jsonl --output build/sink/windowed-orders.jsonl --checkpoint-output build/checkpoints/state.json
python src/validate_sink.py --sink build/sink/windowed-orders.jsonl --checkpoint build/checkpoints/state.json
```

Or run the full local proof path:

```bash
make smoke-test
```

## Compose Sandbox Path

The local smoke test uses a deterministic Python harness for CI-friendly replay and contract proof. The included `docker-compose.yml` stack can also be exercised against real `Kafka` and `Postgres` services:

```bash
docker compose up -d
python src/produce_to_kafka.py --input sample/order-events.jsonl --bootstrap-servers localhost:19092 --topic order-events
python src/kafka_to_postgres.py --bootstrap-servers localhost:19092 --topic order-events --postgres-dsn postgresql://stream:stream@localhost:15432/stream
python src/validate_postgres_sink.py --postgres-dsn postgresql://stream:stream@localhost:15432/stream
python src/replay_to_kafka.py --input sample/order-events.jsonl --bootstrap-servers localhost:19092 --topic order-events
python src/kafka_to_postgres.py --bootstrap-servers localhost:19092 --topic order-events --postgres-dsn postgresql://stream:stream@localhost:15432/stream --group-id order-events-demo-replay
python src/validate_postgres_sink.py --postgres-dsn postgresql://stream:stream@localhost:15432/stream
```
