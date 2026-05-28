#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$PWD}"
TOOL_MODE="${2:-auto}"

echo "Bootstrapping Data Engineering Agent Skills"
echo "Target: $TARGET_DIR"
echo "Tool mode: $TOOL_MODE"

python "$REPO_ROOT/scripts/install_toolkit.py" --tool "$TOOL_MODE" --target "$TARGET_DIR"
echo "Bootstrap complete."
