CREATE SCHEMA security;
GO

CREATE FUNCTION security.fn_sales_region_access(@region NVARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS fn_access
WHERE @region = CAST(SESSION_CONTEXT(N'region') AS NVARCHAR(50));
GO

CREATE SECURITY POLICY security.sales_region_policy
ADD FILTER PREDICATE security.fn_sales_region_access(region)
ON dwh.sales_fact
WITH (STATE = ON);
GO
