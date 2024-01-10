SELECT name,
       surname,
       IFNULL((SELECT SUM(price)
               FROM Films
               WHERE id IN (SELECT film_id
                            FROM Purchases
                            WHERE user_id = Users.id)), 0.00) AS total_spending
FROM Users
ORDER BY total_spending DESC, name;