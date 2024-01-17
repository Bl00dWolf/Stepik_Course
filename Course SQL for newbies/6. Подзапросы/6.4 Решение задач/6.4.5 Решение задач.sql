SELECT id
FROM Orders
GROUP BY id
HAVING SUM(product_id) > SUM(quantity) / SUM(DISTINCT product_id)