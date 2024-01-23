SELECT name                    AS product,
       CONCAT(SUM(price), '€') AS amount
FROM Products
         INNER JOIN Sales ON Products.id = Sales.product_id
GROUP BY name