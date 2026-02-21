-- Databricks SQL notebook
CREATE TABLE IF NOT EXISTS gold.sales_fact AS
SELECT
  order_id,
  customer_id,
  product_id,
  order_date,
  amount,
  _ingestion_ts
FROM silver.orders;

CREATE OR REPLACE VIEW gold.vw_daily_sales AS
SELECT order_date, SUM(amount) AS total_sales
FROM gold.sales_fact
GROUP BY order_date;
