from __future__ import annotations

import unittest
from datetime import datetime, timezone
from decimal import Decimal
from tempfile import TemporaryDirectory
from pathlib import Path

from scripts.validate_dataset_contract import (
    build_schema_map,
    load_records_from_file,
    normalize_value,
    parse_contract,
    validate_contract_compatibility,
    validate_rows,
)


class ValidateDatasetContractTests(unittest.TestCase):
    def test_csv_unique_keys_are_normalized_by_schema(self) -> None:
        contract = {
            "name": "daily_metrics",
            "schema": {
                "columns": [
                    {"name": "entity_id", "type": "string", "nullable": False},
                    {"name": "metric_value", "type": "decimal(18,2)", "nullable": False},
                ]
            },
            "quality": {"checks": [{"unique": ["entity_id", "metric_value"]}]},
            "freshness": {},
        }
        rows = [
            {"entity_id": "a", "metric_value": "125.00"},
            {"entity_id": "a", "metric_value": Decimal("125.0")},
        ]

        with self.assertRaises(SystemExit):
            validate_rows(contract, rows, None)

    def test_previous_contract_additive_compatibility(self) -> None:
        previous = {
            "name": "silver_customer_events",
            "schema": {
                "columns": [
                    {"name": "event_id", "type": "string", "nullable": False},
                    {"name": "event_type", "type": "string", "nullable": False},
                ]
            },
            "compatibility": {"change_policy": "additive_by_default"},
        }
        current = {
            "name": "silver_customer_events",
            "schema": {
                "columns": [
                    {"name": "event_id", "type": "string", "nullable": False},
                    {"name": "event_type", "type": "string", "nullable": False},
                    {"name": "event_ts", "type": "timestamp", "nullable": False},
                ]
            },
            "compatibility": {"change_policy": "additive_by_default"},
        }

        self.assertEqual(validate_contract_compatibility(current, previous), [])

    def test_previous_contract_detects_removed_column(self) -> None:
        previous = {
            "name": "silver_customer_events",
            "schema": {"columns": [{"name": "event_id", "type": "string", "nullable": False}]},
            "compatibility": {"change_policy": "additive_by_default"},
        }
        current = {
            "name": "silver_customer_events",
            "schema": {"columns": []},
            "compatibility": {"change_policy": "additive_by_default"},
        }

        errors = validate_contract_compatibility(current, previous)
        self.assertTrue(any("was removed" in error for error in errors))

    def test_load_records_from_csv(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "dataset.csv"
            csv_path.write_text("entity_id,metric_value\nx,12.50\n", encoding="utf-8")
            rows = load_records_from_file(csv_path)
            self.assertEqual(rows, [{"entity_id": "x", "metric_value": "12.50"}])

    def test_normalize_timestamp_value(self) -> None:
        self.assertEqual(
            normalize_value("2026-05-01T00:00:00Z", "timestamp"),
            datetime(2026, 5, 1, 0, 0, tzinfo=timezone.utc).isoformat(),
        )


if __name__ == "__main__":
    unittest.main()
