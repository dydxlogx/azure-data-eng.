CREATE TABLE IF NOT EXISTS audit.dq_results (
    check_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    check_name NVARCHAR(200),
    severity NVARCHAR(20),
    table_name NVARCHAR(200),
    failed_count BIGINT,
    check_time DATETIME2 DEFAULT SYSDATETIME()
);

-- Example checks
INSERT INTO audit.dq_results (check_name, severity, table_name, failed_count)
SELECT 'NULL_ORDER_ID', 'HIGH', 'dwh.sales_fact', COUNT(*)
FROM dwh.sales_fact
WHERE order_id IS NULL;
