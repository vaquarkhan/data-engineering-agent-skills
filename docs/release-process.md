# Release Process

Use this process to publish repository updates in a way that is reviewable and adoption-friendly.

## Release Surfaces

- skills
- presets
- references
- templates
- examples
- agent packaging files
- IDE plugins
- scripts
- MCP templates

## Suggested Steps

1. Group changes into one coherent release theme.
2. Update `CHANGELOG.md`.
3. Update `skills-index.md` and `README.md` if discovery changes.
4. Verify new examples, templates, and plugin installers are internally consistent.
5. Run the workflow surfaces that matter for the release, especially `Validate and Package`, `Test Plugin Installation`, and `Markdown Lint`.
6. Tag the release with a version and short release notes.
7. Use `Publish Plugins` when marketplace publishing is configured.

## Release Themes

- new skill wave
- new platform or preset pack
- adoption tooling and install improvements
- examples and starter packs
- operational safety and governance improvements

## Evidence To Capture

- what changed
- who should care
- how to install or adopt it
- what examples or starter packs demonstrate the new capability
- what plugin download or marketplace surfaces were updated
