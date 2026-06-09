#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".py",
    ".sql",
    ".yaml",
    ".yml",
    ".json",
    ".avsc",
    ".proto",
    ".tf",
    ".tfvars",
    ".ini",
    ".cfg",
    ".kts",
    ".scala",
    ".java",
    ".xml",
    ".sh",
    ".ps1",
    ".toml",
    ".txt",
    ".csv",
    ".tsv",
    ".md",
}

IMPLEMENTATION_SUFFIXES = TEXT_SUFFIXES - {".md", ".txt"}
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "target",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run data engineering repository hooks.")
    parser.add_argument(
        "hook",
        choices=[
            "session-start",
            "contract-check-pre",
            "pipeline-review-pre",
            "incident-mode",
            "backfill-guard",
            "schema-change-guard",
            "cost-check",
            "release-guard",
        ],
    )
    parser.add_argument("workspace", nargs="?", default=".")
    return parser.parse_args()


def iter_files(workspace: Path, include_docs: bool = True) -> list[Path]:
    allowed = TEXT_SUFFIXES if include_docs else IMPLEMENTATION_SUFFIXES
    files: list[Path] = []
    for path in workspace.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in allowed:
            continue
        files.append(path)
    return files


def has_glob(workspace: Path, *patterns: str) -> bool:
    for path in workspace.rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        relative = path.relative_to(workspace).as_posix()
        if any(fnmatch.fnmatch(relative, pattern) for pattern in patterns):
            return True
    return False


def search_text(workspace: Path, pattern: str, include_docs: bool = True) -> list[str]:
    regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
    hits: list[str] = []
    for file_path in iter_files(workspace, include_docs=include_docs):
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            if regex.search(line):
                hits.append(f"{file_path.relative_to(workspace)}:{number}: {line.strip()}")
    return hits


def contract_type_keys(text: str) -> list[str]:
    if re.search(r"^[ \t]*source_contract:", text, re.MULTILINE):
        return ["name", "owner", "cadence", "schema", "quality", "security"]
    if re.search(r"^[ \t]*dataset_contract:", text, re.MULTILINE):
        return ["name", "owner", "grain", "schema", "freshness", "quality", "compatibility"]
    if re.search(r"^[ \t]*metric_contract:", text, re.MULTILINE):
        return ["name", "owner", "definition", "freshness", "quality", "compatibility"]
    return []


def is_toolkit_repo(workspace: Path) -> bool:
    return (
        (workspace / "skills-index.md").exists()
        and (workspace / "registry" / "assets.json").exists()
        and (workspace / "skills" / "using-data-engineering-agent-skills" / "SKILL.md").exists()
    )


