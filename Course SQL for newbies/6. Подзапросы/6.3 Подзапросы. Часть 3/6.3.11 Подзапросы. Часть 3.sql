SELECT name,
       surname,
       (SELECT title
        FROM Films
        WHERE id IN (SELECT film_id
                     FROM Purchases
                     WHERE user_id = Users.id)
        ORDER BY price DESC, title
        LIMIT 1) AS most_expensive_film
FROM Users
WHERE id IN (SELECT user_id FROM Purchases)
ORDER BY (SELECT price
          FROM Films
          WHERE id IN (SELECT film_id
                       FROM Purchases
                       WHERE user_id = Users.id)
          ORDER BY price DESC
          LIMIT 1) DESC, most_expensive_film, name