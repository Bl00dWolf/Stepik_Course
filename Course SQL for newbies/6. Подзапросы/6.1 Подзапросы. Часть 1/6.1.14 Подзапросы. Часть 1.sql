SELECT director
FROM Films
GROUP BY director
HAVING MIN(running_time) = (SELECT MIN(running_time) FROM Films)
ORDER BY director