def run_session_start(workspace: Path) -> int:
    repo_signals: list[str] = []
    recommended_skills = ["skills/using-data-engineering-agent-skills/SKILL.md"]
    recommended_presets: list[str] = []
    recommended_starters: list[str] = []
    recommended_examples: list[str] = []
    next_command = "/spec"

    if is_toolkit_repo(workspace):
        print("\nData Engineering Hooks: session start")
        print(f"Workspace: {workspace}\n")
        print("Detected signals:\n- toolkit repository detected; stack auto-detection is limited to avoid self-matching")
        print("\nStart here:")
        print("- skills/using-data-engineering-agent-skills/SKILL.md")
        print("- skills/data-platform-ci-cd-and-release-management/SKILL.md")
        print("\nSuggested presets:")
        print("- presets/aws-data-engineering/PRESET.md or the platform preset matching the change you are making")
        print("\nSuggested starter packs:")
        print("- starter-packs/production-reliability-starter.yaml")
        print("- starter-packs/data-platform-cicd-release-starter.yaml")
        print("\nSuggested examples:")
        print("- examples/dbt-warehouse-marts/")
        print("- examples/kafka-flink-streaming/")
        print("\nSafe next command: /plan")
        print("Follow with: /validate before publish, /backfill for replay work, /ship only after rollback notes exist.")
        return 0

    if has_glob(workspace, "dbt_project.yml", "models/**/*.sql"):
        repo_signals.append("dbt-or-warehouse")
        recommended_skills.extend(
            [
                "skills/warehouse-and-schema-design/SKILL.md",
                "skills/dbt-and-analytics-engineering/SKILL.md",
            ]
        )
        recommended_starters.append("starter-packs/warehouse-analytics-starter.yaml")
        recommended_examples.append("examples/dbt-warehouse-marts/")

    if has_glob(workspace, "dataform.json", "workflow_settings.yaml", "definitions/**/*.sqlx"):
        repo_signals.append("bigquery-dataform")
        recommended_skills.append("skills/bigquery-and-dataform-platform-engineering/SKILL.md")
        recommended_presets.append("presets/gcp-data-engineering/PRESET.md")

    if search_text(
        workspace,
        r"glue data catalog|lake formation|lf-tag|athena grant|resource link",
        include_docs=False,
    ):
        repo_signals.append("aws-native-governance")
        recommended_skills.append("skills/glue-data-catalog-and-lake-formation-governance/SKILL.md")
        recommended_presets.append("presets/aws-data-engineering/PRESET.md")

    if search_text(
        workspace,
        r"unity catalog|external location|storage credential|catalog\.schema|delta sharing",
        include_docs=False,
    ):
        repo_signals.append("unity-catalog-governance")
        recommended_skills.append("skills/unity-catalog-and-lakehouse-governance/SKILL.md")
        recommended_presets.append("presets/databricks-lakehouse-engineering/PRESET.md")

    if search_text(
        workspace,
        r"purview|microsoft purview|collection admin|data map|classification rule|endorsement",
        include_docs=False,
    ):
        repo_signals.append("azure-governance")
        recommended_skills.append("skills/microsoft-purview-and-azure-data-governance/SKILL.md")
        recommended_presets.append("presets/azure-data-engineering/PRESET.md")

    if search_text(workspace, r"dataplex|policy tag|bigquery data policy|google data catalog", include_docs=False):
        repo_signals.append("gcp-governance")
        recommended_skills.append("skills/dataplex-and-bigquery-governance/SKILL.md")
        recommended_presets.append("presets/gcp-data-engineering/PRESET.md")

    if has_glob(workspace, "pyproject.toml", "requirements.txt", "poetry.lock", "**/*.py"):
        repo_signals.append("python")
        recommended_skills.append("skills/python-data-engineering-and-pipeline-packaging/SKILL.md")

    if has_glob(workspace, "build.sbt", "project/build.properties", "**/*.scala"):
        repo_signals.append("scala-jvm-data")
        recommended_skills.append("skills/scala-data-engineering-on-jvm-runtimes/SKILL.md")

    if has_glob(workspace, "pom.xml", "build.gradle", "build.gradle.kts", "**/*.java"):
        repo_signals.append("java-data-service")
        recommended_skills.append("skills/java-data-engineering-and-integration-services/SKILL.md")

    if search_text(workspace, r"mysql|postgres|mongodb|mongo|dynamodb|cassandra|redis|documentdb|cosmos db|nosql", include_docs=False):
        repo_signals.append("operational-datastore-choice")
        recommended_skills.append("skills/operational-datastore-selection-relational-and-nosql/SKILL.md")

    if search_text(workspace, r"\betl\b|\belt\b|pushdown|transformation layer|staging layer|curated layer", include_docs=False):
        repo_signals.append("etl-elt")
        recommended_skills.append("skills/etl-elt-and-modernization-strategy/SKILL.md")

    if has_glob(workspace, "dags/**/*.py", "airflow.cfg", "**/dags/**/*.py"):
        repo_signals.append("airflow")
        recommended_skills.extend(
            [
                "skills/airflow-and-workflow-orchestration/SKILL.md",
                "skills/orchestration-and-backfills/SKILL.md",
            ]
        )
        recommended_presets.append("presets/apache-airflow-orchestration/PRESET.md")

    if has_glob(workspace, "databricks.yml", "**/*.dbc", "**/*.ipynb"):
        repo_signals.append("databricks-or-notebook")
        recommended_skills.extend(
            [
                "skills/delta-lake-and-medallion-architecture/SKILL.md",
                "skills/notebook-to-production-hardening/SKILL.md",
            ]
        )
        recommended_presets.append("presets/databricks-lakehouse-engineering/PRESET.md")
        recommended_examples.append("examples/databricks-delta-medallion/")

    if search_text(workspace, r"snowflake|snowpipe|dynamic table|stream\(|create task|row access policy|masking policy", include_docs=False):
        repo_signals.append("snowflake-native")
        recommended_skills.append("skills/snowflake-native-pipelines-and-governance/SKILL.md")
        recommended_presets.append("presets/snowflake-modern-data-platform/PRESET.md")

    if has_glob(workspace, "**/*.tf", "**/*.tfvars"):
        repo_signals.append("terraform")
        recommended_skills.append("skills/terraform-and-data-platform-infrastructure/SKILL.md")

    if has_glob(workspace, ".github/workflows/*.yml", ".github/workflows/*.yaml", ".gitlab-ci.yml", "azure-pipelines*.yml", "Jenkinsfile"):
        repo_signals.append("cicd")
        recommended_skills.append("skills/data-platform-ci-cd-and-release-management/SKILL.md")
        recommended_starters.append("starter-packs/data-platform-cicd-release-starter.yaml")
        next_command = "/plan"

    if has_glob(workspace, "docker-compose.yml", "compose.yaml"):
        repo_signals.append("local-sandbox")

    if has_glob(workspace, "schemas/**/*.avsc", "schemas/**/*.proto", "**/*schema*.json"):
        repo_signals.append("schema-registry")
        recommended_skills.extend(
            [
                "skills/avro-protobuf-json-schema-registry/SKILL.md",
                "skills/data-contract-testing-with-schema-registry/SKILL.md",
            ]
        )

    if has_glob(workspace, "**/talend.project", "**/*.item", "**/*.job") or search_text(
        workspace, r"informatica|powercenter|iics|talend|datastage|ssis|matillion", include_docs=False
    ):
        repo_signals.append("enterprise-etl")
        recommended_skills.append("skills/enterprise-etl-and-data-integration-modernization/SKILL.md")
        recommended_presets.extend(
            [
                "presets/informatica-data-integration/PRESET.md",
                "presets/talend-data-integration/PRESET.md",
            ]
        )
        recommended_starters.append("starter-packs/enterprise-etl-modernization-starter.yaml")
        next_command = "/plan"

    if (
        has_glob(workspace, "**/*kafka*", "docker-compose.yml")
        and search_text(workspace, r"kafka|flink|debezium|schema registry", include_docs=False)
    ):
        repo_signals.append("streaming")
        recommended_skills.extend(
            [
                "skills/streaming-and-messaging-systems/SKILL.md",
                "skills/kafka-resilience-and-schema-evolution/SKILL.md",
                "skills/mcp-data-observability-integration/SKILL.md",
                "skills/incident-triage-and-pipeline-recovery/SKILL.md",
            ]
        )
        recommended_presets.extend(
            [
                "presets/apache-kafka-streaming/PRESET.md",
                "presets/apache-flink-stream-processing/PRESET.md",
            ]
        )
        recommended_starters.append("starter-packs/streaming-reliability-starter.yaml")
        recommended_examples.append("examples/kafka-flink-streaming/")
        next_command = "/plan"

    if search_text(
        workspace,
        r"masked|masking|obfuscat|tokeniz|tokenis|synthetic data|test data|seed data|lower environment|non-prod|qa refresh|staging refresh",
        include_docs=False,
    ):
        repo_signals.append("test-data-or-lower-env")
        recommended_skills.extend(
            [
                "skills/test-data-preparation-and-synthetic-data/SKILL.md",
                "skills/lower-environment-data-masking-and-obfuscation/SKILL.md",
            ]
        )
        recommended_starters.append("starter-packs/test-data-lower-environments-starter.yaml")

    if has_glob(workspace, "**/*.csv", "**/*.tsv", "**/*.json", "**/*.xml") and search_text(
        workspace, r"sftp|mft|partner feed|checksum|manifest|control total|late file|file drop", include_docs=False
    ):
        repo_signals.append("file-ingestion")
        recommended_skills.extend(
            [
                "skills/file-and-partner-feed-ingestion/SKILL.md",
                "skills/source-reliability-and-extraction-resilience/SKILL.md",
            ]
        )
        next_command = "/plan"

    if search_text(
        workspace,
        r"not_null|unique|freshness|reconcile|reconciliation|expectation|great expectations|deequ|cuallee|masking|access control|security review",
        include_docs=False,
    ):
        repo_signals.append("validation-or-security-review")
        recommended_skills.extend(
            [
                "skills/data-quality-and-contract-testing/SKILL.md",
                "skills/data-security-compliance-and-regulated-data/SKILL.md",
            ]
        )
        recommended_starters.append("starter-packs/validation-security-review-starter.yaml")

    if search_text(
        workspace,
        r"great expectations|deequ|cuallee|soda|dbt test|quality suite|expectation suite|quality monitor",
        include_docs=False,
    ):
        repo_signals.append("quality-tooling")
        recommended_skills.extend(
            [
                "skills/data-quality-platforms-and-rule-management/SKILL.md",
                "skills/great-expectations-deequ-and-cuallee/SKILL.md",
            ]
        )

    if search_text(
        workspace,
        r"resilien|resilienc|chaos|failure injection|failover|disaster recovery|dr drill|recovery drill|checkpoint recovery|duplicate delivery|retry storm",
        include_docs=False,
    ):
        repo_signals.append("resiliency-testing")
        recommended_skills.extend(
            [
                "skills/data-resiliency-testing-and-failure-injection/SKILL.md",
                "skills/data-observability-and-sla-management/SKILL.md",
                "skills/incident-triage-and-pipeline-recovery/SKILL.md",
            ]
        )
        recommended_starters.append("starter-packs/resiliency-testing-starter.yaml")
        recommended_starters.append("starter-packs/production-reliability-starter.yaml")

    if search_text(
        workspace,
        r"lambda|serverless|emr serverless|glue.*streaming|checkpoint|state.store|orphan|iceguard",
        include_docs=False,
    ):
        repo_signals.append("serverless-spark")
        recommended_skills.extend(
            [
                "skills/spark-serverless-reliability-and-state-management/SKILL.md",
                "skills/mcp-data-observability-integration/SKILL.md",
            ]
        )
        recommended_presets.append("presets/apache-spark-engineering/PRESET.md")
        recommended_starters.append("starter-packs/production-reliability-starter.yaml")
        next_command = "/plan"

    if search_text(workspace, r"rto|rpo|business continuity|restore drill|backup restore|failover region|cross-region restore|cross-account restore", include_docs=False):
        repo_signals.append("platform-dr")
        recommended_skills.append("skills/data-platform-disaster-recovery-and-business-continuity/SKILL.md")
        next_command = "/plan"

    if search_text(workspace, r"cobol|jcl|vsam|ims|db2 z/os|copybook|mainframe|packed decimal|ebcdic", include_docs=False):
        repo_signals.append("mainframe-modernization")
        recommended_skills.extend(
            [
                "skills/mainframe-modernization-and-data-offload/SKILL.md",
                "skills/data-migration-and-platform-cutover/SKILL.md",
            ]
        )
        next_command = "/plan"

    if search_text(workspace, r"gdpr|pdpl|dpdp|sama|sovereignty|data residency|cross-border|data transfer|csrd|esg|esrs|brsr|sustainability reporting", include_docs=False):
        repo_signals.append("regional-compliance-or-esg")
        recommended_skills.append("skills/regional-data-compliance-and-sovereignty/SKILL.md")
        recommended_starters.append("starter-packs/regional-compliance-and-esg-reporting-starter.yaml")

    if search_text(workspace, r"csrd|esg|esrs|brsr|scope 1|scope 2|scope 3|double materiality|sustainability statement", include_docs=False):
        repo_signals.append("esg-reporting")
        recommended_skills.append("skills/esg-and-sustainability-regulatory-reporting/SKILL.md")

    if has_glob(workspace, "contracts/**/*.yaml", "contracts/**/*.yml", "**/*contract*.yaml", "**/*contract*.yml"):
        repo_signals.append("contracts-present")
        next_command = "/plan"

    if not recommended_presets:
        recommended_presets.append("presets/aws-data-engineering/PRESET.md or the platform preset matching your environment")
    if not recommended_starters:
        recommended_starters.append("starter-packs/aws-lakehouse-starter.yaml or starter-packs/warehouse-analytics-starter.yaml")
    if not recommended_examples:
        recommended_examples.append("examples/aws-s3-glue-athena-iceberg/ or examples/dbt-warehouse-marts/")

    print("\nData Engineering Hooks: session start")
    print(f"Workspace: {workspace}\n")
    if repo_signals:
        print("Detected signals:")
        for signal in dict.fromkeys(repo_signals):
            print(f"- {signal}")
    else:
        print("Detected signals:\n- no strong stack signal detected yet")

    print("\nStart here:")
    for item in dict.fromkeys(recommended_skills):
        print(f"- {item}")

    print("\nSuggested presets:")
    for item in dict.fromkeys(recommended_presets):
        print(f"- {item}")

    print("\nSuggested starter packs:")
    for item in dict.fromkeys(recommended_starters):
        print(f"- {item}")

    print("\nSuggested examples:")
    for item in dict.fromkeys(recommended_examples):
        print(f"- {item}")

    print(f"\nSafe next command: {next_command}")
    print("Follow with: /validate before publish, /backfill for replay work, /ship only after rollback notes exist.")
    return 0


