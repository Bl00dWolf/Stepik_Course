SELECT Products.name             AS product,
       IFNULL(SUM(rest), 0)      AS rest,
       IFNULL(SUM(paid), 0)      AS paid,
       IFNULL(SUM(cancelled), 0) AS cancelled,
       IFNULL(SUM(refunded), 0)  AS refunded
FROM Invoices
         RIGHT JOIN Products ON Invoices.product_id = Products.id
GROUP BY product
ORDER BY product;