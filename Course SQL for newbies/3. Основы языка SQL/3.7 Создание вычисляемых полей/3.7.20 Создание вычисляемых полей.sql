SELECT title,
       price * 0.7 AS discount_price
FROM Films
WHERE price * 0.7 < 4
ORDER BY 2;