def run_contract_check_pre(workspace: Path) -> int:
    contract_files = [
        path
        for path in workspace.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".yaml", ".yml"}
        and ("contract" in path.name.lower() or "contracts" in path.as_posix().lower())
    ]
    if not contract_files:
        print("No contract files found.")
        print(
            "Create one from templates/source-contract.yaml, templates/dataset-contract.yaml, or templates/metric-contract.yaml before planning or build work."
        )
        return 1

    errors = 0
    for file_path in contract_files:
        print(f"Checking {file_path}")
        text = file_path.read_text(encoding="utf-8")
        required_keys = contract_type_keys(text)
        if not required_keys:
            print(f"Could not identify contract type for {file_path}")
            print("Expected one of: source_contract, dataset_contract, metric_contract")
            errors += 1
            continue
        for key in required_keys:
            if not re.search(rf"^[ \t]*{re.escape(key)}:", text, re.MULTILINE):
                print(f"Missing required key '{key}' in {file_path}")
                errors += 1

    if errors:
        print(f"\nContract validation failed with {errors} issue(s).")
        print("Use /spec to define missing ownership, schema, freshness, quality, and compatibility details before implementation.")
        return 1

    print("\nContract validation passed.")
    print("Safe next step: /plan or /build if the contract is approved.")
    return 0


