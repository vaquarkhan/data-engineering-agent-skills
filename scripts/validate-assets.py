#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "registry" / "assets.json"
JS_INSTALLER = ROOT / "vscode-extension" / "extension.js"
KOTLIN_INSTALLER = ROOT / "jetbrains-plugin" / "src" / "main" / "kotlin" / "com" / "vaquarkhan" / "dataengineeringskills" / "InstallerData.kt"
INSTALL_SCRIPT = ROOT / "scripts" / "install.sh"
INSTALL_TOOLKIT = ROOT / "scripts" / "install_toolkit.py"


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def path_exists(relative_path: str) -> bool:
    return (ROOT / relative_path).exists()


def extract_enclosed(text: str, start_idx: int, opener: str) -> tuple[str, int]:
    closer = {"{": "}", "[": "]", "(": ")"}[opener]
    if text[start_idx] != opener:
        raise ValueError(f"expected {opener!r} at index {start_idx}")

    depth = 0
    in_string: str | None = None
    escaped = False

    for idx in range(start_idx, len(text)):
        ch = text[idx]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == in_string:
                in_string = None
            continue

        if ch in ('"', "'"):
            in_string = ch
            continue
        if ch == opener:
            depth += 1
            continue
        if ch == closer:
            depth -= 1
            if depth == 0:
                return text[start_idx + 1 : idx], idx

    raise ValueError(f"unterminated block starting with {opener!r}")


def extract_after_marker(text: str, marker: str, opener: str) -> str:
    marker_idx = text.index(marker)
    start_idx = text.index(opener, marker_idx)
    block, _ = extract_enclosed(text, start_idx, opener)
    return block


def extract_strings(block: str) -> list[str]:
    values: list[str] = []
    current = []
    in_string = False
    escaped = False

    for ch in block:
        if not in_string:
            if ch == '"':
                in_string = True
                current = []
            continue

        if escaped:
            current.append(ch)
            escaped = False
            continue

        if ch == "\\":
            escaped = True
            continue

        if ch == '"':
            values.append("".join(current))
            in_string = False
            continue

        current.append(ch)

    return values


def parse_js_array(text: str, const_name: str) -> list[str]:
    return extract_strings(extract_after_marker(text, f"const {const_name}", "["))


def parse_js_direct_array_map(text: str, const_name: str) -> dict[str, list[str]]:
    block = extract_after_marker(text, f"const {const_name}", "{")
    result: dict[str, list[str]] = {}
    idx = 0
    while idx < len(block):
        if block[idx].isspace() or block[idx] == ",":
            idx += 1
            continue
        if block[idx] == '"':
            end = block.index('"', idx + 1)
            label = block[idx + 1 : end]
            idx = end + 1
        elif block[idx].isalpha():
            end = idx
            while end < len(block) and (block[end].isalnum() or block[end] in {"_", " "}):
                end += 1
            label = block[idx:end].strip()
            idx = end
        else:
            idx += 1
            continue

        colon = block.index(":", idx)
        array_start = block.index("[", colon)
        array_block, array_end = extract_enclosed(block, array_start, "[")
        result[label] = extract_strings(array_block)
        idx = array_end + 1
    return result


def parse_js_files_object_map(text: str, const_name: str) -> dict[str, list[str]]:
    block = extract_after_marker(text, f"const {const_name}", "{")
    result: dict[str, list[str]] = {}
    idx = 0
    while idx < len(block):
        if block[idx].isspace() or block[idx] == ",":
            idx += 1
            continue
        if block[idx] != '"':
            idx += 1
            continue

        end = block.index('"', idx + 1)
        label = block[idx + 1 : end]
        obj_start = block.index("{", end)
        obj_block, obj_end = extract_enclosed(block, obj_start, "{")
        files_marker = obj_block.index("files")
        array_start = obj_block.index("[", files_marker)
        array_block, _ = extract_enclosed(obj_block, array_start, "[")
        result[label] = extract_strings(array_block)
        idx = obj_end + 1
    return result


def parse_kotlin_list(text: str, var_name: str) -> list[str]:
    return extract_strings(extract_after_marker(text, f"val {var_name} = listOf", "("))


def parse_kotlin_linked_map(text: str, var_name: str) -> dict[str, list[str]]:
    block = extract_after_marker(text, f"val {var_name} = linkedMapOf", "(")
    result: dict[str, list[str]] = {}
    idx = 0
    while idx < len(block):
        if block[idx].isspace() or block[idx] == ",":
            idx += 1
            continue
        if block[idx] != '"':
            idx += 1
            continue

        end = block.index('"', idx + 1)
        label = block[idx + 1 : end]
        list_start = block.index("listOf(", end)
        array_start = block.index("(", list_start)
        array_block, array_end = extract_enclosed(block, array_start, "(")
        result[label] = extract_strings(array_block)
        idx = array_end + 1
    return result


