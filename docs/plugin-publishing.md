# Plugin Publishing

This guide covers how to publish the VS Code extension and JetBrains plugin to their respective marketplaces so users can discover, install, and auto-update them like any other plugin.

## What You Get After Publishing

- **VS Code Marketplace**: users search "Data Engineering Agent Skills" in the Extensions panel, install with one click, and receive auto-updates on each release
- **Open VSX**: same experience for VSCodium and other open-source VS Code forks
- **JetBrains Marketplace**: users search in IntelliJ/PyCharm/DataGrip plugin settings, install, and auto-update
- **Download stats**: all marketplaces show install counts, ratings, and trending

## Step-by-Step: Publish to VS Code Marketplace

### 1. Create a Publisher Account

1. Go to [https://marketplace.visualstudio.com/manage](https://marketplace.visualstudio.com/manage)
2. Sign in with your Microsoft or GitHub account
3. Create a publisher with ID `vaquarkhan` (must match `publisher` in `vscode-extension/package.json`)
4. If the ID is taken, update `package.json` to match your chosen publisher ID

### 2. Create a Personal Access Token (PAT)

1. Go to [https://dev.azure.com](https://dev.azure.com) → sign in
2. Click your profile icon → **Personal Access Tokens**
3. Click **New Token**
4. Set:
   - Name: `vsce-publish`
   - Organization: **All accessible organizations**
   - Expiration: 1 year (set a calendar reminder to rotate)
   - Scopes: click **Custom defined** → select **Marketplace > Manage**
5. Click **Create** and copy the token

### 3. Add the Secret to Your Repository

1. Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `VSCE_PAT`
4. Value: paste the PAT from step 2
5. Click **Add secret**

### 4. Publish

Create a new GitHub Release (or push a `v*` tag). The `publish-plugins.yml` workflow will automatically:
- Build the `.vsix`
- Publish to VS Code Marketplace
- The extension appears at: `https://marketplace.visualstudio.com/items?itemName=vaquarkhan.data-engineering-agent-skills`

## Step-by-Step: Publish to Open VSX (VSCodium)

### 1. Create an Account

1. Go to [https://open-vsx.org](https://open-vsx.org)
2. Sign in with GitHub
3. Go to your settings and create a namespace matching your publisher ID

### 2. Create an Access Token

1. In Open VSX settings → **Access Tokens**
2. Create a new token with publish permissions
3. Copy the token

### 3. Add the Secret

1. GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. New secret: `OVSX_PAT` → paste the token

### 4. Publish

Same release flow — the workflow handles Open VSX publishing automatically when the secret exists.

## Step-by-Step: Publish to JetBrains Marketplace

### 1. Create a Vendor Account

1. Go to [https://plugins.jetbrains.com/author/me](https://plugins.jetbrains.com/author/me)
2. Sign in with your JetBrains account (create one if needed)
3. Register as a plugin vendor

### 2. Upload the Plugin Manually (First Time)

For the first ever publish, you must upload the plugin manually:

1. Build the plugin locally: `cd jetbrains-plugin && ./gradlew buildPlugin`
2. Find the `.zip` in `build/distributions/`
3. Go to [https://plugins.jetbrains.com/plugin/add](https://plugins.jetbrains.com/plugin/add)
4. Upload the `.zip`, fill in the plugin details
5. Wait for approval (usually 1-2 business days)

### 3. Generate a Marketplace Token

1. Go to [https://plugins.jetbrains.com/author/me/tokens](https://plugins.jetbrains.com/author/me/tokens)
2. Create a new permanent token
3. Copy the token

### 4. Plugin Signing (Required for Marketplace)

JetBrains requires plugins to be signed. Generate a key pair:

```bash
# Generate a private key
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:4096

# Generate a certificate signing request
openssl req -new -key private.pem -out request.csr

# Self-sign the certificate (or use a CA)
openssl x509 -req -days 3650 -in request.csr -signkey private.pem -out chain.crt
```

### 5. Add All Secrets

Add these secrets in your GitHub repo settings:

| Secret name | Value |
| --- | --- |
| `JETBRAINS_MARKETPLACE_TOKEN` | The marketplace token from step 3 |
| `JETBRAINS_CERTIFICATE_CHAIN` | Contents of `chain.crt` |
| `JETBRAINS_PRIVATE_KEY` | Contents of `private.pem` |
| `JETBRAINS_PRIVATE_KEY_PASSWORD` | Password for the private key (empty string if none) |

### 6. Publish

After secrets are configured, every GitHub Release triggers automatic publish, signing, and upload to JetBrains Marketplace.

## Auto-Update Behavior

Once published to marketplaces:

- **VS Code/Cursor/Windsurf**: updates are delivered automatically when users have auto-update enabled (default). Users see a notification when an update is available.
- **JetBrains IDEs**: updates are checked daily. Users see the update in Settings → Plugins → Updates tab.
- **Version bumps**: change `version` in `vscode-extension/package.json` and `pluginVersion` in `jetbrains-plugin/gradle.properties` before creating a new release tag.

## Release Workflow

```text
1. Update version numbers:
   - vscode-extension/package.json  →  "version": "2.1.0"
   - jetbrains-plugin/gradle.properties  →  pluginVersion = 2.1.0

2. Commit version bump:
   git add -A && git commit -m "Bump version to 2.1.0"

3. Tag and push:
   git tag -a v2.1.0 -m "Release v2.1.0"
   git push origin main --tags

4. Create GitHub Release (automatic via release-artifacts.yml on tag push)

5. Marketplace publish triggers automatically via publish-plugins.yml
```

## Download Stats and Badges

Once published, add badges to your README:

```markdown
[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/vaquarkhan.data-engineering-agent-skills)](https://marketplace.visualstudio.com/items?itemName=vaquarkhan.data-engineering-agent-skills)
[![VS Code Downloads](https://img.shields.io/visual-studio-marketplace/d/vaquarkhan.data-engineering-agent-skills)](https://marketplace.visualstudio.com/items?itemName=vaquarkhan.data-engineering-agent-skills)
[![JetBrains Plugin](https://img.shields.io/jetbrains/plugin/v/PLUGIN_ID)](https://plugins.jetbrains.com/plugin/PLUGIN_ID)
[![JetBrains Downloads](https://img.shields.io/jetbrains/plugin/d/PLUGIN_ID)](https://plugins.jetbrains.com/plugin/PLUGIN_ID)
```

Replace `PLUGIN_ID` with the numeric ID assigned after your first JetBrains upload.

## Troubleshooting

| Problem | Solution |
| --- | --- |
| `VSCE_PAT` expired | Regenerate in Azure DevOps, update the GitHub secret |
| Publisher ID mismatch | Ensure `publisher` in package.json matches your Marketplace publisher exactly |
| JetBrains signing fails | Verify certificate chain is complete and key password matches |
| First JetBrains publish rejected | Check plugin.xml compatibility range and required description fields |
| Workflow skips publish step | Secrets are empty or not configured — check secret names match exactly |

## Workflows Involved

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `release-artifacts.yml` | `v*` tag push | Builds `.vsix` + `.zip`, runs smoke tests, creates GitHub Release |
| `publish-plugins.yml` | Release published | Publishes to VS Code Marketplace, Open VSX, and JetBrains Marketplace |
| `test-plugin-installation.yml` | Push / PR | Validates plugin artifacts are buildable and installable |

## Checklist Before First Publish

- [ ] VS Code Marketplace publisher account created with matching ID
- [ ] `VSCE_PAT` secret added to GitHub repo
- [ ] (Optional) Open VSX namespace created and `OVSX_PAT` secret added
- [ ] JetBrains vendor account created
- [ ] First JetBrains plugin uploaded manually and approved
- [ ] JetBrains signing keys generated
- [ ] All four JetBrains secrets added to GitHub repo
- [ ] Version numbers in `package.json` and `gradle.properties` match the release tag
- [ ] Test by creating a release — verify plugins appear in marketplaces within minutes
