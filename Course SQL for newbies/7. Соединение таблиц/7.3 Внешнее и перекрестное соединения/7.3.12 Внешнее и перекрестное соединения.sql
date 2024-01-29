SELECT Products.name as product, IFNULL(MIN(Sales.sale_date), 'Not sold') as first_sale
FROM Products
         LEFT JOIN Sales ON Products.id = Sales.product_id
GROUP BY Products.name;