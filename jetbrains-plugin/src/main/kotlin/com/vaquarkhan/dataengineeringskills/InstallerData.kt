package com.vaquarkhan.dataengineeringskills

object InstallerData {
    const val RAW_BASE_URL = "https://raw.githubusercontent.com/vaquarkhan/data-engineering-agent-skills/main"

    val coreFiles = listOf(
        "AGENTS.md",
        "skills-index.md",
        "templates/source-contract.yaml",
        "templates/dataset-contract.yaml",
        "templates/metric-contract.yaml",
        "templates/incident-runbook.md",
        "docs/codex-setup.md"
    )

    val agentAdapters = linkedMapOf(
        "Cursor" to listOf(
            ".cursor/rules/00-data-agent-core.mdc",
            ".cursor/rules/10-spec-first.mdc",
            ".cursor/rules/20-platform-preset-selector.mdc",
            ".cursor/rules/30-quality-gates.mdc"
        ),
        "Claude" to listOf(
            ".claude/commands/spec.md",
            ".claude/commands/plan.md",
            ".claude/commands/build.md",
            ".claude/commands/test.md",
            ".claude/commands/review.md",
            ".claude/commands/ship.md",
            "AGENTS.md"
        ),
        "Copilot" to listOf(
            ".github/copilot-instructions.md",
            "AGENTS.md"
        ),
        "Gemini" to listOf(
            ".gemini/commands/spec.md",
            ".gemini/commands/plan.md",
            ".gemini/commands/build.md",
            ".gemini/commands/test.md",
            ".gemini/commands/review.md",
            ".gemini/commands/ship.md"
        ),
        "Codex" to listOf(
            "AGENTS.md",
            "skills-index.md",
            "docs/codex-setup.md"
        )
    )

    val starterPacks = linkedMapOf(
        "AWS Lakehouse" to listOf(
            "starter-packs/aws-lakehouse-starter.yaml",
            "templates/source-contract.yaml",
            "templates/dataset-contract.yaml",
            "AGENTS.md",
            "skills-index.md"
        ),
        "Databricks Medallion" to listOf(
            "starter-packs/databricks-medallion-starter.yaml",
            "templates/source-contract.yaml",
            "templates/dataset-contract.yaml",
            "AGENTS.md",
            "skills-index.md"
        ),
        "Warehouse Analytics" to listOf(
            "starter-packs/warehouse-analytics-starter.yaml",
            "templates/dataset-contract.yaml",
            "templates/metric-contract.yaml",
            "AGENTS.md",
            "skills-index.md"
        ),
        "Streaming Reliability" to listOf(
            "starter-packs/streaming-reliability-starter.yaml",
            "templates/source-contract.yaml",
            "templates/incident-runbook.md",
            "AGENTS.md",
            "skills-index.md"
        ),
        "Privacy Governance" to listOf(
            "starter-packs/privacy-governance-starter.yaml",
            "templates/dataset-contract.yaml",
            "templates/incident-runbook.md",
            "AGENTS.md",
            "skills-index.md"
        )
    )

    val mcpTemplates = linkedMapOf(
        "GitHub" to listOf("mcp/github.mcp.json"),
        "Postgres" to listOf("mcp/postgres.mcp.json"),
        "Snowflake" to listOf("mcp/snowflake.mcp.json"),
        "BigQuery" to listOf("mcp/bigquery.mcp.json"),
        "Databricks" to listOf("mcp/databricks.mcp.json"),
        "dbt Cloud" to listOf("mcp/dbt-cloud.mcp.json"),
        "Airflow" to listOf("mcp/airflow.mcp.json"),
        "Kafka" to listOf("mcp/kafka.mcp.json"),
        "Terraform" to listOf("mcp/terraform.mcp.json"),
        "Slack and Jira" to listOf("mcp/slack-jira-incidents.mcp.json")
    )

    val runnableExamples = linkedMapOf(
        "AWS S3 Glue Athena Iceberg" to listOf(
            "examples/aws-s3-glue-athena-iceberg/README.md",
            "examples/aws-s3-glue-athena-iceberg/spec.md",
            "examples/aws-s3-glue-athena-iceberg/plan.md",
            "examples/aws-s3-glue-athena-iceberg/tasks.md",
            "examples/aws-s3-glue-athena-iceberg/Makefile",
            "examples/aws-s3-glue-athena-iceberg/config/lake-layout.yaml",
            "examples/aws-s3-glue-athena-iceberg/jobs/normalize_customers.py",
            "examples/aws-s3-glue-athena-iceberg/sql/create_publish_view.sql",
            "examples/aws-s3-glue-athena-iceberg/data/customers.jsonl"
        ),
        "Databricks Delta Medallion" to listOf(
            "examples/databricks-delta-medallion/README.md",
            "examples/databricks-delta-medallion/spec.md",
            "examples/databricks-delta-medallion/plan.md",
            "examples/databricks-delta-medallion/tasks.md",
            "examples/databricks-delta-medallion/databricks.yml",
            "examples/databricks-delta-medallion/conf/medallion.yaml",
            "examples/databricks-delta-medallion/src/bronze_to_silver.py",
            "examples/databricks-delta-medallion/sample/bronze.jsonl"
        ),
        "dbt Warehouse Marts" to listOf(
            "examples/dbt-warehouse-marts/README.md",
            "examples/dbt-warehouse-marts/spec.md",
            "examples/dbt-warehouse-marts/plan.md",
            "examples/dbt-warehouse-marts/tasks.md",
            "examples/dbt-warehouse-marts/dbt_project.yml",
            "examples/dbt-warehouse-marts/models/staging/stg_orders.sql",
            "examples/dbt-warehouse-marts/models/marts/fct_daily_revenue.sql",
            "examples/dbt-warehouse-marts/models/schema.yml",
            "examples/dbt-warehouse-marts/seeds/orders.csv"
        ),
        "Kafka Flink Streaming" to listOf(
            "examples/kafka-flink-streaming/README.md",
            "examples/kafka-flink-streaming/spec.md",
            "examples/kafka-flink-streaming/plan.md",
            "examples/kafka-flink-streaming/tasks.md",
            "examples/kafka-flink-streaming/docker-compose.yml",
            "examples/kafka-flink-streaming/config/flink-job.yaml",
            "examples/kafka-flink-streaming/schemas/order-events.avsc",
            "examples/kafka-flink-streaming/src/stream_job.py",
            "examples/kafka-flink-streaming/sample/order-events.jsonl"
        )
    )
}
