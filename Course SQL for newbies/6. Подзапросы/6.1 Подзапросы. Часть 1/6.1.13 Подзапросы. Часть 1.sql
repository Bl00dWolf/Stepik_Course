SELECT director
FROM Films
GROUP BY director
HAVING AVG(running_time) > (SELECT AVG(running_time) FROM Films)
ORDER BY director