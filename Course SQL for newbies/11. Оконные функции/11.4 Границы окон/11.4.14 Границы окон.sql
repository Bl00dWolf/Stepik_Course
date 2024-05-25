SELECT month,
       AVG(quantity) OVER (ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS avg_quantity
FROM Sales;