SELECT MONTHNAME(order_date)       as month,
       COUNT(*)                    AS order_count,
       COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY month;
