SELECT country,
       MIN(rating) AS min_rating,
       MAX(rating) AS max_rating
FROM Directors
GROUP BY country
ORDER BY country