SELECT name, surname
FROM Users
WHERE id = (SELECT user_id
            FROM Purchases
            WHERE film_id = (SELECT id
                             FROM Films
                             WHERE title = 'Toy Story 2')
                             AND user_id = Users.id)
ORDER BY name

# еще вариант
# SELECT name, surname
# FROM Users
# WHERE id IN (SELECT user_id
#              FROM Purchases
#              WHERE film_id = (SELECT id
#                               FROM Films
#                               WHERE title = 'Toy Story 2'))
# ORDER BY name