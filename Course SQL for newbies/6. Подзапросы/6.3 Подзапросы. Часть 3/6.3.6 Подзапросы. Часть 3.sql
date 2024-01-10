SELECT name,
       surname,
       (SELECT COUNT(*)
        FROM Purchases
        WHERE Users.id = user_id) AS num_of_films
FROM Users
ORDER BY num_of_films DESC, name