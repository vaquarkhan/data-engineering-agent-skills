run-full:
	python jobs/checkpoint_batch_job.py --input data/order-events.jsonl --workdir build/full --run-id run-full

validate-contract:
	python ../../scripts/validate_dataset_contract.py --contract contracts/aggregated-events-contract.yaml --data build/full/publish/aggregated-events.jsonl

validate-resume:
	python jobs/validate_resume.py --input data/order-events.jsonl --workdir build --run-id run-resume --fail-after-partitions 1

orphan-check:
	python jobs/orphan_cleanup.py --workdir build/resume --older-than-minutes 0 --dry-run

smoke-test: run-full validate-contract validate-resume orphan-check
