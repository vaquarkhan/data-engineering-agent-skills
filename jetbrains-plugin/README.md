# JetBrains Plugin

This plugin installs the data engineering skill pack into the current project for IntelliJ-based IDEs such as:

- IntelliJ IDEA
- PyCharm
- WebStorm
- DataGrip
- GoLand
- PhpStorm

## Commands

- Install Full Toolkit
- Install Core Pack
- Install Agent Adapters
- Install Starter Pack
- Install MCP Templates
- Scaffold Runnable Example

The plugin installer can also place supporting assets such as:

- `CLAUDE.md`
- `hooks/`
- `.kiro/steering/`
- `.opencode/`
- `docs/getting-started.md`
- `docs/kiro-setup.md`
- `docs/windsurf-setup.md`
- `docs/opencode-setup.md`

## Build

```bash
./gradlew buildPlugin
```

## Local Run

```bash
./gradlew runIde
```

## Related Tutorial

For a longer install-and-usage walkthrough, see:

- `tutorials/installing-vscode-and-jetbrains-plugins.md`
