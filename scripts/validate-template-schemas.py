#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
MCP_SCHEMA_PATH = ROOT / "schemas" / "mcp-template.schema.json"
STARTER_SCHEMA_PATH = ROOT / "schemas" / "starter-pack.schema.json"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_dir(
    target_dir: Path,
    suffix: str,
    validator: Draft202012Validator,
) -> list[str]:
    errors: list[str] = []
    for file_path in sorted(target_dir.glob(f"*{suffix}")):
        payload = (
            load_json(file_path)
            if suffix == ".json"
            else load_yaml(file_path)
        )
        violations = sorted(validator.iter_errors(payload), key=lambda item: item.path)
        for violation in violations:
            path = ".".join(str(part) for part in violation.path) or "<root>"
            errors.append(f"{file_path}: {path}: {violation.message}")
    return errors


def main() -> int:
    mcp_validator = Draft202012Validator(load_json(MCP_SCHEMA_PATH))
    starter_validator = Draft202012Validator(load_json(STARTER_SCHEMA_PATH))

    errors: list[str] = []
    errors.extend(validate_dir(ROOT / "mcp", ".json", mcp_validator))
    errors.extend(validate_dir(ROOT / "starter-packs", ".yaml", starter_validator))

    if errors:
        print("Template schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("MCP and starter-pack schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
