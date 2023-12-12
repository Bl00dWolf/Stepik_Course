SELECT title, director, running_time
FROM Films
WHERE director IN ('John Lasseter', 'Andrew Stanton')
  AND running_time > 100
ORDER BY director, title;