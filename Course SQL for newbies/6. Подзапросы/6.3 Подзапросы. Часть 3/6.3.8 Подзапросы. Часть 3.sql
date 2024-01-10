SELECT name,
       surname
FROM Users
ORDER BY (SELECT COUNT(*)
          FROM Purchases
          WHERE Users.id = user_id) DESC
LIMIT 1