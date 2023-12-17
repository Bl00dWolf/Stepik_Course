SELECT country,
       AVG(rating) AS avg_rating
FROM Directors
WHERE rating BETWEEN 11 AND 89
GROUP BY country
ORDER BY avg_rating;