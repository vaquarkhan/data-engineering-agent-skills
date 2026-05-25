# IDE Support Matrix

This repository supports major IDE families through native adapters or extension scaffolds.

## VS Code Family

Supported with the same extension scaffold in `vscode-extension/`:

- `VS Code`
- `Cursor`
- `Windsurf`
- `VSCodium`

Use cases:

- install the full toolkit into a workspace
- install agent adapters
- install starter packs
- install MCP templates
- scaffold runnable examples

## JetBrains Family

Supported with the plugin scaffold in `jetbrains-plugin/`:

- `IntelliJ IDEA`
- `PyCharm`
- `WebStorm`
- `DataGrip`
- `GoLand`
- `PhpStorm`

Use cases:

- install the same toolkit assets into the current project
- choose starter packs and runnable examples
- install agent adapter files for other tools used alongside JetBrains IDEs

## Agent Surfaces Covered

These IDE integrations install files for:

- `Cursor`
- `Claude`
- `Copilot`
- `Gemini`
- `Codex`
- generic `AGENTS.md` consumers

## Practical Recommendation

- use the `vscode-extension/` package for VS Code-compatible editors
- use the `jetbrains-plugin/` package for IntelliJ-platform IDEs
- use `scripts/install.sh` or starter packs when an extension is not available yet
