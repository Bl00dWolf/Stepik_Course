SELECT Sales.buyer_id
FROM Sales
         INNER JOIN Products ON Sales.product_id = Products.id
WHERE Products.name = 'Canon EOS R6 Camera'
  AND Sales.buyer_id NOT IN (SELECT Sales.buyer_id
                             FROM Sales
                                      INNER JOIN Products ON Sales.product_id = Products.id
                             WHERE Products.name = 'Lenovo ThinkPad X1 Carbon'
                             GROUP BY Sales.buyer_id)
GROUP BY Sales.buyer_id;