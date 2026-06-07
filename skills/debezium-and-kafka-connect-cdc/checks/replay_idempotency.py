#!/usr/bin/env python3
"""Replay idempotency harness for CDC transform pipelines.

This check runs a transform command twice and asserts that the outputs are
identical.  CDC pipelines must be idempotent because Debezium delivers events
at-least-once, and operational scenarios (connector restarts, rebalances,
re-snapshots) can replay events.  If a transform is not idempotent, replays
produce incorrect results.

The harness:
1. Runs the specified command (first execution)
2. Captures the output at the specified path
3. Runs the command again (second execution / replay)
4. Compares the two outputs row-by-row
5. Reports differences as structured JSON evidence

Usage:
    python checks/replay_idempotency.py \\
        --command "python transform.py" \\
        --output path/to/output.parquet \\
        --key-columns "id"

    python checks/replay_idempotency.py \\
        --command "python transform.py --input events.jsonl --output result.csv" \\
        --output result.csv \\
        --key-columns "order_id,line_id"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replay idempotency check: run a transform twice and compare outputs."
    )
    parser.add_argument(
        "--command",
        required=True,
        help="Shell command to run the transform.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the output file produced by the command.",
    )
    parser.add_argument(
        "--key-columns",
        required=True,
        help="Comma-separated key columns for row-level comparison.",
    )
    parser.add_argument(
        "--working-dir",
        type=Path,
        default=None,
        help="Working directory for command execution. Defaults to current directory.",
    )
    return parser.parse_args()


def load_dataframe(path: Path) -> "Any":
    """Load a file into a pandas DataFrame based on extension."""
    import pandas as pd

    suffix = path.suffix.lower()
    if suffix == ".parquet":
        return pd.read_parquet(path)
    elif suffix == ".csv":
        return pd.read_csv(path)
    elif suffix in {".jsonl", ".ndjson"}:
        return pd.read_json(path, lines=True)
    else:
        raise SystemExit(f"Unsupported output format: {suffix}. Use .parquet, .csv, or .jsonl")


def file_hash(path: Path) -> str:
    """Compute SHA256 hash of a file for quick equality check."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def run_command(command: str, working_dir: Path | None) -> dict[str, Any]:
    """Run a shell command and return execution details."""
    cwd = str(working_dir) if working_dir else None
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return {
        "returncode": result.returncode,
        "stdout_lines": len(result.stdout.splitlines()),
        "stderr_preview": result.stderr[:500] if result.stderr else "",
    }


def compare_outputs(
    first_path: Path,
    second_path: Path,
    key_columns: list[str],
) -> dict[str, Any]:
    """Compare two output files row-by-row and report differences."""
    import pandas as pd

    # Quick byte-level check first
    if file_hash(first_path) == file_hash(second_path):
        df = load_dataframe(first_path)
        return {
            "row_count_match": True,
            "content_match": True,
            "first_row_count": len(df),
            "second_row_count": len(df),
            "diff_sample": [],
        }

    df1 = load_dataframe(first_path)
    df2 = load_dataframe(second_path)

    row_count_match = len(df1) == len(df2)

    # Sort both by key columns for deterministic comparison
    missing_keys_1 = [k for k in key_columns if k not in df1.columns]
    missing_keys_2 = [k for k in key_columns if k not in df2.columns]
    if missing_keys_1 or missing_keys_2:
        return {
            "row_count_match": row_count_match,
            "content_match": False,
            "first_row_count": len(df1),
            "second_row_count": len(df2),
            "error": f"Key columns missing. Run 1: {missing_keys_1}, Run 2: {missing_keys_2}",
            "diff_sample": [],
        }

    df1_sorted = df1.sort_values(key_columns).reset_index(drop=True)
    df2_sorted = df2.sort_values(key_columns).reset_index(drop=True)

    # Find differences
    diff_sample: list[dict[str, Any]] = []
    if row_count_match:
        # Compare cell-by-cell
        diff_mask = (df1_sorted != df2_sorted).any(axis=1)
        diff_indices = df1_sorted[diff_mask].index.tolist()[:10]
        for idx in diff_indices:
            row_diff: dict[str, Any] = {"row_index": int(idx)}
            for col in df1_sorted.columns:
                val1 = df1_sorted.at[idx, col]
                val2 = df2_sorted.at[idx, col]
                if val1 != val2:
                    row_diff[col] = {"run_1": str(val1), "run_2": str(val2)}
            diff_sample.append(row_diff)
        content_match = len(diff_indices) == 0
    else:
        content_match = False
        # Show row count difference
        diff_sample.append({
            "note": f"Row count mismatch: run_1={len(df1)}, run_2={len(df2)}"
        })

    return {
        "row_count_match": row_count_match,
        "content_match": content_match,
        "first_row_count": len(df1),
        "second_row_count": len(df2),
        "diff_sample": diff_sample,
    }


def check_replay_idempotency(
    command: str,
    output_path: Path,
    key_columns: list[str],
    working_dir: Path | None,
) -> dict[str, Any]:
    """Run transform twice and compare outputs for idempotency."""
    # Run 1
    run1_result = run_command(command, working_dir)
    if run1_result["returncode"] != 0:
        return {
            "check": "replay_idempotency",
            "status": "error",
            "error": "First run failed",
            "command": command,
            "run_1": run1_result,
        }

    if not output_path.exists():
        return {
            "check": "replay_idempotency",
            "status": "error",
            "error": f"Output file not found after first run: {output_path}",
            "command": command,
            "run_1": run1_result,
        }

    # Save first output to temp location
    tmp_dir = Path(tempfile.mkdtemp(prefix="replay_check_"))
    first_output = tmp_dir / f"run1{output_path.suffix}"
    shutil.copy2(output_path, first_output)

    # Run 2 (replay)
    run2_result = run_command(command, working_dir)
    if run2_result["returncode"] != 0:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        return {
            "check": "replay_idempotency",
            "status": "error",
            "error": "Second run (replay) failed",
            "command": command,
            "run_1": run1_result,
            "run_2": run2_result,
        }

    if not output_path.exists():
        shutil.rmtree(tmp_dir, ignore_errors=True)
        return {
            "check": "replay_idempotency",
            "status": "error",
            "error": f"Output file not found after second run: {output_path}",
            "command": command,
        }

    # Compare outputs
    comparison = compare_outputs(first_output, output_path, key_columns)

    # Cleanup
    shutil.rmtree(tmp_dir, ignore_errors=True)

    status = "pass" if comparison["content_match"] and comparison["row_count_match"] else "fail"

    return {
        "check": "replay_idempotency",
        "status": status,
        "command": command,
        "output": str(output_path),
        "key_columns": key_columns,
        "row_count_match": comparison["row_count_match"],
        "content_match": comparison["content_match"],
        "first_row_count": comparison.get("first_row_count"),
        "second_row_count": comparison.get("second_row_count"),
        "diff_sample": comparison["diff_sample"],
    }


def main() -> int:
    args = parse_args()
    key_columns = [k.strip() for k in args.key_columns.split(",")]
    result = check_replay_idempotency(
        command=args.command,
        output_path=args.output,
        key_columns=key_columns,
        working_dir=args.working_dir,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("status") == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
