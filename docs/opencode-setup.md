# OpenCode Setup

This guide explains how to use the repository with `OpenCode` in an agent-driven way.

## Overview

`OpenCode` does not need a separate plugin to use this repository well. The main pattern is:

- strong root instructions
- discoverable `skills/`
- a clear start-here entry file

## Installation

1. Clone the repository.
2. Ensure these files are available in the workspace:
   - `AGENTS.md`
   - `CLAUDE.md`
   - `skills/`
   - `.opencode/`

## How It Works

1. Start with `skills/using-data-engineering-agent-skills/SKILL.md`
2. Let the agent choose the matching preset and task skill
3. Use references and templates only when they improve decisions or proof

## Suggested Mapping

- new data product -> `data-specification`
- pipeline implementation -> `pipeline-planning-and-task-breakdown` + execution skill
- validation and release gates -> `data-quality-and-contract-testing`
- production issue -> `incident-triage-and-pipeline-recovery`
- replay or cutover -> `orchestration-and-backfills`

## Recommended Workflow

Use natural language requests such as:

- design this new ingestion pipeline
- plan this schema migration
- validate this publish workflow
- review this dbt change
- backfill this date range safely

The agent should map that request to the lifecycle commands and skills automatically.
