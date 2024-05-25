WITH sales_by_quartal AS (SELECT *, NTILE(4) over () AS quartal
                          FROM Sales)

SELECT month,
       quantity,
       SUM(quantity)
           OVER (PARTITION BY quartal ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_quantity_within_quarter
FROM sales_by_quartal;