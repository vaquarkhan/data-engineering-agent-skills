import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--silver", required=True)
    args = parser.parse_args()

    path = Path(args.silver)
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    if len(rows) != 1 or rows[0]["event_id"] != "e-0":
        raise SystemExit(
            "Rollback validation failed: expected the previous snapshot row with event_id e-0"
        )

    print("Rollback validation passed; previous snapshot is active again.")


if __name__ == "__main__":
    main()
