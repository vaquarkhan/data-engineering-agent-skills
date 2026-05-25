---
name: azure-data-engineering
description: Adapts the core skills for Azure-native data engineering teams. Use when the platform is primarily built on Azure services for storage, pipelines, analytics, governance, and enterprise integration.
---

# Azure Data Engineering

## Overview

Use this preset when the platform is centered on Azure services. It maps core workflows to `ADLS Gen2`, `Data Factory`, `Synapse`, `Event Hubs`, `Azure Databricks`, `Purview`, `Key Vault`, and Azure monitoring services.

## Use When

- storage and governance are anchored in `Azure`
- pipelines are managed with `Data Factory`, `Synapse`, or platform-native schedulers
- the environment is integrated with `Microsoft Entra ID`, `Purview`, and enterprise Azure networking

## Preferred Platform Services

- storage: `ADLS Gen2`
- orchestration: `Azure Data Factory`, `Synapse Pipelines`
- batch and lakehouse compute: `Azure Databricks`, `Synapse Spark`
- warehouse and serving: `Synapse Dedicated SQL`, `Azure SQL`, `Fabric` where applicable
- streaming: `Event Hubs`, `Stream Analytics`
- governance: `Microsoft Purview`
- secrets and security: `Key Vault`, `Managed Identity`, `Entra ID`
- monitoring: `Azure Monitor`, `Log Analytics`

## Design Rules

- Keep raw, curated, and publish zones explicit in `ADLS Gen2`.
- Use `Managed Identity` and `Key Vault` instead of embedding credentials in jobs.
- Make governance and classification visible through `Purview` for shared datasets.
- Be clear about whether `Synapse`, `Azure Databricks`, or `Fabric` is the primary execution surface.
- Design for enterprise network, private endpoint, and identity constraints early.

## Verification

- [ ] Storage zones and publish boundaries are defined in `ADLS Gen2`
- [ ] Identity, secrets, and access controls map to Azure-native controls
- [ ] The execution engine choice is explicit and justified
- [ ] Monitoring, lineage, and governance are accounted for with Azure services
