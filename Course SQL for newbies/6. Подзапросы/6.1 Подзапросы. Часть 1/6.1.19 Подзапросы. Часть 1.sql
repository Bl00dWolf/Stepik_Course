SELECT title
FROM Films
WHERE running_time < ALL (SELECT running_time FROM Films WHERE director = 'John Lasseter')
ORDER BY title