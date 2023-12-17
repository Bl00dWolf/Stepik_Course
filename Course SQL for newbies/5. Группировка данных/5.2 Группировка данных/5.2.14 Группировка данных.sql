SELECT country, AVG(rating) AS avg_rating
FROM Directors
GROUP BY country
ORDER BY avg_rating;