#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

CORE_PATHS = [
    "AGENTS.md",
    "CLAUDE.md",
    "skills-index.md",
    "registry/assets.json",
    "templates",
    "hooks",
    "skills",
    "presets",
    "starter-packs",
    "references",
    "examples",
    "tutorials",
    "docs/getting-started.md",
    "docs/codex-setup.md",
    "docs/plugin-publishing.md",
    "mcp",
    "agents",
    "benchmarks",
    "tests",
    "requirements.txt",
    "requirements-proof.txt",
    "scripts/validate_dataset_contract.py",
    "scripts/hook_runner.py",
]

TOOL_PATHS = {
    "cursor": [".cursor/rules"],
    "claude": [".claude/commands", "AGENTS.md", "CLAUDE.md"],
    "copilot": [".github/copilot-instructions.md", "AGENTS.md"],
    "gemini": [".gemini/commands"],
    "codex": CORE_PATHS,
    "generic": CORE_PATHS,
    "kiro": [".kiro/steering", "docs/kiro-setup.md", "AGENTS.md", "CLAUDE.md"],
    "windsurf": [".windsurfrules.example", "docs/windsurf-setup.md"],
    "opencode": [".opencode/README.md", ".opencode/skills", "docs/opencode-setup.md", "AGENTS.md", "CLAUDE.md"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install data engineering agent toolkit files into another project."
    )
    parser.add_argument(
        "--tool",
        required=True,
        choices=[
            "cursor",
            "claude",
            "copilot",
            "gemini",
            "codex",
            "generic",
            "kiro",
            "windsurf",
            "opencode",
            "all",
        ],
    )
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def iter_source_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return [candidate for candidate in path.rglob("*") if candidate.is_file()]


def relative_target(source_file: Path, source_root: Path, target_root: Path) -> Path:
    return target_root / source_file.relative_to(source_root)


def copy_path(relative_path: str, target_root: Path, force: bool) -> None:
    source = REPO_ROOT / relative_path
    if not source.exists():
        raise SystemExit(f"Source path does not exist: {source}")

    source_root = source.parent if source.is_file() else source
    for source_file in iter_source_files(source):
        destination = (
            target_root / relative_path
            if source.is_file()
            else relative_target(source_file, source_root, target_root / relative_path)
        )
        destination.parent.mkdir(parents=True, exist_ok=True)

        if destination.exists() and not force:
            print(f"Skipping existing file: {destination}")
            continue

        shutil.copy2(source_file, destination)
        print(f"Installed: {destination}")


def main() -> int:
    args = parse_args()
    target_root = args.target.resolve()
    target_root.mkdir(parents=True, exist_ok=True)

    paths: list[str] = []
    if args.tool == "all":
        paths.extend(CORE_PATHS)
        for tool_name, tool_paths in TOOL_PATHS.items():
            if tool_name not in {"codex", "generic"}:
                paths.extend(tool_paths)
    else:
        paths.extend(TOOL_PATHS[args.tool])

    seen: set[str] = set()
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        copy_path(path, target_root, args.force)

    print("Toolkit install complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
