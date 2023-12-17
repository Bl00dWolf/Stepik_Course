SELECT country,
       AVG(rating) AS avg_rating
FROM Directors
WHERE rating BETWEEN 31 AND 69
GROUP BY country
HAVING avg_rating < 60
ORDER BY avg_rating;