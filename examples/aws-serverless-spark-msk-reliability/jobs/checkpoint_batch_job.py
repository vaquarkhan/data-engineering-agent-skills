#!/usr/bin/env python3
"""Local proof harness for serverless Spark checkpoint, staging, and publish gating."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_events(path: Path) -> list[dict]:
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            events.append(json.loads(line))
    return events


def partition_key(event: dict) -> str:
    return str(event["event_date"])


def aggregate_partition(events: list[dict]) -> list[dict]:
    totals: dict[tuple[str, str], dict] = defaultdict(lambda: {"total_amount": 0.0, "event_count": 0})
    for event in events:
        key = (event["order_id"], event["event_date"])
        totals[key]["total_amount"] += float(event["amount"])
        totals[key]["event_count"] += 1
    rows = []
    for (order_id, event_date), metrics in sorted(totals.items()):
        rows.append(
            {
                "order_id": order_id,
                "event_date": event_date,
                "total_amount": round(metrics["total_amount"], 2),
                "event_count": metrics["event_count"],
            }
        )
    return rows


def manifest_path(workdir: Path, run_id: str) -> Path:
    return workdir / "checkpoints" / run_id / "manifest.json"


def write_manifest(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def read_manifest(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_publish(workdir: Path, rows: list[dict]) -> Path:
    publish_dir = workdir / "publish"
    publish_dir.mkdir(parents=True, exist_ok=True)
    output = publish_dir / "aggregated-events.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    (publish_dir / "_SUCCESS").write_text("ok\n", encoding="utf-8")
    return output


def run_job(
    input_path: Path,
    workdir: Path,
    run_id: str,
    fail_after_partitions: int | None,
    resume: bool,
) -> int:
    events = load_events(input_path)
    by_partition: dict[str, list[dict]] = defaultdict(list)
    for event in events:
        by_partition[partition_key(event)].append(event)

    manifest_file = manifest_path(workdir, run_id)
    manifest = read_manifest(manifest_file) if resume else None
    completed = set(manifest.get("completed_partitions", [])) if manifest else set()
    aggregated_rows: list[dict] = []

    if manifest and manifest.get("status") == "ready_to_publish":
        publish_file = workdir / "publish" / "aggregated-events.jsonl"
        if publish_file.exists():
            print(f"Run {run_id} already published at {publish_file}")
            return 0

    staging_root = workdir / "staging" / run_id
    staging_root.mkdir(parents=True, exist_ok=True)

    for partition in sorted(by_partition):
        if partition in completed:
            staging_file = staging_root / f"{partition}.jsonl"
            if staging_file.exists():
                for line in staging_file.read_text(encoding="utf-8").splitlines():
                    if line.strip():
                        aggregated_rows.append(json.loads(line))
            continue

        partition_rows = aggregate_partition(by_partition[partition])
        staging_file = staging_root / f"{partition}.jsonl"
        with staging_file.open("w", encoding="utf-8") as handle:
            for row in partition_rows:
                handle.write(json.dumps(row) + "\n")
        aggregated_rows.extend(partition_rows)
        completed.add(partition)

        write_manifest(
            manifest_file,
            {
                "run_id": run_id,
                "started_at": manifest.get("started_at", utc_now()) if manifest else utc_now(),
                "updated_at": utc_now(),
                "completed_partitions": sorted(completed),
                "status": "in_progress",
                "staging_prefix": str(staging_root),
            },
        )

        if fail_after_partitions is not None and len(completed) >= fail_after_partitions:
            remaining = sorted(set(by_partition) - completed)
            if remaining:
                write_manifest(
                    manifest_file,
                    {
                        "run_id": run_id,
                        "started_at": manifest.get("started_at", utc_now()) if manifest else utc_now(),
                        "updated_at": utc_now(),
                        "completed_partitions": sorted(completed),
                        "status": "rolled_back",
                        "staging_prefix": str(staging_root),
                        "note": f"timeout after {fail_after_partitions} partitions; resume required",
                    },
                )
                print(f"Simulated timeout after partition {partition}; remaining={remaining}")
                return 2

    deduped: dict[tuple[str, str], dict] = {}
    for row in aggregated_rows:
        deduped[(row["order_id"], row["event_date"])] = row
    final_rows = [deduped[key] for key in sorted(deduped)]

    write_manifest(
        manifest_file,
        {
            "run_id": run_id,
            "started_at": manifest.get("started_at", utc_now()) if manifest else utc_now(),
            "updated_at": utc_now(),
            "completed_partitions": sorted(completed),
            "status": "ready_to_publish",
            "staging_prefix": str(staging_root),
        },
    )
    publish_file = write_publish(workdir, final_rows)
    print(f"Published {len(final_rows)} rows to {publish_file}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--workdir", default="build")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--fail-after-partitions", type=int, default=None)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    return run_job(
        Path(args.input),
        Path(args.workdir),
        args.run_id,
        args.fail_after_partitions,
        args.resume,
    )


if __name__ == "__main__":
    raise SystemExit(main())
