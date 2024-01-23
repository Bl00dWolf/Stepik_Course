SELECT DISTINCT name AS product
FROM Products
         INNER JOIN Sales ON Sales.product_id = Products.id;