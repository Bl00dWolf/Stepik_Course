SELECT COUNT(DISTINCT customer_id) AS customers_count
FROM Bills
WHERE amount > 500;