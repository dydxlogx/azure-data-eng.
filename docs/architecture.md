# Detailed Architecture and Pattern Catalog

## A. End-to-End Flow

1. Oracle tables are registered in metadata table `meta.ingestion_config`.
2. ADF `pl_oracle_to_raw_metadata` reads active configs and ForEach executes copy.
3. Raw files arrive in ADLS Gen2 as Parquet/CSV with audit columns.
4. Databricks Bronze ingestion enforces schema and stores Delta.
5. Silver jobs apply business rules, DQ checks, and conformance.
6. Gold jobs build marts and publish to Azure SQL for BI consumption.
7. Power BI refreshes model and publishes enterprise dashboard.

## B. Design Patterns Included

- Batch ingestion with watermark.
- CDC-like emulation via timestamp + hard delete handling flags.
- Multi-tenant/product-domain pattern with config-driven routing.
- Late-arriving dimensions handling.
- SCD Type 1 and Type 2.
- Data quality contract pattern (validations as code).
- Dead-letter/quarantine pattern.
- Backfill replay pattern with versioned code and deterministic reprocessing.

## C. Non-Functional Requirements

- **Availability**: 99.9% pipeline availability target.
- **Freshness**: <= 2h latency for daily jobs.
- **Scalability**: partitioned loads + parallelized table groups.
- **Security**: private endpoints, managed identities, KMS-backed encryption.
- **Compliance**: retention, masking, and lineage controls.

## D. Environment Strategy

- dev: frequent deployment, sample data, lower-cost SKUs.
- test: integration and regression runs.
- prod: locked branch, approvals, strict policies.

## E. Incident Levels

- P1: executive dashboard outage.
- P2: domain pipeline missed SLA.
- P3: non-critical data quality warning.

Map incidents to response in `governance/runbooks/oncall-runbook.md`.
