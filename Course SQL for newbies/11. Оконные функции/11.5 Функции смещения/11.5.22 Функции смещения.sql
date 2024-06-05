WITH presales AS (SELECT *,
                         quantity - (LAG(quantity, 1, 1) over (ORDER BY month)) as quant_vs_pre_month
                  FROM Sales)

SELECT month, quantity
FROM presales
WHERE quant_vs_pre_month > 0;