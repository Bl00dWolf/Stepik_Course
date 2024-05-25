WITH all_months AS (SELECT *,
                           AVG(quantity) OVER (ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING) AS two_prev_months_avg_quantity
                    FROM Sales)

SELECT *
FROM all_months
WHERE month >= 3;