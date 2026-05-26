import argparse
import json
from collections import defaultdict
from datetime import UTC, datetime, timedelta
from decimal import Decimal

from kafka import KafkaConsumer
import psycopg


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def floor_window(ts: datetime, window_seconds: int) -> datetime:
    floored = int(ts.timestamp()) // window_seconds * window_seconds
    return datetime.fromtimestamp(floored, tz=UTC)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-servers", default="localhost:19092")
    parser.add_argument("--topic", default="order-events")
    parser.add_argument("--group-id", default="order-events-demo")
    parser.add_argument("--postgres-dsn", default="postgresql://stream:stream@localhost:15432/stream")
    parser.add_argument("--window-seconds", type=int, default=300)
    parser.add_argument("--idle-timeout-ms", type=int, default=3000)
    args = parser.parse_args()

    consumer = KafkaConsumer(
        args.topic,
        bootstrap_servers=args.bootstrap_servers,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id=args.group_id,
        consumer_timeout_ms=args.idle_timeout_ms,
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    )

    deduplicated_events: dict[str, dict] = {}
    duplicate_event_ids: list[str] = []
    try:
        for message in consumer:
            event = message.value
            event["event_ts"] = parse_timestamp(event["event_ts"])
            event["amount"] = Decimal(str(event["amount"]))
            event_id = event["event_id"]
            if event_id in deduplicated_events:
                duplicate_event_ids.append(event_id)
            deduplicated_events[event_id] = event
    finally:
        consumer.close()

    windows: dict[tuple[datetime, str], dict] = defaultdict(
        lambda: {"orders": set(), "total_events": 0, "gross_amount": Decimal("0")}
    )
    for event in deduplicated_events.values():
        window_start = floor_window(event["event_ts"], args.window_seconds)
        key = (window_start, event["event_type"])
        windows[key]["orders"].add(event["order_id"])
        windows[key]["total_events"] += 1
        windows[key]["gross_amount"] += event["amount"]

    rows = []
    for (window_start, event_type), metrics in sorted(windows.items()):
        rows.append(
            (
                window_start,
                window_start + timedelta(seconds=args.window_seconds),
                event_type,
                len(metrics["orders"]),
                metrics["total_events"],
                metrics["gross_amount"],
            )
        )

    with psycopg.connect(args.postgres_dsn) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                create table if not exists windowed_orders (
                    window_start timestamptz not null,
                    window_end timestamptz not null,
                    event_type text not null,
                    unique_orders integer not null,
                    total_events integer not null,
                    gross_amount numeric(18,2) not null
                )
                """
            )
            cursor.execute("truncate table windowed_orders")
            cursor.executemany(
                """
                insert into windowed_orders (
                    window_start, window_end, event_type, unique_orders, total_events, gross_amount
                ) values (%s, %s, %s, %s, %s, %s)
                """,
                rows,
            )
        connection.commit()

    print(
        f"Consumed {len(deduplicated_events) + len(duplicate_event_ids)} event(s) from Kafka and wrote {len(rows)} windowed row(s) to Postgres."
    )


if __name__ == "__main__":
    main()
