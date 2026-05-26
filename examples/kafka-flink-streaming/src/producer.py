import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--topic-log", required=True)
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input)
    topic_log = Path(args.topic_log)
    topic_log.parent.mkdir(parents=True, exist_ok=True)

    payload = input_path.read_text(encoding="utf-8")
    if args.reset:
        topic_log.write_text(payload, encoding="utf-8")
    else:
        with topic_log.open("a", encoding="utf-8") as handle:
            if topic_log.stat().st_size > 0 and not payload.startswith("\n"):
                handle.write("")
            handle.write(payload)

    line_count = len([line for line in payload.splitlines() if line.strip()])
    print(f"Produced {line_count} event(s) into simulated topic log {topic_log}.")


if __name__ == "__main__":
    main()
