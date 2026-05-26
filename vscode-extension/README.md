# Data Engineering Agent Skills for VS Code Family

This extension installs the repository's core data engineering skill pack into the current workspace.

Download paths:

- GitHub Releases `.vsix`: `https://github.com/vaquarkhan/data-engineering-agent-skills/releases/latest`
- publishing workflow and marketplace setup: `docs/plugin-publishing.md`

Compatible editors:

- `VS Code`
- `Cursor`
- `Windsurf`
- `VSCodium`

## Commands

- `Data Engineering Skills: Install Full Toolkit`
- `Data Engineering Skills: Install Core Pack`
- `Data Engineering Skills: Install Agent Adapters`
- `Data Engineering Skills: Install Starter Pack`
- `Data Engineering Skills: Install MCP Templates`
- `Data Engineering Skills: Scaffold Runnable Example`

## What It Installs

Depending on the command, the extension can write:

- `AGENTS.md`
- `CLAUDE.md`
- `skills-index.md`
- `hooks/`
- `.cursor/rules/`
- `.kiro/steering/`
- `.claude/commands/`
- `.gemini/commands/`
- `.opencode/`
- `.windsurfrules`
- `.github/copilot-instructions.md`
- `templates/`
- `starter-packs/`
- `mcp/`
- runnable example folders under `examples/`

## Source Resolution

During local development, the extension loads files from the repository checkout.

For packaged usage, it can fall back to the raw GitHub source using the `dataEngineeringSkills.rawBaseUrl` setting.

## Local Development

1. Open the `vscode-extension/` folder in VS Code.
2. Press `F5` to launch the Extension Development Host.
3. Run the commands from the command palette in a test workspace.

## Related Tutorial

For a longer install-and-usage walkthrough, see:

- `tutorials/installing-vscode-and-jetbrains-plugins.md`
- `docs/plugin-publishing.md`
