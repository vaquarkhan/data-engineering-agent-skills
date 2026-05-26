#!/usr/bin/env python3
"""Smoke-test packaged plugin artifacts."""

from __future__ import annotations

import argparse
import io
import json
import zipfile
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_zip_entries(zip_path: Path, required_entries: list[str]) -> zipfile.ZipFile:
    archive = zipfile.ZipFile(zip_path)
    names = {name.lower() for name in archive.namelist()}
    missing = [entry for entry in required_entries if entry.lower() not in names]
    if missing:
        archive.close()
        fail(f"{zip_path} is missing required entries: {', '.join(missing)}")
    return archive


def test_vsix(vsix_path: Path) -> None:
    with assert_zip_entries(
        vsix_path,
        [
            "extension/package.json",
            "extension/extension.js",
            "extension/README.md",
        ],
    ) as archive:
        package_json = json.loads(archive.read("extension/package.json").decode("utf-8"))
        commands = package_json.get("contributes", {}).get("commands", [])
        if len(commands) < 6:
            fail(f"{vsix_path} packaged only {len(commands)} commands; expected at least 6")


def test_jetbrains_zip(plugin_zip_path: Path) -> None:
    with zipfile.ZipFile(plugin_zip_path) as archive:
        jar_entries = [
            name
            for name in archive.namelist()
            if name.endswith(".jar") and "/lib/" in name
        ]
        if not jar_entries:
            fail(f"{plugin_zip_path} does not contain a plugin JAR under lib/")

        plugin_jar = jar_entries[0]
        with zipfile.ZipFile(io.BytesIO(archive.read(plugin_jar))) as plugin_archive:
            if "META-INF/plugin.xml" not in set(plugin_archive.namelist()):
                fail(
                    f"{plugin_zip_path} plugin JAR {plugin_jar} is missing META-INF/plugin.xml"
                )


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke-test packaged IDE plugin artifacts.")
    parser.add_argument("--vsix", required=True, type=Path, help="Path to the packaged VSIX")
    parser.add_argument(
        "--jetbrains-zip",
        required=True,
        type=Path,
        help="Path to the packaged JetBrains plugin ZIP",
    )
    args = parser.parse_args()

    if not args.vsix.exists():
        fail(f"VSIX not found: {args.vsix}")
    if not args.jetbrains_zip.exists():
        fail(f"JetBrains ZIP not found: {args.jetbrains_zip}")

    test_vsix(args.vsix)
    test_jetbrains_zip(args.jetbrains_zip)
    print("Plugin installation artifacts look structurally valid.")


if __name__ == "__main__":
    main()
