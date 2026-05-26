const vscode = require("vscode");
const fs = require("fs");
const path = require("path");
const https = require("https");

const CORE_FILES = [
  "AGENTS.md",
  "CLAUDE.md",
  "skills-index.md",
  "registry/assets.json",
  "templates/source-contract.yaml",
  "templates/dataset-contract.yaml",
  "templates/metric-contract.yaml",
  "templates/data-compliance-controls.yaml",
  "templates/backfill-plan.yaml",
  "templates/schema-change-plan.yaml",
  "templates/release-gate-evidence.yaml",
  "templates/incident-runbook.md",
  "requirements-proof.txt",
  "docs/getting-started.md",
  "docs/codex-setup.md",
  "scripts/validate_dataset_contract.py",
  "hooks/README.md",
  "hooks/hooks.json",
  "hooks/session-start.sh",
  "hooks/contract-check-pre.sh",
  "hooks/pipeline-review-pre.sh",
  "hooks/incident-mode.sh",
  "hooks/backfill-guard.sh",
  "hooks/schema-change-guard.sh",
  "hooks/cost-check.sh",
  "hooks/release-guard.sh"
];

const AGENT_ADAPTERS = {
  Cursor: [
    ".cursor/rules/00-data-agent-core.mdc",
    ".cursor/rules/10-spec-first.mdc",
    ".cursor/rules/20-platform-preset-selector.mdc",
    ".cursor/rules/30-quality-gates.mdc"
  ],
  Claude: [
    ".claude/commands/spec.md",
    ".claude/commands/plan.md",
    ".claude/commands/build.md",
    ".claude/commands/test.md",
    ".claude/commands/validate.md",
    ".claude/commands/backfill.md",
    ".claude/commands/review.md",
    ".claude/commands/ship.md",
    "AGENTS.md",
    "CLAUDE.md"
  ],
  Copilot: [
    ".github/copilot-instructions.md",
    "AGENTS.md"
  ],
  Gemini: [
    ".gemini/commands/spec.md",
    ".gemini/commands/plan.md",
    ".gemini/commands/build.md",
    ".gemini/commands/test.md",
    ".gemini/commands/validate.md",
    ".gemini/commands/backfill.md",
    ".gemini/commands/review.md",
    ".gemini/commands/ship.md"
  ],
  Kiro: [
    ".kiro/steering/product.md",
    ".kiro/steering/tech.md",
    ".kiro/steering/structure.md",
    "docs/kiro-setup.md",
    "AGENTS.md",
    "CLAUDE.md"
  ],
  Codex: [
    "AGENTS.md",
    "CLAUDE.md",
    "skills-index.md",
    "docs/getting-started.md",
    "docs/codex-setup.md"
  ],
  OpenCode: [
    "AGENTS.md",
    "CLAUDE.md",
    ".opencode/README.md",
    ".opencode/skills",
    "docs/opencode-setup.md",
    "docs/getting-started.md"
  ],
  Windsurf: [
    ".windsurfrules.example",
    "docs/windsurf-setup.md",
    "docs/getting-started.md"
  ]
};

