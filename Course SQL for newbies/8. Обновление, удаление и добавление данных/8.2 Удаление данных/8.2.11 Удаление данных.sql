DELETE
FROM Users
    USING Users
              LEFT JOIN Purchases ON Users.id = Purchases.user_id
WHERE Purchases.id IS NULL;