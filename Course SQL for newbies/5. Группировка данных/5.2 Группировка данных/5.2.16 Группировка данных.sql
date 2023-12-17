SELECT country, rating, COUNT(*) AS num_of_directors
FROM Directors
GROUP BY country, rating
ORDER BY num_of_directors, country, rating