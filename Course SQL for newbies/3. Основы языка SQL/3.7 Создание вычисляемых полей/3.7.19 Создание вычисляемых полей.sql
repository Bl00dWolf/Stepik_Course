SELECT title,
       price * purchases as profit
FROM Films
ORDER BY profit DESC
LIMIT 3;