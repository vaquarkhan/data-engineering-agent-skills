# Tutorial: Installing The VS Code And JetBrains Plugins

This tutorial explains how to install and use the repository through its native editor/plugin surfaces.

## Goal

By the end of this tutorial, you should be able to:

- install the `VS Code` family extension from the release asset
- use the extension commands to install repo assets into a workspace
- install the `JetBrains` plugin ZIP
- use the plugin actions from the IDE
- decide when the plugin path is better than direct file-based setup

## Part 1: Install The VS Code Family Extension

The extension supports:

- `VS Code`
- `Cursor`
- `Windsurf`
- `VSCodium`

### Step 1: Download The `.vsix`

Go to the latest release page and download the `VS Code` family `.vsix` file.

The release page is linked from:

- `README.md`
- the repository Releases tab

### Step 2: Install The `.vsix`

In a `VS Code` family editor:

1. open the Extensions panel
2. open the Extensions menu
3. choose `Install from VSIX...`
4. select the downloaded `.vsix`

### Step 3: Open A Workspace

Open the project where you want to install the data engineering assets.

The extension installs files into the current workspace, not into every project globally.

### Step 4: Use The Command Palette

Run one of these commands:

- `Data Engineering Skills: Install Full Toolkit`
- `Data Engineering Skills: Install Core Pack`
- `Data Engineering Skills: Install Agent Adapters`
- `Data Engineering Skills: Install Starter Pack`
- `Data Engineering Skills: Install MCP Templates`
- `Data Engineering Skills: Scaffold Runnable Example`

### Step 5: Choose The Smallest Useful Install

Recommended choices:

- new team adoption -> `Install Full Toolkit`
- existing repo with specific editor setup -> `Install Agent Adapters`
- focused use case -> `Install Starter Pack`
- trying one pattern quickly -> `Scaffold Runnable Example`

### What The Extension Can Install

Depending on the command, it can place:

- `AGENTS.md`
- `CLAUDE.md`
- `hooks/`
- `.cursor/rules/`
- `.claude/commands/`
- `.gemini/commands/`
- `.opencode/`
- `.windsurfrules`
- `starter-packs/`
- `templates/`
- `mcp/`
- runnable example files

## Part 2: Install The JetBrains Plugin

The plugin targets IntelliJ-platform IDEs such as:

- `IntelliJ IDEA`
- `PyCharm`
- `WebStorm`
- `DataGrip`
- `GoLand`
- `PhpStorm`

### Step 1: Download The Plugin ZIP

Download the JetBrains plugin ZIP from the latest repository release.

### Step 2: Install From Disk

In a JetBrains IDE:

1. open `Settings` or `Preferences`
2. open `Plugins`
3. click the gear icon
4. choose `Install Plugin from Disk...`
5. select the downloaded plugin ZIP
6. restart the IDE if prompted

### Step 3: Open The Target Project

Open the project where you want the repo assets installed.

### Step 4: Use The Tools Menu

After installation, use the plugin actions from the `Tools` menu:

- `Install Full Toolkit`
- `Install Core Pack`
- `Install Agent Adapters`
- `Install Starter Pack`
- `Install MCP Templates`
- `Scaffold Runnable Example`

### What The Plugin Can Install

It can place the same major repository assets into the current project, including:

- `AGENTS.md`
- `CLAUDE.md`
- `hooks/`
- `.opencode/`
- setup docs such as `docs/getting-started.md`
- starter packs and examples

## Part 3: Which Plugin Path Should You Use?

Use the `VS Code` extension when:

- the team uses `VS Code`, `Cursor`, `Windsurf`, or `VSCodium`
- you want command-palette driven installs
- you want the repo assets pulled into an existing workspace quickly

Use the `JetBrains` plugin when:

- the team is on IntelliJ-platform IDEs
- you want the install flow inside the IDE instead of manual copying
- you want starter packs and examples installed from menu actions

Use direct file-based setup when:

- the team uses a different agent or editor
- you want full control over which files are copied
- you prefer `scripts/install.sh`

## Part 4: Recommended First Use After Install

After installing through either plugin surface:

1. open `skills/using-data-engineering-agent-skills/SKILL.md`
2. pick the relevant preset under `presets/`
3. choose the safest lifecycle step:
   - `/spec`
   - `/plan`
   - `/build`
   - `/validate`
   - `/review`
   - `/backfill`
   - `/ship`
4. use a starter pack or example instead of starting from scratch

## Part 5: Troubleshooting

### Plugin installed but commands do not show up

- verify the IDE/editor was restarted if required
- confirm a workspace or project folder is open
- check that the extension/plugin actually finished installing

### Files already exist

Both installer surfaces may prompt about overwriting existing files.

Use:

- overwrite when you want repo defaults refreshed
- skip existing when the project already has customized local instructions

### You only want one narrow workflow

Do not install the full toolkit if you only need one slice.

Instead use:

- `Install Agent Adapters`
- `Install Starter Pack`
- `Scaffold Runnable Example`

## Related Docs

- `docs/getting-started.md`
- `docs/cursor-setup.md`
- `docs/jetbrains-setup.md`
- `vscode-extension/README.md`
- `jetbrains-plugin/README.md`
