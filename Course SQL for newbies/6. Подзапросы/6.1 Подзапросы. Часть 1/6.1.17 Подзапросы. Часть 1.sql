SELECT director, COUNT(*) AS num_of_films
FROM Films
WHERE running_time > (SELECT AVG(running_time) FROM Films)
GROUP BY director
ORDER BY num_of_films DESC, director