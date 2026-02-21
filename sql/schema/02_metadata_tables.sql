CREATE TABLE meta.ingestion_config (
    config_id INT IDENTITY(1,1) PRIMARY KEY,
    source_system NVARCHAR(100) NOT NULL,
    source_schema NVARCHAR(128) NOT NULL,
    source_table NVARCHAR(128) NOT NULL,
    target_domain NVARCHAR(128) NOT NULL,
    load_type NVARCHAR(50) NOT NULL, -- historical, one_time, initial, daily, selective
    watermark_column NVARCHAR(128) NULL,
    watermark_value NVARCHAR(100) NULL,
    primary_keys NVARCHAR(1000) NOT NULL,
    is_active BIT NOT NULL DEFAULT 1,
    batch_size INT NOT NULL DEFAULT 50000,
    created_at DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    updated_at DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE audit.pipeline_runs (
    run_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    pipeline_name NVARCHAR(256) NOT NULL,
    load_type NVARCHAR(50) NOT NULL,
    start_time DATETIME2 NOT NULL,
    end_time DATETIME2 NULL,
    status NVARCHAR(30) NOT NULL,
    records_read BIGINT NULL,
    records_written BIGINT NULL,
    error_message NVARCHAR(MAX) NULL
);
