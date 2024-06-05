WITH ntile_quartal AS (SELECT *,
                              NTILE(4) over (ORDER BY month) as quarter
                       FROM Sales)

SELECT DISTINCT quarter,
                FIRST_VALUE(month) over (PARTITION BY quarter ORDER BY quantity)    as lowest_sales_month,
                FIRST_VALUE(quantity) over (PARTITION BY quarter ORDER BY quantity) as lowest_sales_quantity
FROM ntile_quartal;