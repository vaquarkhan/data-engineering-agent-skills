run-local:
	python src/bronze_to_silver.py --input sample/bronze.jsonl --output build/silver.jsonl

validate-contract:
	python ../../scripts/validate_dataset_contract.py --contract contracts/silver-contract.yaml --previous-contract contracts/silver-contract-v1.yaml --data build/silver.jsonl --reference-time 2026-05-02T00:00:00Z

validate-silver:
	python src/validate_silver.py --silver build/silver.jsonl

rollback:
	python src/rollback_silver.py --snapshot snapshots/silver_previous.jsonl --output build/silver.jsonl

validate-rollback:
	python src/validate_rollback.py --silver build/silver.jsonl

smoke-test: run-local validate-contract validate-silver rollback validate-rollback
