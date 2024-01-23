SELECT Sales.id        AS sale_id,
       sale_date,
       Products.name   AS product,
       Categories.name AS category
FROM Products
         INNER JOIN Sales ON Products.id = Sales.product_id
         INNER JOIN Categories ON Products.category_id = Categories.id