def run_pipeline_review_pre(workspace: Path) -> int:
    missing: list[str] = []
    if not (
        has_glob(workspace, "tests/**/*", "test/**/*", "**/*test*.py", "**/*test*.sql")
        or has_glob(workspace, "benchmarks/**/*")
    ):
        missing.append("tests, benchmarks, or validation queries")
    if not has_glob(workspace, "**/*contract*.yaml", "**/*contract*.yml"):
        missing.append("contract artifacts")
    if not search_text(workspace, r"lineage|openlineage|datahub|openmetadata|upstream|downstream", include_docs=True):
        missing.append("lineage notes or metadata wiring")
    if not search_text(workspace, r"rollback|backout|restore|revert", include_docs=True):
        missing.append("rollback or recovery notes")
    if not search_text(workspace, r"owner|ownership|oncall|pager", include_docs=True):
        missing.append("ownership or escalation notes")
    if not search_text(workspace, r"quality|reconcile|reconciliation|not_null|unique|freshness", include_docs=True):
        missing.append("quality gates or reconciliation evidence")

    print(f"Pipeline review pre-check for {workspace}")
    if not missing:
        print("Pre-review evidence looks healthy.")
        print("Safe next step: /review")
        return 0

    print("Missing or weak review evidence:")
    for item in missing:
        print(f"- {item}")
    print("\nBefore /review or /ship, add evidence for reliability, lineage, quality, ownership, and rollback.")
    return 1


