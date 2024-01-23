SELECT Categories.name AS category
FROM Categories
         INNER JOIN Products ON Categories.id = Products.category_id
         INNER JOIN Sales ON Products.id = Sales.product_id
GROUP BY Categories.name
ORDER BY SUM(price) DESC
LIMIT 1