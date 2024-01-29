SELECT Products.name                                         AS product,
       CONCAT(Products.price * COUNT(Sales.product_id), '€') AS amount
FROM Products
         LEFT JOIN Sales ON Products.id = Sales.product_id
GROUP BY Products.name, Products.price;