# Plugin Publishing

Use this guide when you want the `VS Code` extension and `JetBrains` plugin to be easy to discover and download beyond raw build artifacts.

## Discovery And Download Surfaces

This repository supports three plugin delivery surfaces:

- GitHub Releases for direct `.vsix` and `.zip` downloads
- `VS Code Marketplace` and `Open VSX` for the `VS Code` family extension
- `JetBrains Marketplace` for the IntelliJ-platform plugin

GitHub Releases remain the universal fallback download surface even when marketplace publishing is not configured yet.

## Workflows

- `.github/workflows/validate-and-package.yml`  
  Validates repo structure and builds release-ready plugin artifacts on `push`, `pull_request`, and manual runs.

- `.github/workflows/test-plugin-installation.yml`  
  Packages both plugins and smoke-tests the built `.vsix` and `.zip` contents so broken installer artifacts are caught early.

- `.github/workflows/release-artifacts.yml`  
  Publishes GitHub release assets when a `v*` tag is pushed.

- `.github/workflows/publish-plugins.yml`  
  Publishes the `VS Code` extension and `JetBrains` plugin to their marketplaces when the required secrets are configured.

- `.github/workflows/markdown-lint.yml`  
  Keeps docs and setup guides clean so discovery surfaces do not drift.

## Secrets Required For Marketplace Publish

### VS Code Marketplace

- `VSCE_PAT`

### Open VSX

- `OVSX_PAT`

### JetBrains Marketplace

- `JETBRAINS_MARKETPLACE_TOKEN`
- `JETBRAINS_CERTIFICATE_CHAIN`
- `JETBRAINS_PRIVATE_KEY`
- `JETBRAINS_PRIVATE_KEY_PASSWORD`

## Recommended Release Flow

1. Run the validation and packaging workflows on the branch or pull request.
2. Confirm `Test Plugin Installation` passes.
3. Tag the release so `Release Artifacts` uploads GitHub-downloadable `.vsix` and `.zip` files.
4. Publish to marketplaces through `Publish Plugins` once secrets are configured.

## Good Outcome

The plugins should be discoverable from repo docs, downloadable from GitHub Releases, and publishable to editor marketplaces without changing the build by hand.
