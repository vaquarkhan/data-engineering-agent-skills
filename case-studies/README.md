# Data Engineering Case Studies

This folder contains practical, scenario-driven case studies that show how to apply the repository skills, presets, templates, and examples to real delivery situations.

Use case studies when you need:

- a realistic end-to-end walkthrough instead of isolated commands
- release-safe patterns for incidents, replays, and regulated data workflows
- evidence-oriented execution with explicit rollback paths

## Included Case Studies

| Case study | Best when | Stack anchor | Typical run time |
| --- | --- | --- | --- |
| `incident-bad-publish-recovery.md` | bad numbers reached publish outputs and downstream dashboards | `examples/dbt-warehouse-marts` | 30-90 minutes |
| `replay-safe-backfill-after-corruption.md` | historical window is corrupted and requires bounded replay | `examples/kafka-flink-streaming` | 1-3 hours |
| `regulated-data-release-gate.md` | sensitive dataset must pass compliance controls before broad access | `templates/data-compliance-controls.yaml` | 2-6 hours |

## How To Read A Case Study

1. Start with scenario and failure mode.
2. Follow the architecture and control boundaries.
3. Execute steps in order and collect evidence artifacts.
4. Use rollback criteria exactly as written before broad publish.
5. Adapt owners, SLAs, and platform details to your environment.

## Template

Use `template-case-study.md` when creating new case studies in this folder.
