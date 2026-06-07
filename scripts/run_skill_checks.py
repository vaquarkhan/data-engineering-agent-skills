#!/usr/bin/env python3
"""Generic runner that discovers and executes checks for a given skill.

This script provides a unified entry point to run all quality checks defined
in a skill's checks/ directory.  It aggregates results into a single JSON
evidence report and returns an appropriate exit code for CI integration.

Usage:
    python scripts/run_skill_checks.py \\
        --skill debezium-and-kafka-connect-cdc \\
        --source data/ \\
        --contract contract.yaml

    python scripts/run_skill_checks.py \\
        --skill debezium-and-kafka-connect-cdc \\
        --source data/orders.parquet \\
        --contract contracts/orders-contract.yaml \\
        --key order_id \\
        --threshold 0.001

Exit codes:
    0 = all checks pass
    1 = one or more checks failed
    2 = execution error (check could not run)
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path
from typing import Any


SKILLS_ROOT = Path(__file__).resolve().parent.parent / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover and run checks for a given skill."
    )
    parser.add_argument(
        "--skill",
        required=True,
        help="Skill name (directory under skills/).",
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Path to data source file or directory.",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        help="Path to dataset contract YAML.",
    )
    parser.add_argument(
        "--key",
        help="Comma-separated business key column(s) for duplicate checks.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="Duplicate rate threshold. Default: 0.0",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        help="Path to JSON schema file for drift checks.",
    )
    parser.add_argument(
        "--command",
        help="Transform command for replay idempotency checks.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file path for replay idempotency checks.",
    )
    parser.add_argument(
        "--key-columns",
        help="Comma-separated key columns for replay comparison.",
    )
    parser.add_argument(
        "--checks",
        help="Comma-separated list of specific checks to run. Default: all discovered checks.",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        help="Optional path to write aggregated JSON report.",
    )
    return parser.parse_args()


def discover_checks(skill_name: str) -> list[Path]:
    """Find all Python check files in a skill's checks/ directory."""
    checks_dir = SKILLS_ROOT / skill_name / "checks"
    if not checks_dir.is_dir():
        return []
    return sorted(
        p for p in checks_dir.glob("*.py")
        if p.name != "__init__.py" and not p.name.startswith("_")
    )


def load_check_module(check_path: Path) -> Any:
    """Dynamically load a check module from its file path."""
    module_name = f"check_{check_path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, check_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {check_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_duplicate_rate_check(check_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    """Run the duplicate_rate check with provided arguments."""
    if not args.source:
        return {"check": "duplicate_rate", "status": "skipped", "reason": "no --source provided"}
    if not args.key:
        return {"check": "duplicate_rate", "status": "skipped", "reason": "no --key provided"}

    module = load_check_module(check_path)
    key_columns = [k.strip() for k in args.key.split(",")]
    source_path = args.source

    # If source is a directory, find parquet/csv files
    if source_path.is_dir():
        data_files = list(source_path.glob("*.parquet")) + list(source_path.glob("*.csv"))
        if not data_files:
            return {"check": "duplicate_rate", "status": "skipped", "reason": "no data files in source directory"}
        source_path = data_files[0]

    return module.check_duplicates(source_path, key_columns, args.threshold)


def run_schema_drift_check(check_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    """Run the schema_drift check with provided arguments."""
    if not args.contract:
        return {"check": "schema_drift", "status": "skipped", "reason": "no --contract provided"}

    module = load_check_module(check_path)
    contract_columns = module.load_contract_schema(args.contract)

    if args.schema:
        actual_columns = module.load_actual_schema_from_json(args.schema)
    elif args.source:
        source_path = args.source
        if source_path.is_dir():
            data_files = list(source_path.glob("*.parquet")) + list(source_path.glob("*.csv"))
            if not data_files:
                return {"check": "schema_drift", "status": "skipped", "reason": "no data files in source directory"}
            source_path = data_files[0]
        actual_columns = module.load_actual_schema_from_source(source_path)
    else:
        return {"check": "schema_drift", "status": "skipped", "reason": "no --schema or --source provided"}

    return module.check_schema_drift(contract_columns, actual_columns, str(args.contract))


def run_replay_idempotency_check(check_path: Path, args: argparse.Namespace) -> dict[str, Any]:
    """Run the replay_idempotency check with provided arguments."""
    if not args.command:
        return {"check": "replay_idempotency", "status": "skipped", "reason": "no --command provided"}
    if not args.output:
        return {"check": "replay_idempotency", "status": "skipped", "reason": "no --output provided"}

    key_cols = args.key_columns or args.key
    if not key_cols:
        return {"check": "replay_idempotency", "status": "skipped", "reason": "no --key-columns provided"}

    module = load_check_module(check_path)
    key_columns = [k.strip() for k in key_cols.split(",")]
    return module.check_replay_idempotency(
        command=args.command,
        output_path=args.output,
        key_columns=key_columns,
        working_dir=None,
    )


CHECK_RUNNERS: dict[str, Any] = {
    "duplicate_rate": run_duplicate_rate_check,
    "schema_drift": run_schema_drift_check,
    "replay_idempotency": run_replay_idempotency_check,
}


def run_checks(args: argparse.Namespace) -> dict[str, Any]:
    """Discover and run all applicable checks for the skill."""
    check_files = discover_checks(args.skill)

    if not check_files:
        return {
            "skill": args.skill,
            "status": "error",
            "error": f"No checks found in skills/{args.skill}/checks/",
            "results": [],
        }

    # Filter to requested checks if specified
    if args.checks:
        requested = {c.strip() for c in args.checks.split(",")}
        check_files = [f for f in check_files if f.stem in requested]

    results: list[dict[str, Any]] = []
    start_time = time.time()

    for check_path in check_files:
        check_name = check_path.stem
        runner = CHECK_RUNNERS.get(check_name)

        if runner is None:
            # Unknown check — try to run its main() but skip gracefully
            results.append({
                "check": check_name,
                "status": "skipped",
                "reason": f"no runner registered for '{check_name}'",
            })
            continue

        try:
            result = runner(check_path, args)
            results.append(result)
        except Exception as exc:
            results.append({
                "check": check_name,
                "status": "error",
                "error": str(exc),
            })

    elapsed_ms = round((time.time() - start_time) * 1000, 1)

    # Aggregate status
    statuses = [r.get("status") for r in results]
    if "fail" in statuses:
        overall_status = "fail"
    elif "error" in statuses:
        overall_status = "error"
    elif all(s == "skipped" for s in statuses):
        overall_status = "skipped"
    else:
        overall_status = "pass"

    return {
        "skill": args.skill,
        "status": overall_status,
        "elapsed_ms": elapsed_ms,
        "checks_discovered": len(check_files),
        "checks_run": len([r for r in results if r.get("status") != "skipped"]),
        "checks_passed": len([r for r in results if r.get("status") == "pass"]),
        "checks_failed": len([r for r in results if r.get("status") == "fail"]),
        "checks_skipped": len([r for r in results if r.get("status") == "skipped"]),
        "results": results,
    }


def main() -> int:
    args = parse_args()
    report = run_checks(args)

    print(json.dumps(report, indent=2))

    # Write report to file if requested
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )

    # CI-friendly exit codes
    if report["status"] == "fail":
        return 1
    elif report["status"] == "error":
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