def run_incident_mode(_: Path) -> int:
    print("Incident mode enabled.\n")
    print("Load these skills first:")
    print("- skills/incident-triage-and-pipeline-recovery/SKILL.md")
    print("- skills/mcp-data-observability-integration/SKILL.md")
    print("- skills/data-observability-and-sla-management/SKILL.md")
    print("- skills/safe-backfill-and-replay-orchestration/SKILL.md (when replay or backfill is required)")
    print("- skills/kafka-resilience-and-schema-evolution/SKILL.md (when Kafka lag, DLQ, or schema drift is involved)")
    print("- skills/orchestration-and-backfills/SKILL.md\n")
    print("Use these references and templates:")
    print("- templates/incident-runbook.md")
    print("- references/incident-recovery-checklist.md")
    print("- references/observability-and-sla-checklist.md\n")
    print("Immediate priorities:")
    print("1. contain bad publishes before broad reruns")
    print("2. preserve evidence before mutation")
    print("3. define the affected window, consumers, and metrics")
    print("4. choose rerun, replay, rollback, or partial correction intentionally")
    print("5. reopen publish only after reconciliation and freshness validation")
    return 0


def run_backfill_guard(workspace: Path) -> int:
    print(f"Backfill guard for {workspace}\n")
    print("Answer these before replay or cutover work:")
    print("- what exact time window or partition range is affected?")
    print("- is the job idempotent and safe to rerun?")
    print("- which downstream datasets, dashboards, and SLAs will move?")
    print("- what metric reconciliation proves the replay is correct?")
    print("- what is the rollback or re-close strategy if the replay is wrong?\n")

    missing = 0
    if has_glob(workspace, "dags/**/*.py"):
        dag_hits = search_text(workspace, r"catchup\s*=\s*True", include_docs=False)
        if not dag_hits:
            print("No Airflow DAG with catchup=True was found for replay-safe backfill orchestration.")
            missing = 1
    if not search_text(workspace, r"backfill|replay|rerun|cutover|reconcile|rollback", include_docs=True):
        print("No replay or rollback notes were found in the workspace.")
        missing = 1
    if not search_text(workspace, r"time window|partition|date range|affected window", include_docs=True):
        print("No affected window or partition range was found.")
        missing = 1
    if not search_text(workspace, r"reconcile|reconciliation|row count|metric", include_docs=True):
        print("No reconciliation evidence was found.")
        missing = 1

    print("\nRecommended skills:")
    print("- skills/safe-backfill-and-replay-orchestration/SKILL.md")
    print("- skills/orchestration-and-backfills/SKILL.md")
    print("- skills/data-migration-and-platform-cutover/SKILL.md")
    print("- skills/data-reconciliation-and-financial-controls/SKILL.md")
    print("- skills/mcp-data-observability-integration/SKILL.md (when live lag or run state bounds the replay window)")
    print("Starter template: templates/backfill-plan.yaml")

    if missing:
        print("\nBackfill guard failed. Capture the missing replay details before execution.")
        return 1
    print("\nBackfill guard passed.")
    return 0


