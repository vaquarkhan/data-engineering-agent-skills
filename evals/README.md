# Evaluation Runner

This folder contains a simple runner that compares baseline concern coverage against with-skills concern coverage.

It is intended to provide a repeatable score signal in CI, not a full benchmark framework.

## Run

```bash
python evals/run.py
```

## Optional custom inputs

```bash
python evals/run.py --tasks benchmarks/tasks.json --baseline benchmarks/baseline-results.json --with-skills benchmarks/with-skills-results.json --report evals/report.json
```
