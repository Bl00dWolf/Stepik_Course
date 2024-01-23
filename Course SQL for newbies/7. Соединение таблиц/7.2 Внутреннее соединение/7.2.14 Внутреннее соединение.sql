SELECT name AS bestseller
FROM Products
         INNER JOIN Sales ON Products.id = Sales.product_id
WHERE sale_date = '2023-09-12'
GROUP BY name
ORDER BY COUNT(product_id) DESC
LIMIT 1