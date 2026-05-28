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
    "evals",
    "docs/getting-started.md",
    "docs/codex-setup.md",
    "docs/plugin-publishing.md",
    "mcp",
    "agents",
    "benchmarks",
    "schemas",
    "tests",
    "requirements.txt",
    "requirements-proof.txt",
    "scripts/validate_dataset_contract.py",
    "scripts/validate-template-schemas.py",
    "scripts/hook_runner.py",
    "bootstrap.sh",
    "bootstrap.ps1",
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
        help="Tool name, comma-separated tool names, or one of: auto, all",
    )
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--symlink",
        action="store_true",
        help="Create symlinks instead of copying files",
    )
    return parser.parse_args()


def iter_source_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return [candidate for candidate in path.rglob("*") if candidate.is_file()]


def relative_target(source_file: Path, source_root: Path, target_root: Path) -> Path:
    return target_root / source_file.relative_to(source_root)


def copy_path(relative_path: str, target_root: Path, force: bool, symlink: bool) -> None:
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

        if destination.exists():
            destination.unlink()
        if symlink:
            destination.symlink_to(source_file.resolve())
            print(f"Linked: {destination} -> {source_file}")
        else:
            shutil.copy2(source_file, destination)
            print(f"Installed: {destination}")


def detect_tools(target_root: Path) -> list[str]:
    detections = {
        "cursor": (target_root / ".cursor").exists(),
        "claude": (target_root / ".claude").exists()
        or (target_root / "CLAUDE.md").exists(),
        "copilot": (target_root / ".github" / "copilot-instructions.md").exists(),
        "gemini": (target_root / ".gemini").exists() or (target_root / "GEMINI.md").exists(),
        "kiro": (target_root / ".kiro").exists(),
        "windsurf": (target_root / ".windsurfrules").exists()
        or (target_root / ".windsurfrules.example").exists(),
        "opencode": (target_root / ".opencode").exists(),
    }
    detected = [tool for tool, found in detections.items() if found]
    return detected or ["generic"]


def parse_tools_argument(raw: str, target_root: Path) -> list[str]:
    if raw == "auto":
        return detect_tools(target_root)
    if raw == "all":
        return ["all"]

    requested = [part.strip() for part in raw.split(",") if part.strip()]
    unknown = [
        tool
        for tool in requested
        if tool not in TOOL_PATHS and tool not in {"all", "auto"}
    ]
    if unknown:
        raise SystemExit(f"Unsupported tools requested: {', '.join(unknown)}")
    return requested


def main() -> int:
    args = parse_args()
    target_root = args.target.resolve()
    target_root.mkdir(parents=True, exist_ok=True)
    selected_tools = parse_tools_argument(args.tool, target_root)

    paths: list[str] = []
    for selected in selected_tools:
        if selected == "all":
            paths.extend(CORE_PATHS)
            for tool_name, tool_paths in TOOL_PATHS.items():
                if tool_name not in {"codex", "generic"}:
                    paths.extend(tool_paths)
            continue
        paths.extend(TOOL_PATHS[selected])

    seen: set[str] = set()
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        copy_path(path, target_root, args.force, args.symlink)

    print("Toolkit install complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
