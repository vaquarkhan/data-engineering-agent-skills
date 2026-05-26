import argparse
import json
from pathlib import Path

from kafka import KafkaProducer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--bootstrap-servers", default="localhost:19092")
    parser.add_argument("--topic", default="order-events")
    args = parser.parse_args()

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap_servers,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )
    count = 0
    try:
        for line in Path(args.input).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            producer.send(args.topic, json.loads(line))
            count += 1
        producer.flush()
    finally:
        producer.close()

    print(f"Produced {count} event(s) to Kafka topic {args.topic} at {args.bootstrap_servers}.")


if __name__ == "__main__":
    main()
