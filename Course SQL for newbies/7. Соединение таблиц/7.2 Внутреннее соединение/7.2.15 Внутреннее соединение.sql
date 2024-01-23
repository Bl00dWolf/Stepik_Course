SELECT name AS product
FROM Products
         INNER JOIN Sales ON Products.id = Sales.product_id AND sale_date = '2023-09-12'
GROUP BY name
HAVING COUNT(*) = 1
ORDER BY product