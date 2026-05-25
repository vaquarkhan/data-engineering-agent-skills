# JetBrains Setup

Use the plugin scaffold in `jetbrains-plugin/` to install the data engineering skill pack into IntelliJ-platform IDEs.

Supported IDE families include:

- `IntelliJ IDEA`
- `PyCharm`
- `WebStorm`
- `DataGrip`
- `GoLand`
- `PhpStorm`

## Recommended Flow

1. Build or run the plugin from `jetbrains-plugin/`
2. Open the target project in a JetBrains IDE
3. Use the `Tools` menu:
   - Install Full Toolkit
   - Install Core Pack
   - Install Agent Adapters
   - Install Starter Pack
   - Install MCP Templates
   - Scaffold Runnable Example

## What Gets Installed

- `AGENTS.md`
- `skills-index.md`
- agent adapter files for supported tools
- starter packs
- MCP templates
- runnable example packs

## Notes

- The plugin installs repository assets into the current project, not the IDE globally
- It complements other tools in the repo such as the `VS Code` family extension and `scripts/install.sh`
