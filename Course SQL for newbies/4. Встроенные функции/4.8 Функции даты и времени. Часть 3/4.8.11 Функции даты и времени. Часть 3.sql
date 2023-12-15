SELECT customer_name,
       ADDTIME(order_time, spent_on_delivery) AS delivery_datetime
FROM Orders
WHERE DATE(order_time) = DATE('2023-10-24')
ORDER BY delivery_datetime DESC
LIMIT 1;