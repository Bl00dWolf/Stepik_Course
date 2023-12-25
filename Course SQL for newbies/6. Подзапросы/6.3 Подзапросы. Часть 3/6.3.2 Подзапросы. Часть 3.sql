SELECT name, surname
FROM Users
WHERE id NOT IN (SELECT user_id FROM Purchases)