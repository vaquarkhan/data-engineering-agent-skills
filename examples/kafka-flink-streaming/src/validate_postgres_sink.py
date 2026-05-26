import argparse
from decimal import Decimal

import psycopg


EXPECTED_ROWS = [
    ("created", 2, 2, Decimal("205.00")),
    ("paid", 1, 1, Decimal("125.00")),
    ("created", 1, 1, Decimal("40.00")),
    ("paid", 1, 1, Decimal("40.00")),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--postgres-dsn", default="postgresql://stream:stream@localhost:15432/stream")
    args = parser.parse_args()

    with psycopg.connect(args.postgres_dsn) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                select event_type, unique_orders, total_events, gross_amount
                from windowed_orders
                order by window_start, event_type
                """
            )
            rows = cursor.fetchall()

    if len(rows) != len(EXPECTED_ROWS):
        raise SystemExit(
            f"Postgres sink validation failed: expected {len(EXPECTED_ROWS)} rows, found {len(rows)}"
        )

    for actual, expected in zip(rows, EXPECTED_ROWS, strict=True):
        if (
            actual[0] != expected[0]
            or actual[1] != expected[1]
            or actual[2] != expected[2]
            or Decimal(str(actual[3])) != expected[3]
        ):
            raise SystemExit(
                f"Postgres sink validation failed: expected {expected}, found {actual}"
            )

    print("Postgres sink validation passed; Kafka sandbox output matches expected window aggregates.")


if __name__ == "__main__":
    main()
