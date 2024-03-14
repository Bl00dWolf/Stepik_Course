WITH AvgMax_Custom AS (SELECT customer_id, AVG(amount)
                       FROM Orders
                       GROUP BY customer_id
                       ORDER BY 2 DESC
                       LIMIT 1)

SELECT name AS customer
FROM Customers
WHERE Customers.id = (SELECT customer_id
                      FROM AvgMax_Custom);