SELECT *,
       AVG(amount) OVER (ORDER BY date) AS avg_amount
FROM Orders;