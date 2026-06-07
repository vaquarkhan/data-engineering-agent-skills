#!/usr/bin/env python3
"""Validate sample events against a JSON schema definition.

In event-driven architectures, schema validation ensures that producers
emit events conforming to the agreed contract.  Schema violations cause
consumer deserialization failures, silent data loss, or corrupted state.

This check reads a file of sample events (JSONL) and validates each
against a provided JSON Schema file.

Usage:
    python checks/event_schema_valid.py --events events.jsonl --schema event-schema.json
    python checks/event_schema_valid.py --events events.jsonl --schema schema.json --max-errors 10
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate sample events against a JSON schema."
    )
    parser.add_argument(
        "--events",
        required=True,
        type=Path,
        help="Path to events file (JSONL or JSON array).",
    )
    parser.add_argument(
        "--schema",
        required=True,
        type=Path,
        help="Path to JSON Schema file.",
    )
    parser.add_argument(
        "--max-errors",
        type=int,
        default=20,
        help="Maximum number of errors to report. Default: 20",
    )
    return parser.parse_args()


def load_events(events_path: Path) -> list[dict[str, Any]]:
    """Load events from JSONL or JSON array file."""
    if not events_path.exists():
        raise SystemExit(f"Events file not found: {events_path}")

    text = events_path.read_text(encoding="utf-8").strip()

    # Try JSON array first
    if text.startswith("["):
        return json.loads(text)

    # Otherwise treat as JSONL
    events: list[dict[str, Any]] = []
    for line_num, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON at line {line_num}: {e}")
    return events


def load_schema(schema_path: Path) -> dict[str, Any]:
    """Load JSON Schema from file."""
    if not schema_path.exists():
        raise SystemExit(f"Schema file not found: {schema_path}")
    return json.loads(schema_path.read_text(encoding="utf-8"))


def validate_event(event: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Validate a single event against the schema using basic checks.

    Implements a lightweight JSON Schema subset validator (type, required,
    properties, enum) without requiring jsonschema library.
    """
    errors: list[str] = []

    # Check required fields
    required = schema.get("required", [])
    for field in required:
        if field not in event:
            errors.append(f"Missing required field: '{field}'")

    # Check property types
    properties = schema.get("properties", {})
    for field, prop_schema in properties.items():
        if field not in event:
            continue

        value = event[field]
        expected_type = prop_schema.get("type")

        if expected_type and not _type_matches(value, expected_type):
            errors.append(
                f"Field '{field}': expected type '{expected_type}', "
                f"got '{type(value).__name__}' (value: {_truncate(value)})"
            )

        # Enum validation
        if "enum" in prop_schema and value not in prop_schema["enum"]:
            errors.append(
                f"Field '{field}': value '{value}' not in enum {prop_schema['enum']}"
            )

        # Pattern validation
        if "pattern" in prop_schema and isinstance(value, str):
            if not re.match(prop_schema["pattern"], value):
                errors.append(
                    f"Field '{field}': value '{_truncate(value)}' "
                    f"does not match pattern '{prop_schema['pattern']}'"
                )

        # Minimum/maximum validation
        if "minimum" in prop_schema and isinstance(value, (int, float)):
            if value < prop_schema["minimum"]:
                errors.append(f"Field '{field}': value {value} < minimum {prop_schema['minimum']}")
        if "maximum" in prop_schema and isinstance(value, (int, float)):
            if value > prop_schema["maximum"]:
                errors.append(f"Field '{field}': value {value} > maximum {prop_schema['maximum']}")

    return errors


def _type_matches(value: Any, expected_type: str) -> bool:
    """Check if a Python value matches a JSON Schema type."""
    if value is None:
        return expected_type == "null"
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True  # Unknown type, pass
    # bool is subclass of int in Python, handle explicitly
    if expected_type == "integer" and isinstance(value, bool):
        return False
    return isinstance(value, expected)


def _truncate(value: Any, max_len: int = 50) -> str:
    """Truncate a value for display."""
    s = str(value)
    return s if len(s) <= max_len else s[:max_len] + "..."


def check_event_schema(
    events_path: Path,
    schema_path: Path,
    max_errors: int = 20,
) -> dict[str, Any]:
    """Validate all events against schema and return structured evidence."""
    events = load_events(events_path)
    schema = load_schema(schema_path)

    if not events:
        return {
            "check": "event_schema_valid",
            "status": "pass",
            "events_file": str(events_path),
            "schema_file": str(schema_path),
            "total_events": 0,
            "valid_events": 0,
            "invalid_events": 0,
            "errors": [],
        }

    all_errors: list[dict[str, Any]] = []
    invalid_count = 0

    for idx, event in enumerate(events):
        event_errors = validate_event(event, schema)
        if event_errors:
            invalid_count += 1
            if len(all_errors) < max_errors:
                all_errors.append({
                    "event_index": idx,
                    "errors": event_errors,
                    "event_preview": {k: _truncate(v) for k, v in list(event.items())[:5]},
                })

    valid_count = len(events) - invalid_count
    status = "pass" if invalid_count == 0 else "fail"

    return {
        "check": "event_schema_valid",
        "status": status,
        "events_file": str(events_path),
        "schema_file": str(schema_path),
        "total_events": len(events),
        "valid_events": valid_count,
        "invalid_events": invalid_count,
        "validity_rate": round(valid_count / len(events), 4) if events else 1.0,
        "errors_reported": len(all_errors),
        "errors_truncated": invalid_count > max_errors,
        "errors": all_errors,
    }


def main() -> int:
    args = parse_args()
    result = check_event_schema(args.events, args.schema, args.max_errors)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
