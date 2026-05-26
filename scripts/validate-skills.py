#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

REQUIRED_SKILL_SECTIONS = [
    "## Overview",
    "## When to Use",
    "## Workflow",
    "## Common Rationalizations",
    "## Red Flags",
    "## Verification",
]

REQUIRED_PRESET_SECTIONS = [
    "## Overview",
    "## Use When",
    "## Preferred Platform Services",
    "## Design Rules",
    "## Verification",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening YAML frontmatter delimiter"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, ["missing closing YAML frontmatter delimiter"]

    body = parts[1].strip()
    metadata: dict[str, str] = {}
    for line in body.splitlines():
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, errors


def validate_markdown_file(path: Path, expected_name: str, required_sections: list[str]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    metadata, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    if metadata.get("name") != expected_name:
        errors.append(f"name frontmatter must match directory name '{expected_name}'")
    elif not SKILL_NAME_PATTERN.fullmatch(expected_name):
        errors.append("name must be lowercase and hyphen-separated")

    description = metadata.get("description", "")
    if not description:
        errors.append("missing description frontmatter")
    elif "use when" not in description.lower():
        errors.append("description should explain when to use the file")
    elif len(description.split()) < 8:
        errors.append("description should be descriptive enough for progressive disclosure")

    for section in required_sections:
        if section not in text:
            errors.append(f"missing section '{section}'")

    return errors


def validate_command_surfaces() -> list[str]:
    errors: list[str] = []
    expected_commands = ["spec", "plan", "build", "validate", "review", "backfill", "ship"]
    for command_dir in [ROOT / ".claude" / "commands", ROOT / ".gemini" / "commands"]:
        for name in expected_commands:
            if not (command_dir / f"{name}.md").exists():
                errors.append(f"missing command file: {command_dir / f'{name}.md'}")
    return errors


def main() -> int:
    all_errors: list[str] = []

    for skill_file in sorted(ROOT.glob("skills/*/SKILL.md")):
        expected_name = skill_file.parent.name
        errors = validate_markdown_file(skill_file, expected_name, REQUIRED_SKILL_SECTIONS)
        all_errors.extend(f"{skill_file}: {error}" for error in errors)

    for preset_file in sorted(ROOT.glob("presets/*/PRESET.md")):
        expected_name = preset_file.parent.name
        errors = validate_markdown_file(preset_file, expected_name, REQUIRED_PRESET_SECTIONS)
        all_errors.extend(f"{preset_file}: {error}" for error in errors)

    all_errors.extend(validate_command_surfaces())

    if all_errors:
        print("Validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    skill_count = len(list(ROOT.glob("skills/*/SKILL.md")))
    preset_count = len(list(ROOT.glob("presets/*/PRESET.md")))
    print(f"Validated {skill_count} skills and {preset_count} presets.")
    print("Lifecycle command surfaces are present for Claude and Gemini.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
