WITH Sales_By_Quartal AS (SELECT *,
                                 NTILE(4) over (ORDER BY month) as quarter
                          FROM Sales),

     prequery AS (SELECT quarter,
                         (ABS((NTH_VALUE(quantity, 1) over sl_qua - NTH_VALUE(quantity, 2) over sl_qua)) +
                          ABS((NTH_VALUE(quantity, 2) over sl_qua - NTH_VALUE(quantity, 3) over sl_qua))) /
                         2 as sales_avg_diff
                  FROM Sales_By_Quartal
                  WINDOW sl_qua AS (PARTITION BY quarter ORDER BY month))

SELECT *
FROM prequery
WHERE sales_avg_diff IS NOT NULL;

#еще вариант
WITH QuarterSales AS (SELECT Sales.*,
                             NTILE(4) OVER (ORDER BY month) AS quarter
                      FROM Sales),
     Difference AS (SELECT quarter,
                           ABS(LAG(quantity) OVER (PARTITION BY quarter ORDER BY month) - quantity) AS difference
                    FROM QuarterSales)
SELECT quarter,
       AVG(difference) AS sales_avg_diff
FROM Difference
GROUP BY quarter;