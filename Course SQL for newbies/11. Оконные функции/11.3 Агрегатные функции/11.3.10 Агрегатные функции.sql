SELECT title,
       director,
       rating,
       AVG(rating) OVER (PARTITION BY director) as avg_rating_by_director
FROM Films
ORDER BY director, rating;