def registry_map(items: list[dict], key_field: str, value_field: str) -> dict[str, list[str]]:
    return {item[key_field]: item[value_field] for item in items}


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []

    for template in data["templates"]:
        if not path_exists(template["path"]):
            errors.append(f"missing template path: {template['path']}")

    seen_ids: set[str] = set()
    seen_labels: set[str] = set()
    for starter in data["starter_packs"]:
        if starter["id"] in seen_ids:
            errors.append(f"duplicate starter pack id: {starter['id']}")
        seen_ids.add(starter["id"])
        if starter["label"] in seen_labels:
            errors.append(f"duplicate starter pack label: {starter['label']}")
        seen_labels.add(starter["label"])
        if not path_exists(starter["path"]):
            errors.append(f"missing starter pack path: {starter['path']}")
        for file_path in starter["install_files"]:
            if not path_exists(file_path):
                errors.append(f"missing starter pack install file: {file_path}")

    example_ids: set[str] = set()
    for example in data["examples"]:
        if example["id"] in example_ids:
            errors.append(f"duplicate example id: {example['id']}")
        example_ids.add(example["id"])
        if not path_exists(example["readme"]):
            errors.append(f"missing example readme: {example['readme']}")

    mcp_labels: set[str] = set()
    for mcp in data["mcp_templates"]:
        if mcp["label"] in mcp_labels:
            errors.append(f"duplicate MCP label: {mcp['label']}")
        mcp_labels.add(mcp["label"])
        if not path_exists(mcp["path"]):
            errors.append(f"missing MCP template: {mcp['path']}")

    for file_path in data["install_surfaces"]["core_files"]:
        if not path_exists(file_path):
            errors.append(f"missing core install file: {file_path}")

    for file_path in data["install_surfaces"]["generic_install_files"]:
        if not path_exists(file_path):
            errors.append(f"missing generic install file: {file_path}")

    for adapter in data["install_surfaces"]["agent_adapters"]:
        for file_path in adapter["files"]:
            if not path_exists(file_path):
                errors.append(f"missing agent adapter file: {file_path}")

    for example in data["install_surfaces"]["runnable_examples"]:
        for file_path in example["files"]:
            if not path_exists(file_path):
                errors.append(f"missing runnable example file: {file_path}")

    for manifest_path in data["packaging_manifests"]:
        if not path_exists(manifest_path):
            errors.append(f"missing packaging manifest: {manifest_path}")

    return errors


def validate_installer_parity(data: dict) -> list[str]:
    errors: list[str] = []
    js_text = JS_INSTALLER.read_text(encoding="utf-8")
    kt_text = KOTLIN_INSTALLER.read_text(encoding="utf-8")

    registry_core = data["install_surfaces"]["core_files"]
    if registry_core != parse_js_array(js_text, "CORE_FILES"):
        errors.append("registry core_files do not match vscode-extension/extension.js CORE_FILES")
    if registry_core != parse_kotlin_list(kt_text, "coreFiles"):
        errors.append("registry core_files do not match jetbrains-plugin InstallerData.coreFiles")

    registry_agent = registry_map(data["install_surfaces"]["agent_adapters"], "label", "files")
    if registry_agent != parse_js_direct_array_map(js_text, "AGENT_ADAPTERS"):
        errors.append("registry agent adapters do not match vscode-extension/extension.js AGENT_ADAPTERS")
    if registry_agent != parse_kotlin_linked_map(kt_text, "agentAdapters"):
        errors.append("registry agent adapters do not match jetbrains-plugin InstallerData.agentAdapters")

    registry_starter = registry_map(data["starter_packs"], "label", "install_files")
    if registry_starter != parse_js_files_object_map(js_text, "STARTER_PACKS"):
        errors.append("registry starter packs do not match vscode-extension/extension.js STARTER_PACKS")
    if registry_starter != parse_kotlin_linked_map(kt_text, "starterPacks"):
        errors.append("registry starter packs do not match jetbrains-plugin InstallerData.starterPacks")

    registry_mcp = {item["label"]: [item["path"]] for item in data["mcp_templates"]}
    if registry_mcp != parse_js_direct_array_map(js_text, "MCP_TEMPLATES"):
        errors.append("registry MCP templates do not match vscode-extension/extension.js MCP_TEMPLATES")
    if registry_mcp != parse_kotlin_linked_map(kt_text, "mcpTemplates"):
        errors.append("registry MCP templates do not match jetbrains-plugin InstallerData.mcpTemplates")

    registry_examples = registry_map(data["install_surfaces"]["runnable_examples"], "label", "files")
    if registry_examples != parse_js_direct_array_map(js_text, "RUNNABLE_EXAMPLES"):
        errors.append("registry runnable examples do not match vscode-extension/extension.js RUNNABLE_EXAMPLES")
    if registry_examples != parse_kotlin_linked_map(kt_text, "runnableExamples"):
        errors.append("registry runnable examples do not match jetbrains-plugin InstallerData.runnableExamples")

    install_text = INSTALL_SCRIPT.read_text(encoding="utf-8")
    install_toolkit_text = INSTALL_TOOLKIT.read_text(encoding="utf-8")
    expected_install_snippets = [
        'python "$SCRIPT_DIR/install_toolkit.py" "$@"',
        '"registry/assets.json"',
        '"templates"',
        '"hooks"',
        '".kiro/steering"',
        '"docs/kiro-setup.md"',
    ]
    if expected_install_snippets[0] not in install_text:
        errors.append(
            f"scripts/install.sh missing expected install behavior: {expected_install_snippets[0]}"
        )
    for snippet in expected_install_snippets[1:]:
        if snippet not in install_toolkit_text:
            errors.append(f"scripts/install_toolkit.py missing expected install behavior: {snippet}")

    return errors


def main() -> int:
    errors: list[str] = []
    if not REGISTRY_PATH.exists():
        print(f"Missing asset registry: {REGISTRY_PATH}")
        return 1

    data = load_registry()
    errors.extend(validate_registry(data))
    errors.extend(validate_installer_parity(data))

    if errors:
        print("Asset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validated "
        f"{len(data['templates'])} templates, "
        f"{len(data['starter_packs'])} starter packs, "
        f"{len(data['examples'])} examples, and "
        f"{len(data['mcp_templates'])} MCP templates."
    )
    print("Registry and installer parity look healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
