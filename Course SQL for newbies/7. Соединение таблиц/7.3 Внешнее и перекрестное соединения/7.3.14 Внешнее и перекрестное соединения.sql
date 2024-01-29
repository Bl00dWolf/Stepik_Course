SELECT Categories.name                                    AS category,
       CONCAT(ROUND(IFNULL(AVG(Products.price), 0)), '€') AS avg_amount
FROM Sales
         LEFT JOIN Products ON Sales.product_id = Products.id
         RIGHT JOIN Categories ON Products.category_id = Categories.id
GROUP BY Categories.name;