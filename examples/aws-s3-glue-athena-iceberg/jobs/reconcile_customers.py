import argparse
import json
from pathlib import Path


def load_json_lines(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--normalized", required=True)
    args = parser.parse_args()

    source_rows = load_json_lines(Path(args.source))
    normalized_rows = load_json_lines(Path(args.normalized))

    if len(source_rows) != len(normalized_rows):
        raise SystemExit(
            f"Reconciliation failed: source has {len(source_rows)} rows but normalized output has {len(normalized_rows)} rows"
        )

    source_by_key = {(row["id"], row["updated_at"]): row for row in source_rows}
    normalized_by_key = {
        (row["customer_id"], row["updated_at"]): row for row in normalized_rows
    }

    if set(source_by_key) != set(normalized_by_key):
        missing = sorted(set(source_by_key) ^ set(normalized_by_key))
        raise SystemExit(f"Reconciliation failed: mismatched business keys {missing}")

    for key, source_row in source_by_key.items():
        normalized_row = normalized_by_key[key]
        if normalized_row["customer_name"] != source_row["name"].strip():
            raise SystemExit(f"Reconciliation failed for {key}: customer_name not normalized correctly")
        if normalized_row["country"] != source_row.get("country", "unknown").upper():
            raise SystemExit(f"Reconciliation failed for {key}: country normalization mismatch")

    print(
        f"Reconciliation passed for {len(normalized_rows)} row(s); source-to-curated mapping is complete."
    )


if __name__ == "__main__":
    main()
