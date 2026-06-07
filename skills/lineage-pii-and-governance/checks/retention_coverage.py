#!/usr/bin/env python3
"""Validate that all datasets in a catalog have retention policies defined.

Data retention is a regulatory and cost requirement.  Every dataset must have
a defined retention period, archive strategy, and deletion mechanism.  Datasets
without retention policies accumulate indefinitely, increasing storage costs
and creating compliance risk (GDPR right-to-erasure, CCPA deletion requests).

This check reads a data catalog file and verifies that each dataset entry
has a retention policy defined.

Usage:
    python checks/retention_coverage.py --catalog catalog.yaml
    python checks/retention_coverage.py --catalog catalog.json --require-delete-mechanism
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate retention policy coverage across a data catalog."
    )
    parser.add_argument(
        "--catalog",
        required=True,
        type=Path,
        help="Path to data catalog file (YAML or JSON).",
    )
    parser.add_argument(
        "--require-delete-mechanism",
        action="store_true",
        default=False,
        help="Require each dataset to specify a deletion mechanism.",
    )
    parser.add_argument(
        "--require-archive-strategy",
        action="store_true",
        default=False,
        help="Require each dataset to specify an archive strategy.",
    )
    return parser.parse_args()


def load_catalog(catalog_path: Path) -> list[dict[str, Any]]:
    """Load dataset catalog from YAML or JSON file."""
    if not catalog_path.exists():
        raise SystemExit(f"Catalog file not found: {catalog_path}")

    suffix = catalog_path.suffix.lower()
    text = catalog_path.read_text(encoding="utf-8")

    if suffix in {".yaml", ".yml"}:
        import yaml
        data = yaml.safe_load(text) or {}
    elif suffix == ".json":
        data = json.loads(text)
    else:
        raise SystemExit(f"Unsupported catalog format: {suffix}. Use .yaml or .json")

    # Handle various catalog structures
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "datasets" in data:
            return data["datasets"]
        if "catalog" in data:
            catalog = data["catalog"]
            if isinstance(catalog, list):
                return catalog
            if isinstance(catalog, dict) and "datasets" in catalog:
                return catalog["datasets"]
    raise SystemExit(f"Cannot find dataset list in catalog. Expected 'datasets' key or top-level list.")


def check_retention_coverage(
    catalog_path: Path,
    require_delete_mechanism: bool = False,
    require_archive_strategy: bool = False,
) -> dict[str, Any]:
    """Validate retention policy coverage and return structured evidence."""
    datasets = load_catalog(catalog_path)

    if not datasets:
        return {
            "check": "retention_coverage",
            "status": "error",
            "catalog": str(catalog_path),
            "error": "No datasets found in catalog.",
        }

    violations: list[dict[str, Any]] = []
    covered_datasets: list[str] = []

    for dataset in datasets:
        name = dataset.get("name", dataset.get("dataset", "unknown"))
        retention = dataset.get("retention", dataset.get("retention_policy"))
        issues: list[str] = []

        if retention is None:
            issues.append("no retention policy defined")
        elif isinstance(retention, dict):
            if not retention.get("period") and not retention.get("days") and not retention.get("retention_days"):
                issues.append("retention policy has no period/days specified")
            if require_delete_mechanism and not retention.get("delete_mechanism"):
                issues.append("no delete_mechanism specified")
            if require_archive_strategy and not retention.get("archive_strategy"):
                issues.append("no archive_strategy specified")
        elif isinstance(retention, str):
            # Simple string retention like "90 days" is acceptable
            pass
        else:
            issues.append(f"retention policy has unexpected format: {type(retention).__name__}")

        if issues:
            violations.append({"dataset": name, "issues": issues})
        else:
            covered_datasets.append(name)

    total = len(datasets)
    covered = len(covered_datasets)
    coverage_pct = (covered / total * 100) if total > 0 else 0.0
    status = "pass" if not violations else "fail"

    return {
        "check": "retention_coverage",
        "status": status,
        "catalog": str(catalog_path),
        "total_datasets": total,
        "datasets_with_retention": covered,
        "datasets_without_retention": len(violations),
        "coverage_percentage": round(coverage_pct, 1),
        "require_delete_mechanism": require_delete_mechanism,
        "require_archive_strategy": require_archive_strategy,
        "violations": violations,
        "covered_datasets": covered_datasets,
    }


def main() -> int:
    args = parse_args()
    result = check_retention_coverage(
        catalog_path=args.catalog,
        require_delete_mechanism=args.require_delete_mechanism,
        require_archive_strategy=args.require_archive_strategy,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
