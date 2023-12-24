SELECT title
FROM Films
WHERE running_time = (SELECT running_time FROM Films WHERE title = 'WALL-E')
  AND title != 'WALL-E';