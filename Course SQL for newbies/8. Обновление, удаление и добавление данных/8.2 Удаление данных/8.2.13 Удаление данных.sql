DELETE
FROM Purchases
    USING Purchases
              INNER JOIN Users ON Purchases.user_id = Users.id
WHERE Users.user = 'Matt Damon';

DELETE
FROM Users
WHERE user = 'Matt Damon';