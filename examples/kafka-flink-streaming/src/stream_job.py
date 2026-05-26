import argparse
import json
from collections import defaultdict
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from pathlib import Path


REQUIRED_FIELDS = {
    "event_id",
    "order_id",
    "customer_id",
    "event_type",
    "amount",
    "event_ts",
}


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def floor_window(ts: datetime, window_seconds: int) -> datetime:
    floored = int(ts.timestamp()) // window_seconds * window_seconds
    return datetime.fromtimestamp(floored, tz=UTC)


def load_events(path: Path) -> list[dict]:
    events: list[dict] = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        event = json.loads(line)
        missing = sorted(REQUIRED_FIELDS - event.keys())
        if missing:
            raise SystemExit(f"row {index} is missing required fields: {', '.join(missing)}")
        event["event_ts"] = parse_timestamp(event["event_ts"])
        event["amount"] = Decimal(str(event["amount"]))
        events.append(event)
    return events


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--checkpoint-output", required=True)
    parser.add_argument("--window-seconds", type=int, default=300)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    checkpoint_path = Path(args.checkpoint_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)

    source_events = load_events(input_path)
    deduplicated_events: dict[str, dict] = {}
    duplicate_event_ids: list[str] = []
    for event in source_events:
        event_id = event["event_id"]
        if event_id in deduplicated_events:
            duplicate_event_ids.append(event_id)
        deduplicated_events[event_id] = event

    windows: dict[tuple[datetime, str], dict] = defaultdict(
        lambda: {"orders": set(), "total_events": 0, "gross_amount": Decimal("0")}
    )

    for event in deduplicated_events.values():
        window_start = floor_window(event["event_ts"], args.window_seconds)
        key = (window_start, event["event_type"])
        windows[key]["orders"].add(event["order_id"])
        windows[key]["total_events"] += 1
        windows[key]["gross_amount"] += event["amount"]

    sink_rows: list[dict] = []
    for (window_start, event_type), metrics in sorted(windows.items()):
        sink_rows.append(
            {
                "window_start": window_start.isoformat().replace("+00:00", "Z"),
                "window_end": (
                    window_start + timedelta(seconds=args.window_seconds)
                ).isoformat().replace("+00:00", "Z"),
                "event_type": event_type,
                "unique_orders": len(metrics["orders"]),
                "total_events": metrics["total_events"],
                "gross_amount": f"{metrics['gross_amount']:.2f}",
            }
        )

    with output_path.open("w", encoding="utf-8") as handle:
        for row in sink_rows:
            handle.write(json.dumps(row) + "\n")

    checkpoint_path.write_text(
        json.dumps(
            {
                "source_event_count": len(source_events),
                "deduplicated_event_count": len(deduplicated_events),
                "duplicate_event_ids": sorted(set(duplicate_event_ids)),
                "window_count": len(sink_rows),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        f"Processed {len(source_events)} source event(s) into {len(sink_rows)} sink window(s); deduplicated to {len(deduplicated_events)} unique event(s)."
    )


if __name__ == "__main__":
    main()
