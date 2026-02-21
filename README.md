# Azure Data Engineering Utilities

This repository now includes lightweight **project utilities** and reusable **templates (`temps/`)** to speed up common setup tasks.

## What's included

- `project_utils/`: reusable Python helper functions for:
  - directory bootstrapping
  - normalized resource naming
  - simple token-based template rendering
- `temps/`: starter template files for common data engineering project configuration.
- `tests/`: unit tests for core utility behavior.

## Quick start

```bash
python -m unittest discover -s tests -v
```

## Example usage

```python
from pathlib import Path
from project_utils import ensure_project_dirs, make_resource_name, render_template_file

base = Path("demo_project")
ensure_project_dirs(base, ["src", "configs", "pipelines"])

name = make_resource_name("sales", "daily ingest", max_length=24)
print(name)  # sales-daily-ingest

result = render_template_file(
    template_path=Path("temps/pipeline_config.template.json"),
    output_path=base / "configs" / "pipeline_config.json",
    context={"PROJECT": "sales", "ENV": "dev", "OWNER": "data-team"},
)
print(result)
```
# Oracle to Power BI: Enterprise-Grade Azure Data Platform

This repository provides a **production-ready, product-company style blueprint** for migrating Oracle data to a governed, observable Power BI semantic layer using:

- **Oracle** (source)
- **Azure Data Factory (ADF)** for orchestration and ingestion
- **ADLS Gen2 + Blob** for landing/raw/curated storage
- **Azure Databricks (Delta Lake)** for transformation and data quality
- **Azure SQL** for serving marts and operational reporting contracts
- **Power BI** for dashboards and semantic models
- **Azure DevOps** for CI/CD and GitOps
- **Purview + Azure Monitor + Log Analytics** for governance and observability

---

## 1) Reference Architecture (Medallion + Lakehouse + Serving)

1. **Ingestion Layer (ADF + Self-hosted IR)**
   - Oracle incremental extraction with watermark or CDC where available.
   - Land files in `adls://raw/{system}/{schema}/{table}/ingest_date=YYYY-MM-DD/`.
   - Metadata-driven pipeline executes one-time, initial, daily, and selective loads.

2. **Storage Layer (ADLS Gen2 / Blob)**
   - Raw zone: immutable source dumps.
   - Bronze zone: Delta converted canonical raw tables.
   - Silver zone: cleansed conforming entities.
   - Gold zone: dimensional/fact/star or data products.

3. **Processing Layer (Databricks)**
   - Auto Loader / COPY INTO for robust ingestion.
   - Delta MERGE for SCD1/SCD2.
   - Data quality assertions and quarantine.
   - Unity Catalog for governance.

4. **Serving Layer (Azure SQL + Power BI)**
   - Curated marts published to Azure SQL (DirectQuery/Import choices by use-case).
   - Power BI semantic model with RLS and incremental refresh.

5. **Control Plane & Ops**
   - Azure DevOps multi-stage pipelines deploy infra and data code.
   - Monitoring dashboards for SLA/SLO, freshness, quality, and cost.

---

## 2) Load Frameworks Included

- **Historical Load**: full backfill by date-partition or key-range chunking.
- **One-Time Load**: ad hoc migration job for specific data assets.
- **Initial Load**: first complete baseline before incremental begins.
- **Daily Incremental**: watermark/CDC-based ingestion and MERGE.
- **Selective Load**: targeted table/domain execution with dynamic parameters.

All patterns are implemented as metadata-driven controls in `sql/schema/02_metadata_tables.sql` and orchestrated by ADF parameters.

---

## 3) Folder Map

- `docs/` — architecture and learning playbooks.
- `architecture/databricks/` — notebooks/jobs/config for medallion transformations.
- `adf/` — linked services, datasets, pipelines, triggers (template-ready JSON).
- `sql/` — schema, ETL proc/staging scripts, quality checks, security.
- `infra/` — IaC templates (Bicep + Terraform examples).
- `devops/` — Azure DevOps CI/CD YAML and deployment templates.
- `governance/` — Purview glossary, monitoring workbook query samples, runbooks.

---

## 4) Production Readiness Checklist

- [x] Environment separation: dev/test/prod with isolated key vaults and workspaces.
- [x] Secrets managed via Key Vault references only.
- [x] Idempotent pipelines and replay strategy.
- [x] Data quality checks with fail-fast + quarantine.
- [x] End-to-end lineage and ownership catalog.
- [x] SLA/SLO dashboards and on-call runbook.
- [x] Cost guardrails (cluster policies, auto-termination, data retention).
- [x] RBAC + least privilege + PII masking.

---

## 5) How to Start

1. Deploy infra using `infra/bicep/main.bicep` or `infra/terraform/main.tf`.
2. Create metadata and serving objects by running SQL scripts in order under `sql/schema`.
3. Publish ADF artifacts from `adf/`.
4. Import Databricks jobs/notebooks from `architecture/databricks/`.
5. Configure Azure DevOps pipelines from `devops/pipelines`.
6. Apply governance assets from `governance/`.

---

## 6) Learn to Become a Strong Data Engineer

Read `docs/learning-path.md` for a 24-week mastery roadmap including:
- SQL excellence, distributed processing fundamentals
- Data modeling, orchestration, quality engineering
- Platform reliability, FinOps, governance
- Project communication and product-thinking

