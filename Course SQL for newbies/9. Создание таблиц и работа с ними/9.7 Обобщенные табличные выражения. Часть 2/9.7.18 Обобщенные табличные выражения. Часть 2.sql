WITH RECURSIVE orderss AS (SELECT order_date
                           FROM Orders
                           UNION
                           SELECT order_date + INTERVAL 1 DAY
                           FROM orderss
                           WHERE order_date < (SELECT MAX(order_date) FROM Orders))

SELECT orderss.order_date, COUNT(Orders.store) AS orders_count
FROM orderss
         LEFT JOIN Orders on orderss.order_date = Orders.order_date
GROUP BY orderss.order_date
ORDER BY order_date;