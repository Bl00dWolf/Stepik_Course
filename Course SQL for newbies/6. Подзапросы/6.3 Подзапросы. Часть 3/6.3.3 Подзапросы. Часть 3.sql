SELECT title, director
FROM Films
WHERE id IN (SELECT film_id FROM Purchases)
ORDER BY title