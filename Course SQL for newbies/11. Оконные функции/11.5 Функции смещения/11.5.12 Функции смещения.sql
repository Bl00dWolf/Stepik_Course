WITH ord AS (SELECT DISTINCT date,
                             ABS((NTH_VALUE(amount, 1) over (PARTITION BY date ORDER BY date)) -
                                 (NTH_VALUE(amount, 2) over (PARTITION BY date ORDER BY date))) as two_first_orders_amount_diff
             FROM Orders)

SELECT *
FROM ord
WHERE two_first_orders_amount_diff IS NOT NULL;