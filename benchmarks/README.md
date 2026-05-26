# Agent Behavior Benchmarks

This folder contains a lightweight benchmark pack that compares baseline agent behavior against responses produced with the data engineering skills loaded.

Use it to answer one practical question: does the skill pack cause an agent to cover more data-engineering concerns such as contracts, replay safety, observability, rollback, and compliance?

## Included Assets

- `tasks.json`
  Ten benchmark prompts covering contracts, dbt, streaming, schema change, regulated data, backfills, cost review, release safety, incidents, and Terraform.
- `baseline-results.json`
  Sample concern coverage without the skill pack.
- `with-skills-results.json`
  Sample concern coverage with the skill pack loaded.
- `score_benchmarks.py`
  Scores concern coverage and fails if the with-skills run does not improve over baseline.

## Run

```bash
python benchmarks/score_benchmarks.py
```

## Good Outcome

The with-skills score should exceed the baseline score and demonstrate that the toolkit changes what the agent remembers to check.
