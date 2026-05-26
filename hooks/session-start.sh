#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${1:-$PWD}"
shopt -s globstar nullglob

has_match() {
  local pattern="$1"
  local matches=("$WORKSPACE"/$pattern)
  [[ ${#matches[@]} -gt 0 ]]
}

repo_signals=()
recommended_skills=("skills/using-data-engineering-agent-skills/SKILL.md")
recommended_presets=()
recommended_starters=()
recommended_examples=()
next_command="/spec"

if has_match "dbt_project.yml" || has_match "models/**/*.sql"; then
  repo_signals+=("dbt-or-warehouse")
  recommended_skills+=("skills/warehouse-and-schema-design/SKILL.md" "skills/dbt-and-analytics-engineering/SKILL.md")
  recommended_starters+=("starter-packs/warehouse-analytics-starter.yaml")
  recommended_examples+=("examples/dbt-warehouse-marts/")
fi

if has_match "dataform.json" || has_match "workflow_settings.yaml" || has_match "definitions/**/*.sqlx"; then
  repo_signals+=("bigquery-dataform")
  recommended_skills+=("skills/bigquery-and-dataform-platform-engineering/SKILL.md")
  recommended_presets+=("presets/gcp-data-engineering/PRESET.md")
fi

if rg -n -i "glue data catalog|lake formation|lf-tag|athena grant|resource link" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("aws-native-governance")
  recommended_skills+=("skills/glue-data-catalog-and-lake-formation-governance/SKILL.md")
  recommended_presets+=("presets/aws-data-engineering/PRESET.md")
fi

if rg -n -i "unity catalog|external location|storage credential|catalog\\.schema|delta sharing" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("unity-catalog-governance")
  recommended_skills+=("skills/unity-catalog-and-lakehouse-governance/SKILL.md")
  recommended_presets+=("presets/databricks-lakehouse-engineering/PRESET.md")
fi

if rg -n -i "purview|microsoft purview|collection admin|data map|classification rule|endorsement" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("azure-governance")
  recommended_skills+=("skills/microsoft-purview-and-azure-data-governance/SKILL.md")
  recommended_presets+=("presets/azure-data-engineering/PRESET.md")
fi

if rg -n -i "dataplex|policy tag|bigquery data policy|google data catalog" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("gcp-governance")
  recommended_skills+=("skills/dataplex-and-bigquery-governance/SKILL.md")
  recommended_presets+=("presets/gcp-data-engineering/PRESET.md")
fi

if has_match "pyproject.toml" || has_match "requirements.txt" || has_match "poetry.lock" || has_match "**/*.py"; then
  repo_signals+=("python")
  recommended_skills+=("skills/python-data-engineering-and-pipeline-packaging/SKILL.md")
fi

if has_match "build.sbt" || has_match "project/build.properties" || has_match "**/*.scala"; then
  repo_signals+=("scala-jvm-data")
  recommended_skills+=("skills/scala-data-engineering-on-jvm-runtimes/SKILL.md")
fi

if has_match "pom.xml" || has_match "build.gradle" || has_match "build.gradle.kts" || has_match "**/*.java"; then
  repo_signals+=("java-data-service")
  recommended_skills+=("skills/java-data-engineering-and-integration-services/SKILL.md")
fi

if rg -n -i "mysql|postgres|mongodb|mongo|dynamodb|cassandra|redis|documentdb|cosmos db|nosql" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("operational-datastore-choice")
  recommended_skills+=("skills/operational-datastore-selection-relational-and-nosql/SKILL.md")
fi

if rg -n -i "\betl\b|\belt\b|pushdown|transformation layer|staging layer|curated layer" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("etl-elt")
  recommended_skills+=("skills/etl-elt-and-modernization-strategy/SKILL.md")
fi

if has_match "dags/**/*.py" || has_match "airflow.cfg" || has_match "**/dags/**/*.py"; then
  repo_signals+=("airflow")
  recommended_skills+=("skills/airflow-and-workflow-orchestration/SKILL.md" "skills/orchestration-and-backfills/SKILL.md")
  recommended_presets+=("presets/apache-airflow-orchestration/PRESET.md")
fi

if has_match "databricks.yml" || has_match "**/*.dbc" || has_match "**/*.ipynb"; then
  repo_signals+=("databricks-or-notebook")
  recommended_skills+=("skills/delta-lake-and-medallion-architecture/SKILL.md" "skills/notebook-to-production-hardening/SKILL.md")
  recommended_presets+=("presets/databricks-lakehouse-engineering/PRESET.md")
  recommended_examples+=("examples/databricks-delta-medallion/")
fi

if rg -n -i "snowflake|snowpipe|dynamic table|stream\\(|create task|row access policy|masking policy" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("snowflake-native")
  recommended_skills+=("skills/snowflake-native-pipelines-and-governance/SKILL.md")
  recommended_presets+=("presets/snowflake-modern-data-platform/PRESET.md")
fi

if has_match "**/*.tf" || has_match "**/*.tfvars"; then
  repo_signals+=("terraform")
  recommended_skills+=("skills/terraform-and-data-platform-infrastructure/SKILL.md")
fi

if has_match ".github/workflows/*.yml" || has_match ".github/workflows/*.yaml" || has_match ".gitlab-ci.yml" || has_match "azure-pipelines*.yml" || has_match "Jenkinsfile"; then
  repo_signals+=("cicd")
  recommended_skills+=("skills/data-platform-ci-cd-and-release-management/SKILL.md")
  recommended_starters+=("starter-packs/data-platform-cicd-release-starter.yaml")
  next_command="/plan"
fi

if has_match "docker-compose.yml" || has_match "compose.yaml"; then
  repo_signals+=("local-sandbox")
fi

if has_match "schemas/**/*.avsc" || has_match "schemas/**/*.proto" || has_match "**/*schema*.json"; then
  repo_signals+=("schema-registry")
  recommended_skills+=("skills/avro-protobuf-json-schema-registry/SKILL.md" "skills/data-contract-testing-with-schema-registry/SKILL.md")
fi

if has_match "**/talend.project" || has_match "**/*.item" || has_match "**/*.job"; then
  repo_signals+=("enterprise-etl")
  recommended_skills+=("skills/enterprise-etl-and-data-integration-modernization/SKILL.md")
  recommended_presets+=("presets/talend-data-integration/PRESET.md")
  recommended_starters+=("starter-packs/enterprise-etl-modernization-starter.yaml")
  next_command="/plan"
elif rg -n -i "informatica|powercenter|iics|talend|datastage|ssis|matillion" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("enterprise-etl")
  recommended_skills+=("skills/enterprise-etl-and-data-integration-modernization/SKILL.md")
  recommended_presets+=("presets/informatica-data-integration/PRESET.md" "presets/talend-data-integration/PRESET.md")
  recommended_starters+=("starter-packs/enterprise-etl-modernization-starter.yaml")
  next_command="/plan"
fi

if has_match "**/*kafka*" || has_match "docker-compose.yml"; then
  if rg -n -i "kafka|flink|debezium|schema registry" "$WORKSPACE" >/dev/null 2>&1; then
    repo_signals+=("streaming")
    recommended_skills+=("skills/streaming-and-messaging-systems/SKILL.md" "skills/incident-triage-and-pipeline-recovery/SKILL.md")
    recommended_presets+=("presets/apache-kafka-streaming/PRESET.md" "presets/apache-flink-stream-processing/PRESET.md")
    recommended_starters+=("starter-packs/streaming-reliability-starter.yaml")
    recommended_examples+=("examples/kafka-flink-streaming/")
    next_command="/plan"
  fi
fi

if rg -n -i "masked|masking|obfuscat|tokeniz|tokenis|synthetic data|test data|seed data|lower environment|non-prod|qa refresh|staging refresh" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("test-data-or-lower-env")
  recommended_skills+=("skills/test-data-preparation-and-synthetic-data/SKILL.md" "skills/lower-environment-data-masking-and-obfuscation/SKILL.md")
  recommended_starters+=("starter-packs/test-data-lower-environments-starter.yaml")
fi

if has_match "**/*.csv" || has_match "**/*.tsv" || has_match "**/*.json" || has_match "**/*.xml"; then
  if rg -n -i "sftp|mft|partner feed|checksum|manifest|control total|late file|file drop" "$WORKSPACE" >/dev/null 2>&1; then
    repo_signals+=("file-ingestion")
    recommended_skills+=("skills/file-and-partner-feed-ingestion/SKILL.md" "skills/source-reliability-and-extraction-resilience/SKILL.md")
    next_command="/plan"
  fi
fi

if rg -n -i "not_null|unique|freshness|reconcile|reconciliation|expectation|great expectations|deequ|cuallee|masking|access control|security review" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("validation-or-security-review")
  recommended_skills+=("skills/data-quality-and-contract-testing/SKILL.md" "skills/data-security-compliance-and-regulated-data/SKILL.md")
  recommended_starters+=("starter-packs/validation-security-review-starter.yaml")
fi

if rg -n -i "great expectations|deequ|cuallee|soda|dbt test|quality suite|expectation suite|quality monitor" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("quality-tooling")
  recommended_skills+=("skills/data-quality-platforms-and-rule-management/SKILL.md" "skills/great-expectations-deequ-and-cuallee/SKILL.md")
fi

if rg -n -i "resilien|resilienc|chaos|failure injection|failover|disaster recovery|dr drill|recovery drill|checkpoint recovery|duplicate delivery|retry storm" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("resiliency-testing")
  recommended_skills+=("skills/data-resiliency-testing-and-failure-injection/SKILL.md" "skills/data-observability-and-sla-management/SKILL.md" "skills/incident-triage-and-pipeline-recovery/SKILL.md")
  recommended_starters+=("starter-packs/resiliency-testing-starter.yaml")
  next_command="/plan"
fi

if rg -n -i "rto|rpo|business continuity|restore drill|backup restore|failover region|cross-region restore|cross-account restore" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("platform-dr")
  recommended_skills+=("skills/data-platform-disaster-recovery-and-business-continuity/SKILL.md")
  next_command="/plan"
fi

if rg -n -i "cobol|jcl|vsam|ims|db2 z/os|copybook|mainframe|packed decimal|ebcdic" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("mainframe-modernization")
  recommended_skills+=("skills/mainframe-modernization-and-data-offload/SKILL.md" "skills/data-migration-and-platform-cutover/SKILL.md")
  next_command="/plan"
fi

if rg -n -i "gdpr|pdpl|dpdp|sama|sovereignty|data residency|cross-border|data transfer|csrd|esg|esrs|brsr|sustainability reporting" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("regional-compliance-or-esg")
  recommended_skills+=("skills/regional-data-compliance-and-sovereignty/SKILL.md")
  recommended_starters+=("starter-packs/regional-compliance-and-esg-reporting-starter.yaml")
fi

if rg -n -i "csrd|esg|esrs|brsr|scope 1|scope 2|scope 3|double materiality|sustainability statement" "$WORKSPACE" >/dev/null 2>&1; then
  repo_signals+=("esg-reporting")
  recommended_skills+=("skills/esg-and-sustainability-regulatory-reporting/SKILL.md")
fi

if has_match "contracts/**/*.yaml" || has_match "**/*contract*.yaml"; then
  repo_signals+=("contracts-present")
  next_command="/plan"
fi

if [[ ${#recommended_presets[@]} -eq 0 ]]; then
  recommended_presets+=("presets/aws-data-engineering/PRESET.md or the platform preset matching your environment")
fi

if [[ ${#recommended_starters[@]} -eq 0 ]]; then
  recommended_starters+=("starter-packs/aws-lakehouse-starter.yaml or starter-packs/warehouse-analytics-starter.yaml")
fi

if [[ ${#recommended_examples[@]} -eq 0 ]]; then
  recommended_examples+=("examples/aws-s3-glue-athena-iceberg/ or examples/dbt-warehouse-marts/")
fi

printf '\nData Engineering Hooks: session start\n'
printf 'Workspace: %s\n\n' "$WORKSPACE"

if [[ ${#repo_signals[@]} -gt 0 ]]; then
  printf 'Detected signals:\n'
  printf -- '- %s\n' "${repo_signals[@]}"
else
  printf 'Detected signals:\n- no strong stack signal detected yet\n'
fi

printf '\nStart here:\n'
printf -- '- %s\n' "${recommended_skills[@]}" | awk '!seen[$0]++'

printf '\nSuggested presets:\n'
printf -- '- %s\n' "${recommended_presets[@]}" | awk '!seen[$0]++'

printf '\nSuggested starter packs:\n'
printf -- '- %s\n' "${recommended_starters[@]}" | awk '!seen[$0]++'

printf '\nSuggested examples:\n'
printf -- '- %s\n' "${recommended_examples[@]}" | awk '!seen[$0]++'

printf '\nSafe next command: %s\n' "$next_command"
printf 'Follow with: /validate before publish, /backfill for replay work, /ship only after rollback notes exist.\n'
