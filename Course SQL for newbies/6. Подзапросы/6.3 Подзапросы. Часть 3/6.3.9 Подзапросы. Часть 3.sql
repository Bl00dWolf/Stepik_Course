SELECT name,
       surname,
       (SELECT title
        FROM Films
        WHERE (SELECT film_id
               FROM Purchases
               WHERE user_id = Users.id
               ORDER BY id
               LIMIT 1) = Films.id) AS first_film
FROM Users
WHERE (SELECT title
       FROM Films
       WHERE (SELECT film_id
              FROM Purchases
              WHERE user_id = Users.id
              ORDER BY id
              LIMIT 1) = Films.id) IS NOT NULL
ORDER BY name

# Еще вариант
# SELECT name,
#        surname,
#        (SELECT title
#         FROM Films
#         WHERE (SELECT film_id
#                FROM Purchases
#                WHERE user_id = Users.id
#                ORDER BY id
#                LIMIT 1) = Films.id) AS first_film
# FROM Users
# HAVING ISNULL(first_film) = 0
# ORDER BY name

# Еще вариант
# SELECT name, surname,
#        (SELECT title
#         FROM Films
#         WHERE id = (SELECT film_id
#                     FROM Purchases
#                     WHERE user_id = Users.id
#                     ORDER BY id
#                     LIMIT 1)) AS first_film
# FROM Users
# WHERE id IN (SELECT user_id
#              FROM Purchases)
# ORDER BY name