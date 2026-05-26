import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as src, output_path.open("w", encoding="utf-8") as dst:
        for line in src:
            record = json.loads(line)
            normalized = {
                "customer_id": record["id"],
                "customer_name": record["name"].strip(),
                "country": record.get("country", "unknown").upper(),
                "updated_at": record["updated_at"],
            }
            dst.write(json.dumps(normalized) + "\n")


if __name__ == "__main__":
    main()
