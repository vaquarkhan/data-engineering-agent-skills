import argparse
import json
from pathlib import Path


EXPECTED_ROWS = {
    ("2026-05-01T00:00:00Z", "created"): {
        "unique_orders": 2,
        "total_events": 2,
        "gross_amount": "205.00",
    },
    ("2026-05-01T00:00:00Z", "paid"): {
        "unique_orders": 1,
        "total_events": 1,
        "gross_amount": "125.00",
    },
    ("2026-05-01T00:05:00Z", "created"): {
        "unique_orders": 1,
        "total_events": 1,
        "gross_amount": "40.00",
    },
    ("2026-05-01T00:05:00Z", "paid"): {
        "unique_orders": 1,
        "total_events": 1,
        "gross_amount": "40.00",
    },
}


def load_json_lines(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sink", required=True)
    parser.add_argument("--checkpoint", required=True)
    args = parser.parse_args()

    sink_rows = load_json_lines(Path(args.sink))
    checkpoint = json.loads(Path(args.checkpoint).read_text(encoding="utf-8"))

    actual = {(row["window_start"], row["event_type"]): row for row in sink_rows}
    if set(actual) != set(EXPECTED_ROWS):
        raise SystemExit(
            f"Sink validation failed: expected keys {sorted(EXPECTED_ROWS)} but found {sorted(actual)}"
        )

    for key, expected in EXPECTED_ROWS.items():
        row = actual[key]
        for field, expected_value in expected.items():
            if row[field] != expected_value:
                raise SystemExit(
                    f"Sink validation failed for {key}: expected {field}={expected_value}, found {row[field]}"
                )

    if checkpoint["deduplicated_event_count"] != 5:
        raise SystemExit(
            f"Checkpoint validation failed: expected 5 deduplicated events, found {checkpoint['deduplicated_event_count']}"
        )
    if checkpoint["window_count"] != 4:
        raise SystemExit(
            f"Checkpoint validation failed: expected 4 windows, found {checkpoint['window_count']}"
        )
    if "e-5" not in checkpoint["duplicate_event_ids"]:
        raise SystemExit("Checkpoint validation failed: expected duplicate event_id e-5 to be recorded")

    print("Streaming sink validation passed; window outputs and replay-safe deduplication match expectations.")


if __name__ == "__main__":
    main()
