SELECT *,
       SUM(quantity) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_quantity
FROM Sales;