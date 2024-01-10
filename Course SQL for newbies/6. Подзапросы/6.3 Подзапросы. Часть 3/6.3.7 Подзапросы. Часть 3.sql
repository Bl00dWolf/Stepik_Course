SELECT name,
       surname
FROM Users
WHERE (SELECT COUNT(*)
       FROM Purchases
       WHERE Users.id = user_id) = 2
ORDER BY name