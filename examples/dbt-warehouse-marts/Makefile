prepare:
	python -c "from pathlib import Path; Path('build').mkdir(exist_ok=True)"

seed: prepare
	dbt seed --project-dir . --profiles-dir profiles

run: prepare
	dbt run --project-dir . --profiles-dir profiles

test: prepare
	dbt test --project-dir . --profiles-dir profiles

validate-contract:
	python ../../scripts/validate_dataset_contract.py --contract contracts/fct_daily_revenue-contract.yaml --duckdb build/dbt_warehouse_marts.duckdb --query "select * from fct_daily_revenue order by order_date"

smoke-test: seed run test validate-contract
