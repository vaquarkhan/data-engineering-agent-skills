#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, NoReturn

import duckdb
import yaml


@dataclass
class ValidationResult:
    contract_name: str
    row_count: int
    latest_freshness_value: str | None


def fail(message: str) -> NoReturn:
    raise SystemExit(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate sample data against a dataset contract YAML."
    )
    parser.add_argument("--contract", required=True, type=Path, help="Path to contract YAML")

    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--data", type=Path, help="Path to CSV, JSONL, or NDJSON data file")
    source.add_argument("--duckdb", type=Path, help="Path to DuckDB database file")

    parser.add_argument(
        "--query",
        help="SQL query used with --duckdb to fetch the dataset to validate",
    )
    parser.add_argument(
        "--reference-time",
        help="Reference timestamp used for freshness checks, ISO 8601 format",
    )
    parser.add_argument(
        "--previous-contract",
        type=Path,
        help="Optional path to the previous contract version for compatibility validation",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        help="Optional path to write a JSON validation summary",
    )
    return parser.parse_args()


def parse_contract(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    contract = payload.get("dataset_contract")
    if not isinstance(contract, dict):
        fail(f"{path} is missing a top-level dataset_contract object")
    return contract


def load_records_from_file(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix in {".jsonl", ".ndjson"}:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    if suffix == ".csv":
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    fail(f"Unsupported data file format for {path}; use .jsonl, .ndjson, or .csv")


def build_schema_map(contract: dict[str, Any]) -> dict[str, str]:
    columns = contract.get("schema", {}).get("columns", [])
    return {
        column["name"]: str(column.get("type", "string"))
        for column in columns
        if isinstance(column, dict) and column.get("name")
    }


def load_records_from_duckdb(database_path: Path, query: str | None) -> list[dict[str, Any]]:
    if not query:
        fail("--query is required when validating from DuckDB")
    connection = duckdb.connect(str(database_path))
    try:
        cursor = connection.execute(query)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    finally:
        connection.close()


def is_null_like(value: Any) -> bool:
    return value is None or (isinstance(value, str) and value.strip() == "")


def parse_temporal_value(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, date):
        return datetime.combine(value, time.min, tzinfo=timezone.utc)

    text = str(value).strip()
    if not text:
        raise ValueError("empty temporal value")
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"

    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        parsed_date = date.fromisoformat(text)
        return datetime.combine(parsed_date, time.min, tzinfo=timezone.utc)

    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def parse_reference_time(raw_value: str | None) -> datetime | None:
    if raw_value is None:
        return None
    return parse_temporal_value(raw_value)


def normalize_value(value: Any, type_name: str) -> Any:
    if is_null_like(value):
        return None

    normalized = type_name.lower()
    if normalized.startswith("string"):
        return str(value).strip()
    if normalized.startswith("date"):
        parsed = parse_temporal_value(value)
        return parsed.date().isoformat()
    if normalized.startswith("timestamp"):
        parsed = parse_temporal_value(value)
        return parsed.isoformat()
    if normalized.startswith("decimal") or normalized.startswith("numeric"):
        return Decimal(str(value))
    if normalized.startswith("int") or normalized.startswith("bigint"):
        return int(str(value))
    if normalized.startswith("float") or normalized.startswith("double"):
        return Decimal(str(value))
    if normalized.startswith("bool"):
        lowered = str(value).strip().lower()
        if lowered in {"true", "1", "yes"}:
            return True
        if lowered in {"false", "0", "no"}:
            return False
        raise ValueError(f"unsupported boolean value {value!r}")
    return value


def validate_value_type(value: Any, type_name: str) -> bool:
    if is_null_like(value):
        return True

    try:
        normalize_value(value, type_name)
        return True
    except (InvalidOperation, ValueError):
        return False


def validate_contract_compatibility(
    current_contract: dict[str, Any], previous_contract: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    current_name = current_contract.get("name")
    previous_name = previous_contract.get("name")
    if current_name and previous_name and current_name != previous_name:
        errors.append(
            f"contract name changed from {previous_name!r} to {current_name!r}; compatibility checks require the same dataset name"
        )

    policy = str(
        current_contract.get("compatibility", {}).get(
            "change_policy",
            previous_contract.get("compatibility", {}).get("change_policy", "additive_by_default"),
        )
    )
    if policy != "additive_by_default":
        return errors

    current_columns = {
        column["name"]: column
        for column in current_contract.get("schema", {}).get("columns", [])
        if isinstance(column, dict) and column.get("name")
    }
    previous_columns = {
        column["name"]: column
        for column in previous_contract.get("schema", {}).get("columns", [])
        if isinstance(column, dict) and column.get("name")
    }

    for name, previous_column in previous_columns.items():
        current_column = current_columns.get(name)
        if current_column is None:
            errors.append(f"additive compatibility violation: column '{name}' was removed")
            continue

        previous_type = str(previous_column.get("type", "string")).lower()
        current_type = str(current_column.get("type", "string")).lower()
        if previous_type != current_type:
            errors.append(
                f"additive compatibility violation: column '{name}' changed type from {previous_type} to {current_type}"
            )

        if bool(previous_column.get("nullable", True)) and not bool(
            current_column.get("nullable", True)
        ):
            errors.append(
                f"additive compatibility violation: column '{name}' changed from nullable to non-nullable"
            )

    return errors


def validate_rows(contract: dict[str, Any], rows: list[dict[str, Any]], reference_time: datetime | None) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    contract_name = contract.get("name", "unnamed_dataset_contract")
    if not rows:
        errors.append("dataset is empty")

    schema = contract.get("schema", {})
    columns = schema.get("columns", [])
    schema_map = build_schema_map(contract)
    column_names = [column.get("name") for column in columns if column.get("name")]

    for column in column_names:
        if rows and any(column not in row for row in rows):
            errors.append(f"missing schema column in data: {column}")

    for column in columns:
        name = column.get("name")
        if not name:
            continue
        type_name = str(column.get("type", "string"))
        nullable = bool(column.get("nullable", True))

        for index, row in enumerate(rows, start=1):
            value = row.get(name)
            if not nullable and is_null_like(value):
                errors.append(f"row {index}: column '{name}' is null but contract marks it non-nullable")
            if not validate_value_type(value, type_name):
                errors.append(f"row {index}: column '{name}' value {value!r} does not match type {type_name}")

    checks = contract.get("quality", {}).get("checks", [])
    for check in checks:
        if not isinstance(check, dict):
            continue

        if "not_null" in check:
            for column in check["not_null"]:
                null_rows = [
                    index
                    for index, row in enumerate(rows, start=1)
                    if is_null_like(row.get(column))
                ]
                if null_rows:
                    errors.append(
                        f"not_null check failed for '{column}' on rows {', '.join(map(str, null_rows[:10]))}"
                    )

        if "unique" in check:
            key_columns = check["unique"]
            seen: dict[tuple[Any, ...], int] = {}
            duplicates: list[str] = []
            for index, row in enumerate(rows, start=1):
                try:
                    key = tuple(
                        normalize_value(row.get(column), schema_map.get(column, "string"))
                        for column in key_columns
                    )
                except (InvalidOperation, ValueError) as exc:
                    errors.append(
                        f"unique check could not normalize key {key_columns} on row {index}: {exc}"
                    )
                    continue
                if key in seen:
                    duplicates.append(
                        f"rows {seen[key]} and {index} share key {dict(zip(key_columns, key))}"
                    )
                else:
                    seen[key] = index
            if duplicates:
                errors.append(f"unique check failed for {key_columns}: {'; '.join(duplicates[:5])}")

        if "row_count_min" in check and len(rows) < int(check["row_count_min"]):
            errors.append(
                f"row_count_min check failed: expected at least {check['row_count_min']} rows, found {len(rows)}"
            )

    freshness = contract.get("freshness", {})
    latest_freshness_value: str | None = None
    freshness_field = freshness.get("field")
    if freshness_field:
        temporal_values: list[datetime] = []
        for index, row in enumerate(rows, start=1):
            if is_null_like(row.get(freshness_field)):
                errors.append(f"row {index}: freshness field '{freshness_field}' is null")
                continue
            try:
                temporal_values.append(parse_temporal_value(row[freshness_field]))
            except ValueError as exc:
                errors.append(f"row {index}: freshness field '{freshness_field}' is invalid: {exc}")

        if temporal_values:
            latest = max(temporal_values)
            latest_freshness_value = latest.isoformat()
            max_age_hours = freshness.get("max_age_hours")
            max_age_days = freshness.get("max_age_days")
            if reference_time and (max_age_hours is not None or max_age_days is not None):
                allowed_age = timedelta(
                    hours=float(max_age_hours or 0),
                    days=float(max_age_days or 0),
                )
                if reference_time - latest > allowed_age:
                    errors.append(
                        f"freshness check failed for '{freshness_field}': latest value {latest.isoformat()} is older than allowed age {allowed_age}"
                    )
    elif freshness:
        warnings.append("freshness section is present but no freshness.field was defined")

    if warnings:
        for warning in warnings:
            print(f"Warning: {warning}")

    if errors:
        print(f"Contract validation failed for {contract_name}:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(
        f"Validated contract '{contract_name}' against {len(rows)} row(s)"
        + (f"; latest freshness value: {latest_freshness_value}" if latest_freshness_value else "")
    )
    return ValidationResult(
        contract_name=contract_name,
        row_count=len(rows),
        latest_freshness_value=latest_freshness_value,
    )


def main() -> int:
    args = parse_args()
    contract = parse_contract(args.contract)
    reference_time = parse_reference_time(args.reference_time)
    previous_contract = None

    if getattr(args, "previous_contract", None):
        previous_contract = parse_contract(args.previous_contract)
        compatibility_errors = validate_contract_compatibility(contract, previous_contract)
        if compatibility_errors:
            print(f"Contract compatibility failed for {contract.get('name', 'unnamed_dataset_contract')}:")
            for error in compatibility_errors:
                print(f"- {error}")
            return 1

    if args.data:
        rows = load_records_from_file(args.data)
    else:
        rows = load_records_from_duckdb(args.duckdb, args.query)

    result = validate_rows(contract, rows, reference_time)

    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(
            json.dumps(
                {
                    "contract_name": result.contract_name,
                    "row_count": result.row_count,
                    "latest_freshness_value": result.latest_freshness_value,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