def run_schema_change_guard(workspace: Path) -> int:
    print(f"Schema change guard for {workspace}\n")
    patterns = [
        ("drop column", r"drop[ \t]+column"),
        ("rename column", r"rename[ \t]+column"),
        ("alter column", r"alter[ \t]+column"),
        ("replace table", r"replace[ \t]+table"),
        ("truncate table", r"truncate[ \t]+table"),
        ("full refresh", r"full-refresh"),
    ]
    hits = 0
    for label, pattern in patterns:
        matches = search_text(workspace, pattern, include_docs=False)
        if matches:
            print(f"Risky pattern detected: {label}")
            for match in matches[:10]:
                print(match)
            print()
            hits = 1

    if hits:
        print("Breaking or destructive schema signals were found.")
        print("Use these skills before merging:")
        print("- skills/schema-evolution-and-contract-migrations/SKILL.md")
        print("- skills/data-contract-testing-with-schema-registry/SKILL.md")
        print("- skills/data-sharing-and-publishing-contracts/SKILL.md")
        print("Starter template: templates/schema-change-plan.yaml")
        return 1

    print("No obvious destructive schema patterns detected.")
    return 0


def run_cost_check(workspace: Path) -> int:
    print(f"Cost check for {workspace}\n")
    patterns = [
        ("SELECT * in SQL models", r"select[ \t]+\*"),
        ("cross joins", r"cross[ \t]+join"),
        ("destructive dbt full refresh usage", r"dbt[ \t]+run.*full-refresh|full-refresh"),
        ("Spark repartition or coalesce usage", r"repartition\(|coalesce\("),
        ("explode-heavy transformations", r"explode\("),
        ("warehouse cost estimate calls", r"query_cost_estimate|EXPLAIN|bytes processed"),
    ]
    warnings = 0
    for label, pattern in patterns:
        matches = search_text(workspace, pattern, include_docs=False)
        if matches:
            print(f"Potential cost hotspot: {label}")
            for match in matches[:10]:
                print(match)
            print()
            warnings = 1

    if warnings:
        print("Review these skills before shipping:")
        print("- skills/warehouse-performance-and-cost-optimization/SKILL.md")
        print("- skills/spark-and-distributed-processing/SKILL.md")
        print("- skills/data-observability-and-sla-management/SKILL.md")
        return 1

    print("No obvious high-cost patterns were detected.")
    return 0