const STARTER_PACKS = {
  "AWS Lakehouse": {
    files: [
      "starter-packs/aws-lakehouse-starter.yaml",
      "templates/source-contract.yaml",
      "templates/dataset-contract.yaml",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Databricks Medallion": {
    files: [
      "starter-packs/databricks-medallion-starter.yaml",
      "templates/source-contract.yaml",
      "templates/dataset-contract.yaml",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Warehouse Analytics": {
    files: [
      "starter-packs/warehouse-analytics-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/metric-contract.yaml",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Streaming Reliability": {
    files: [
      "starter-packs/streaming-reliability-starter.yaml",
      "templates/source-contract.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Privacy Governance": {
    files: [
      "starter-packs/privacy-governance-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Regulated Data Compliance": {
    files: [
      "starter-packs/regulated-data-compliance-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/data-compliance-controls.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Data Platform CI CD Release": {
    files: [
      "starter-packs/data-platform-cicd-release-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Resiliency Testing": {
    files: [
      "starter-packs/resiliency-testing-starter.yaml",
      "templates/incident-runbook.md",
      "templates/backfill-plan.yaml",
      "templates/release-gate-evidence.yaml",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Validation Security Review": {
    files: [
      "starter-packs/validation-security-review-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/data-compliance-controls.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Regional Compliance ESG Reporting": {
    files: [
      "starter-packs/regional-compliance-and-esg-reporting-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/data-compliance-controls.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Test Data Lower Environments": {
    files: [
      "starter-packs/test-data-lower-environments-starter.yaml",
      "templates/dataset-contract.yaml",
      "templates/data-compliance-controls.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  },
  "Enterprise ETL Modernization": {
    files: [
      "starter-packs/enterprise-etl-modernization-starter.yaml",
      "templates/source-contract.yaml",
      "templates/dataset-contract.yaml",
      "templates/incident-runbook.md",
      "AGENTS.md",
      "skills-index.md"
    ]
  }
};

const MCP_TEMPLATES = {
  GitHub: ["mcp/github.mcp.json"],
  Postgres: ["mcp/postgres.mcp.json"],
  Snowflake: ["mcp/snowflake.mcp.json"],
  BigQuery: ["mcp/bigquery.mcp.json"],
  Databricks: ["mcp/databricks.mcp.json"],
  "dbt Cloud": ["mcp/dbt-cloud.mcp.json"],
  Airflow: ["mcp/airflow.mcp.json"],
  Kafka: ["mcp/kafka.mcp.json"],
  Terraform: ["mcp/terraform.mcp.json"],
  "Slack and Jira": ["mcp/slack-jira-incidents.mcp.json"]
};

const RUNNABLE_EXAMPLES = {
  "AWS S3 Glue Athena Iceberg": [
    "examples/aws-s3-glue-athena-iceberg/README.md",
    "examples/aws-s3-glue-athena-iceberg/spec.md",
    "examples/aws-s3-glue-athena-iceberg/plan.md",
    "examples/aws-s3-glue-athena-iceberg/tasks.md",
    "examples/aws-s3-glue-athena-iceberg/Makefile",
    "examples/aws-s3-glue-athena-iceberg/contracts/customers-contract.yaml",
    "examples/aws-s3-glue-athena-iceberg/config/lake-layout.yaml",
    "examples/aws-s3-glue-athena-iceberg/jobs/normalize_customers.py",
    "examples/aws-s3-glue-athena-iceberg/jobs/reconcile_customers.py",
    "examples/aws-s3-glue-athena-iceberg/sql/create_publish_view.sql",
    "examples/aws-s3-glue-athena-iceberg/data/customers.jsonl",
    "scripts/validate_dataset_contract.py",
    "requirements-proof.txt"
  ],
  "Databricks Delta Medallion": [
    "examples/databricks-delta-medallion/README.md",
    "examples/databricks-delta-medallion/spec.md",
    "examples/databricks-delta-medallion/plan.md",
    "examples/databricks-delta-medallion/tasks.md",
    "examples/databricks-delta-medallion/databricks.yml",
    "examples/databricks-delta-medallion/conf/medallion.yaml",
    "examples/databricks-delta-medallion/src/bronze_to_silver.py",
    "examples/databricks-delta-medallion/sample/bronze.jsonl"
  ],
  "dbt Warehouse Marts": [
    "examples/dbt-warehouse-marts/README.md",
    "examples/dbt-warehouse-marts/spec.md",
    "examples/dbt-warehouse-marts/plan.md",
    "examples/dbt-warehouse-marts/tasks.md",
    "examples/dbt-warehouse-marts/Makefile",
    "examples/dbt-warehouse-marts/contracts/fct_daily_revenue-contract.yaml",
    "examples/dbt-warehouse-marts/dbt_project.yml",
    "examples/dbt-warehouse-marts/profiles/profiles.yml",
    "examples/dbt-warehouse-marts/models/staging/stg_orders.sql",
    "examples/dbt-warehouse-marts/models/marts/fct_daily_revenue.sql",
    "examples/dbt-warehouse-marts/models/schema.yml",
    "examples/dbt-warehouse-marts/seeds/orders.csv",
    "scripts/validate_dataset_contract.py",
    "requirements-proof.txt"
  ],
  "Kafka Flink Streaming": [
    "examples/kafka-flink-streaming/README.md",
    "examples/kafka-flink-streaming/spec.md",
    "examples/kafka-flink-streaming/plan.md",
    "examples/kafka-flink-streaming/tasks.md",
    "examples/kafka-flink-streaming/Makefile",
    "examples/kafka-flink-streaming/docker-compose.yml",
    "examples/kafka-flink-streaming/config/flink-job.yaml",
    "examples/kafka-flink-streaming/contracts/windowed-orders-contract.yaml",
    "examples/kafka-flink-streaming/schemas/order-events.avsc",
    "examples/kafka-flink-streaming/src/producer.py",
    "examples/kafka-flink-streaming/src/replay.py",
    "examples/kafka-flink-streaming/src/stream_job.py",
    "examples/kafka-flink-streaming/src/validate_sink.py",
    "examples/kafka-flink-streaming/sample/order-events.jsonl",
    "scripts/validate_dataset_contract.py",
    "requirements-proof.txt"
  ]
};

function activate(context) {
  context.subscriptions.push(
    vscode.commands.registerCommand("dataEngineeringSkills.installFullToolkit", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      const files = [
        ...CORE_FILES,
        ...Object.values(AGENT_ADAPTERS).flat(),
        ...Object.values(STARTER_PACKS).flatMap((item) => item.files),
        ...Object.values(MCP_TEMPLATES).flat(),
        "mcp/README.md"
      ];
      await installFiles(context, root, dedupe(files), "full toolkit");
    }),
    vscode.commands.registerCommand("dataEngineeringSkills.installCorePack", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      await installFiles(context, root, CORE_FILES, "core pack");
    }),
    vscode.commands.registerCommand("dataEngineeringSkills.installAgentAdapters", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      const choices = [...Object.keys(AGENT_ADAPTERS), "All"];
      const picked = await vscode.window.showQuickPick(choices, {
        placeHolder: "Choose which agent adapters to install"
      });
      if (!picked) {
        return;
      }
      const files = picked === "All"
        ? dedupe(Object.values(AGENT_ADAPTERS).flat())
        : AGENT_ADAPTERS[picked];
      await installFiles(context, root, files, `${picked} adapters`);
    }),
    vscode.commands.registerCommand("dataEngineeringSkills.installStarterPack", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      const picked = await vscode.window.showQuickPick(Object.keys(STARTER_PACKS), {
        placeHolder: "Choose a starter pack"
      });
      if (!picked) {
        return;
      }
      await installFiles(context, root, STARTER_PACKS[picked].files, `${picked} starter pack`);
    }),
    vscode.commands.registerCommand("dataEngineeringSkills.installMcpTemplates", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      const choices = [...Object.keys(MCP_TEMPLATES), "All"];
      const picked = await vscode.window.showQuickPick(choices, {
        placeHolder: "Choose MCP templates to install"
      });
      if (!picked) {
        return;
      }
      const files = picked === "All"
        ? dedupe(["mcp/README.md", ...Object.values(MCP_TEMPLATES).flat()])
        : ["mcp/README.md", ...MCP_TEMPLATES[picked]];
      await installFiles(context, root, files, `${picked} MCP templates`);
    }),
    vscode.commands.registerCommand("dataEngineeringSkills.scaffoldRunnableExample", async () => {
      const root = getWorkspaceRoot();
      if (!root) {
        return;
      }
      const picked = await vscode.window.showQuickPick(Object.keys(RUNNABLE_EXAMPLES), {
        placeHolder: "Choose a runnable example to scaffold"
      });
      if (!picked) {
        return;
      }
      await installFiles(context, root, RUNNABLE_EXAMPLES[picked], `${picked} example`);
    })
  );
}

function deactivate() {}

function getWorkspaceRoot() {
  const folders = vscode.workspace.workspaceFolders;
  if (!folders || folders.length === 0) {
    vscode.window.showErrorMessage("Open a workspace folder before installing the skill pack.");
    return null;
  }
  return folders[0].uri.fsPath;
}

async function installFiles(context, workspaceRoot, relativePaths, label) {
  const collisions = [];
  for (const relativePath of relativePaths) {
    const targetPath = path.join(workspaceRoot, relativePath);
    if (fs.existsSync(targetPath)) {
      collisions.push(relativePath);
    }
  }

  let overwrite = false;
  if (collisions.length > 0) {
    const choice = await vscode.window.showWarningMessage(
      `${collisions.length} file(s) already exist for ${label}. Overwrite them?`,
      { modal: true },
      "Overwrite",
      "Skip Existing",
      "Cancel"
    );
    if (choice === "Cancel" || !choice) {
      return;
    }
    overwrite = choice === "Overwrite";
  }

  const installed = [];
  const skipped = [];

  await vscode.window.withProgress(
    {
      location: vscode.ProgressLocation.Notification,
      title: `Installing ${label}`,
      cancellable: false
    },
    async (progress) => {
      let completed = 0;
      for (const relativePath of relativePaths) {
        const targetPath = path.join(workspaceRoot, relativePath);
        completed += 1;
        progress.report({
          message: relativePath,
          increment: 100 / relativePaths.length
        });

        if (fs.existsSync(targetPath) && !overwrite) {
          skipped.push(relativePath);
          continue;
        }

        const content = await loadAsset(context, relativePath);
        await fs.promises.mkdir(path.dirname(targetPath), { recursive: true });
        await fs.promises.writeFile(targetPath, content, "utf8");
        installed.push(relativePath);
      }
    }
  );

  const parts = [`Installed ${installed.length} file(s) for ${label}.`];
  if (skipped.length > 0) {
    parts.push(`Skipped ${skipped.length} existing file(s).`);
  }
  vscode.window.showInformationMessage(parts.join(" "));
}

async function loadAsset(context, relativePath) {
  const localCandidates = [
    path.resolve(context.extensionPath, "..", relativePath),
    path.join(context.extensionPath, "resources", relativePath)
  ];

  for (const candidate of localCandidates) {
    if (fs.existsSync(candidate)) {
      return fs.promises.readFile(candidate, "utf8");
    }
  }

  const config = vscode.workspace.getConfiguration("dataEngineeringSkills");
  const rawBaseUrl = config.get(
    "rawBaseUrl",
    "https://raw.githubusercontent.com/vaquarkhan/data-engineering-agent-skills/main"
  );
  const url = `${String(rawBaseUrl).replace(/\/$/, "")}/${relativePath.replace(/\\/g, "/")}`;
  return downloadText(url);
}

function downloadText(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, (response) => {
        if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
          resolve(downloadText(response.headers.location));
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Failed to download ${url}: ${response.statusCode}`));
          return;
        }

        const chunks = [];
        response.on("data", (chunk) => chunks.push(chunk));
        response.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
      })
      .on("error", reject);
  });
}

function dedupe(items) {
  return [...new Set(items)];
}

module.exports = {
  activate,
  deactivate
};
