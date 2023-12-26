SELECT COUNT(*) AS num_of_users
FROM Users
WHERE id = (SELECT user_id
            FROM Purchases
            WHERE film_id = (SELECT id
                             FROM Films
                             WHERE title = 'Toy Story 2')
              AND Users.id = user_id)

# еще вариант
# SELECT COUNT(*) AS num_of_users
# FROM Purchases
# WHERE film_id = (SELECT id
#                  FROM Films
#                  WHERE title = 'Toy Story 2')