def run_release_guard(workspace: Path) -> int:
    missing: list[str] = []
    checks = [
        (r"rollback|backout|restore|revert|forward-fix", "rollback or forward-fix notes"),
        (r"shadow|canary|dual-run|dual read|dual-write|staged validation|progressive release", "staged validation or progressive-release evidence"),
        (r"reconcile|reconciliation|parity|row count|metric parity", "reconciliation or parity evidence"),
        (r"publish|consumer cutover|visibility toggle|feature flag|dataset swap|view swap", "publish separation or consumer-cutover plan"),
        (r"monitor|observability|alert|sla|lag|checkpoint|freshness", "post-release observability notes"),
        (r"owner|approver|approval|oncall|pager", "release ownership or approval path"),
    ]
    for pattern, label in checks:
        if not search_text(workspace, pattern, include_docs=True):
            missing.append(label)

    print(f"Release guard for {workspace}")
    if not missing:
        print("Release evidence looks healthy.")
        print("Safe next step: /ship")
        return 0

    print("Missing or weak release evidence:")
    for item in missing:
        print(f"- {item}")
    print("\nBefore /ship, capture staged validation, publish control, reconciliation, observability, ownership, and rollback evidence.")
    print("Starter template: templates/release-gate-evidence.yaml")
    return 1


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).resolve()
    handlers = {
        "session-start": run_session_start,
        "contract-check-pre": run_contract_check_pre,
        "pipeline-review-pre": run_pipeline_review_pre,
        "incident-mode": run_incident_mode,
        "backfill-guard": run_backfill_guard,
        "schema-change-guard": run_schema_change_guard,
        "cost-check": run_cost_check,
        "release-guard": run_release_guard,
    }
    return handlers[args.hook](workspace)


if __name__ == "__main__":
    sys.exit(main())
