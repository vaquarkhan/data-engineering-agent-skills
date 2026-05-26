#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/install.sh --tool <cursor|claude|copilot|gemini|codex|generic|kiro|windsurf|opencode|all> --target <path> [--force]

Examples:
  scripts/install.sh --tool cursor --target /path/to/project
  scripts/install.sh --tool kiro --target /path/to/project
  scripts/install.sh --tool windsurf --target /path/to/project
  scripts/install.sh --tool all --target /path/to/project --force
EOF
}

TOOL=""
TARGET=""
FORCE="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)
      TOOL="${2:-}"
      shift 2
      ;;
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --force)
      FORCE="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$TOOL" || -z "$TARGET" ]]; then
  usage
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

copy_file() {
  local src="$1"
  local dst="$2"
  mkdir -p "$(dirname "$dst")"
  if [[ -f "$dst" && "$FORCE" != "true" ]]; then
    echo "Skipping existing file: $dst"
    return 0
  fi
  cp "$src" "$dst"
  echo "Installed: $dst"
}

copy_dir_contents() {
  local src_dir="$1"
  local dst_dir="$2"
  mkdir -p "$dst_dir"
  shopt -s nullglob
  local files=("$src_dir"/*)
  for file in "${files[@]}"; do
    if [[ -f "$file" ]]; then
      copy_file "$file" "$dst_dir/$(basename "$file")"
    fi
  done
  shopt -u nullglob
}

install_cursor() {
  copy_dir_contents "$REPO_ROOT/.cursor/rules" "$TARGET/.cursor/rules"
}

install_claude() {
  copy_dir_contents "$REPO_ROOT/.claude/commands" "$TARGET/.claude/commands"
  copy_file "$REPO_ROOT/AGENTS.md" "$TARGET/AGENTS.md"
  copy_file "$REPO_ROOT/CLAUDE.md" "$TARGET/CLAUDE.md"
}

install_copilot() {
  copy_file "$REPO_ROOT/.github/copilot-instructions.md" "$TARGET/.github/copilot-instructions.md"
  copy_file "$REPO_ROOT/AGENTS.md" "$TARGET/AGENTS.md"
}

install_gemini() {
  copy_dir_contents "$REPO_ROOT/.gemini/commands" "$TARGET/.gemini/commands"
}

install_kiro() {
  copy_dir_contents "$REPO_ROOT/.kiro/steering" "$TARGET/.kiro/steering"
  copy_file "$REPO_ROOT/docs/kiro-setup.md" "$TARGET/docs/kiro-setup.md"
  copy_file "$REPO_ROOT/AGENTS.md" "$TARGET/AGENTS.md"
  copy_file "$REPO_ROOT/CLAUDE.md" "$TARGET/CLAUDE.md"
}

install_windsurf() {
  copy_file "$REPO_ROOT/.windsurfrules.example" "$TARGET/.windsurfrules"
  copy_file "$REPO_ROOT/docs/windsurf-setup.md" "$TARGET/docs/windsurf-setup.md"
}

install_opencode() {
  copy_file "$REPO_ROOT/AGENTS.md" "$TARGET/AGENTS.md"
  copy_file "$REPO_ROOT/CLAUDE.md" "$TARGET/CLAUDE.md"
  copy_file "$REPO_ROOT/.opencode/README.md" "$TARGET/.opencode/README.md"
  copy_file "$REPO_ROOT/.opencode/skills" "$TARGET/.opencode/skills"
  copy_file "$REPO_ROOT/docs/opencode-setup.md" "$TARGET/docs/opencode-setup.md"
}

install_generic() {
  copy_file "$REPO_ROOT/AGENTS.md" "$TARGET/AGENTS.md"
  copy_file "$REPO_ROOT/CLAUDE.md" "$TARGET/CLAUDE.md"
  copy_file "$REPO_ROOT/skills-index.md" "$TARGET/skills-index.md"
  copy_file "$REPO_ROOT/docs/getting-started.md" "$TARGET/docs/getting-started.md"
  copy_file "$REPO_ROOT/registry/assets.json" "$TARGET/registry/assets.json"
  copy_dir_contents "$REPO_ROOT/templates" "$TARGET/templates"
  copy_dir_contents "$REPO_ROOT/hooks" "$TARGET/hooks"
}

case "$TOOL" in
  cursor) install_cursor ;;
  claude) install_claude ;;
  copilot) install_copilot ;;
  gemini) install_gemini ;;
  codex) install_generic ;;
  generic) install_generic ;;
  kiro) install_kiro ;;
  windsurf) install_windsurf ;;
  opencode) install_opencode ;;
  all)
    install_cursor
    install_claude
    install_copilot
    install_gemini
    install_kiro
    install_windsurf
    install_opencode
    install_generic
    ;;
  *)
    echo "Unsupported tool: $TOOL" >&2
    exit 1
    ;;
esac
