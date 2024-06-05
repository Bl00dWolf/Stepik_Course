WITH presales AS (SELECT *,
                         ABS(quantity - (LEAD(quantity)
                                              over (ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING))) as next_month_sales_diff
                  FROM Sales)

SELECT *
FROM presales
WHERE month != 12;
