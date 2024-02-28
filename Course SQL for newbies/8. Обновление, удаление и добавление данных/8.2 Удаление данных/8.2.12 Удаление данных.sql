DELETE
FROM Purchases
WHERE user_id = (SELECT id FROM Users WHERE user = 'Matt Damon')
ORDER BY id DESC
LIMIT 2;