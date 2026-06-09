#!/usr/bin/env python3
"""Prove timeout resume produces the same publish output as a full run."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def load_rows(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return sorted(rows, key=lambda row: (row["order_id"], row["event_date"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--workdir", default="build")
    parser.add_argument("--run-id", default="run-resume")
    parser.add_argument("--fail-after-partitions", type=int, default=1)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    job = root / "checkpoint_batch_job.py"
    workdir = Path(args.workdir)
    full_workdir = workdir / "full"
    resume_workdir = workdir / "resume"

    for path in (full_workdir, resume_workdir):
        if path.exists():
            shutil.rmtree(path)

    full_cmd = [
        sys.executable,
        str(job),
        "--input",
        args.input,
        "--workdir",
        str(full_workdir),
        "--run-id",
        "run-full",
    ]
    if subprocess.run(full_cmd, check=False).returncode != 0:
        return 1

    timeout_cmd = [
        sys.executable,
        str(job),
        "--input",
        args.input,
        "--workdir",
        str(resume_workdir),
        "--run-id",
        args.run_id,
        "--fail-after-partitions",
        str(args.fail_after_partitions),
    ]
    if subprocess.run(timeout_cmd, check=False).returncode != 2:
        print("Expected timeout exit code 2")
        return 1

    resume_cmd = [
        sys.executable,
        str(job),
        "--input",
        args.input,
        "--workdir",
        str(resume_workdir),
        "--run-id",
        args.run_id,
        "--resume",
    ]
    if subprocess.run(resume_cmd, check=False).returncode != 0:
        return 1

    full_rows = load_rows(full_workdir / "publish" / "aggregated-events.jsonl")
    resume_rows = load_rows(resume_workdir / "publish" / "aggregated-events.jsonl")
    if full_rows != resume_rows:
        print("Resume output does not match full run output")
        print("full:", full_rows)
        print("resume:", resume_rows)
        return 1

    print("Resume proof passed: timeout resume matches full-run publish output")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
