#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TASKS_PATH = ROOT / "tasks.json"
BASELINE_PATH = ROOT / "baseline-results.json"
WITH_SKILLS_PATH = ROOT / "with-skills-results.json"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def score(tasks: list[dict], results: dict[str, list[str]]) -> tuple[int, int]:
    total = 0
    possible = 0
    for task in tasks:
        expected = set(task["expected_concerns"])
        actual = set(results.get(task["id"], []))
        total += len(expected & actual)
        possible += len(expected)
    return total, possible


def main() -> int:
    tasks = load_json(TASKS_PATH)
    baseline = load_json(BASELINE_PATH)
    with_skills = load_json(WITH_SKILLS_PATH)

    baseline_score, possible = score(tasks, baseline)
    with_skills_score, _ = score(tasks, with_skills)

    print(f"Baseline benchmark score: {baseline_score}/{possible}")
    print(f"With-skills benchmark score: {with_skills_score}/{possible}")

    if with_skills_score <= baseline_score:
        print("Benchmark regression: with-skills score did not improve over baseline.")
        return 1

    print("Benchmark check passed: with-skills coverage improves over baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
