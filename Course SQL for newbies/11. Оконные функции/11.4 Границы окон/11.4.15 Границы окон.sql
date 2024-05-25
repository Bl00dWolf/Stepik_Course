SELECT month,
       quantity,
       COALESCE(SUM(quantity) OVER (ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING), 0) AS prev_month_quantity
FROM Sales;