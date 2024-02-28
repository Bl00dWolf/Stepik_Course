DELETE
FROM Purchases
    USING Purchases
              INNER JOIN Films ON Purchases.film_id = Films.id
WHERE Films.title LIKE 'Toy Story%';

DELETE
FROM Films
WHERE title LIKE 'Toy Story%';