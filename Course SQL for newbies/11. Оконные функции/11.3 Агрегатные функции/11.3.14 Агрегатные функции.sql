SELECT title,
       rating,
       CONCAT(ROUND((rating - MIN(rating) OVER ()) / MIN(rating) OVER () * 100), '%') as better_than_low_rated_film
FROM Films
ORDER BY ROUND((rating - MIN(rating) OVER ()) / MIN(rating) OVER () * 100) DESC;