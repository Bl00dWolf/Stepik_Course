SELECT name, surname, COUNT(*) AS num_of_films
FROM Users
WHERE id IN (SELECT user_id, COUNT(*)
             FROM Purchases
             GROUP BY user_id);

SELECT user_id, COUNT(*)
FROM Purchases
GROUP BY user_id;