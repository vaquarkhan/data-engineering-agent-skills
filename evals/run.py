#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare baseline and with-skills concern coverage scores."
    )
    parser.add_argument(
        "--tasks",
        type=Path,
        default=Path("benchmarks/tasks.json"),
        help="Path to tasks definition file",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=Path("benchmarks/baseline-results.json"),
        help="Path to baseline results file",
    )
    parser.add_argument(
        "--with-skills",
        type=Path,
        default=Path("benchmarks/with-skills-results.json"),
        help="Path to with-skills results file",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("evals/report.json"),
        help="Output path for JSON report",
    )
    return parser.parse_args()


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
    args = parse_args()
    tasks = load_json(args.tasks)
    baseline = load_json(args.baseline)
    with_skills = load_json(args.with_skills)

    baseline_score, possible = score(tasks, baseline)
    with_skills_score, _ = score(tasks, with_skills)
    delta = with_skills_score - baseline_score

    report = {
        "baseline_score": baseline_score,
        "with_skills_score": with_skills_score,
        "possible_score": possible,
        "delta": delta,
        "improved": delta > 0,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(
        f"Baseline: {baseline_score}/{possible} | With skills: {with_skills_score}/{possible} | Delta: {delta:+d}"
    )
    if delta <= 0:
        print("Evaluation failed: with-skills score did not improve.")
        return 1
    print(f"Evaluation report written to {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
