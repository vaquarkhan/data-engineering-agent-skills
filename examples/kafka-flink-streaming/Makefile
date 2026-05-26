TOPIC_LOG=build/topic/order-events.jsonl
SINK_FILE=build/sink/windowed-orders.jsonl
CHECKPOINT_FILE=build/checkpoints/state.json

produce:
	python src/producer.py --input sample/order-events.jsonl --topic-log $(TOPIC_LOG) --reset

run-local:
	python src/stream_job.py --input $(TOPIC_LOG) --output $(SINK_FILE) --checkpoint-output $(CHECKPOINT_FILE)

validate-contract:
	python ../../scripts/validate_dataset_contract.py --contract contracts/windowed-orders-contract.yaml --data $(SINK_FILE)

validate-sink:
	python src/validate_sink.py --sink $(SINK_FILE) --checkpoint $(CHECKPOINT_FILE)

replay:
	python src/replay.py --input sample/order-events.jsonl --topic-log $(TOPIC_LOG)

smoke-test: produce run-local validate-contract validate-sink replay run-local validate-contract validate-sink
