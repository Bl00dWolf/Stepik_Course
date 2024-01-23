SELECT DISTINCT name AS product
FROM Products
         INNER JOIN Sales ON Products.id = Sales.product_id
WHERE sale_date = DATE('2023-09-12')
