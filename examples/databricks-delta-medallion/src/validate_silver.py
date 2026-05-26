import argparse
import json
from pathlib import Path


EXPECTED_ROWS = {
    "e-1": {
        "customer_id": "c-100",
        "event_type": "purchase",
        "event_ts": "2026-05-01T00:00:00Z",
    },
    "e-2": {
        "customer_id": "c-101",
        "event_type": "refund",
        "event_ts": "2026-05-01T01:00:00Z",
    },
}


def load_rows(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--silver", required=True)
    args = parser.parse_args()

    rows = load_rows(Path(args.silver))
    if len(rows) != len(EXPECTED_ROWS):
        raise SystemExit(
            f"Silver validation failed: expected {len(EXPECTED_ROWS)} rows, found {len(rows)}"
        )

    for row in rows:
        expected = EXPECTED_ROWS.get(row["event_id"])
        if expected is None:
            raise SystemExit(f"Silver validation failed: unexpected event_id {row['event_id']}")
        for field, value in expected.items():
            if row[field] != value:
                raise SystemExit(
                    f"Silver validation failed for {row['event_id']}: expected {field}={value}, found {row[field]}"
                )

    print("Silver validation passed; conformed rows match the expected medallion output.")


if __name__ == "__main__":
    main()
