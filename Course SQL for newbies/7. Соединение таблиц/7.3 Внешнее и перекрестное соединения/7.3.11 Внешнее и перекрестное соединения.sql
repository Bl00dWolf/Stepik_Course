SELECT Products.name as product
FROM Products
         LEFT JOIN Sales ON Products.id = Sales.product_id
WHERE Sales.id IS NULL;