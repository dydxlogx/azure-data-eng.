CREATE OR ALTER PROCEDURE dwh.usp_upsert_sales_fact
AS
BEGIN
    SET NOCOUNT ON;

    MERGE dwh.sales_fact AS tgt
    USING (
        SELECT order_id, customer_id, product_id, order_date, amount, load_datetime
        FROM stg.sales_fact_delta
    ) AS src
    ON tgt.order_id = src.order_id
    WHEN MATCHED THEN
        UPDATE SET
            tgt.customer_id = src.customer_id,
            tgt.product_id = src.product_id,
            tgt.order_date = src.order_date,
            tgt.amount = src.amount,
            tgt.updated_at = SYSDATETIME()
    WHEN NOT MATCHED THEN
        INSERT (order_id, customer_id, product_id, order_date, amount, created_at, updated_at)
        VALUES (src.order_id, src.customer_id, src.product_id, src.order_date, src.amount, SYSDATETIME(), SYSDATETIME());
END
GO
