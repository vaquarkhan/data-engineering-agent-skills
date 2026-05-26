#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_ignored(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def check_markdown_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    for match in MD_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if is_ignored(target):
            continue

        target_path = target.split("#", 1)[0]
        if not target_path:
            continue

        resolved = (path.parent / target_path).resolve()
        if not resolved.exists():
            try:
                relative = resolved.relative_to(ROOT)
            except ValueError:
                relative = resolved
            errors.append(f"{path}: broken local link -> {target} ({relative})")

    return errors


def main() -> int:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        errors.extend(check_markdown_file(path))

    if errors:
        print("Local markdown link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Local markdown links look valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
