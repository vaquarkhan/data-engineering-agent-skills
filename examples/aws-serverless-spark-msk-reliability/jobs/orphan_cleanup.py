#!/usr/bin/env python3
"""Detect abandoned staging prefixes for serverless Spark runs."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir", default="build")
    parser.add_argument("--older-than-minutes", type=int, default=60)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    workdir = Path(args.workdir)
    checkpoint_root = workdir / "checkpoints"
    now = datetime.now(timezone.utc)
    orphans: list[str] = []

    if not checkpoint_root.exists():
        print("No checkpoints found")
        return 0

    for manifest_file in checkpoint_root.glob("*/manifest.json"):
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        status = manifest.get("status")
        updated_at = manifest.get("updated_at")
        if status in {"in_progress", "rolled_back"} and updated_at:
            age_minutes = (now - parse_ts(updated_at)).total_seconds() / 60
            if age_minutes >= args.older_than_minutes:
                orphans.append(str(manifest.get("staging_prefix", manifest_file.parent)))

    if not orphans:
        print("No orphan staging prefixes detected")
        return 0

    print("Orphan staging prefixes:")
    for orphan in orphans:
        print(f"- {orphan}")
        if not args.dry_run:
            path = Path(orphan)
            if path.exists():
                for child in path.glob("*"):
                    child.unlink()
                path.rmdir()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
