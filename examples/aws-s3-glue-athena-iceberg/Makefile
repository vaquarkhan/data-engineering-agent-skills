run-local:
	python jobs/normalize_customers.py --input data/customers.jsonl --output build/customers.ndjson

validate-contract:
	python ../../scripts/validate_dataset_contract.py --contract contracts/customers-contract.yaml --data build/customers.ndjson --reference-time 2026-05-02T00:00:00Z

reconcile:
	python jobs/reconcile_customers.py --source data/customers.jsonl --normalized build/customers.ndjson

smoke-test: run-local validate-contract reconcile

publish-sql:
	@echo "Review sql/create_publish_view.sql and apply it in Athena or your warehouse tool."
