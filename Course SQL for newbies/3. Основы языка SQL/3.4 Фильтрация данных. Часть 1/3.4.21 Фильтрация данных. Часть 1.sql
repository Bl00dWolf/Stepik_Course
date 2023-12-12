SELECT title AS 'Movie', director AS 'Directed by'
FROM Films
WHERE director IS NOT NULL
ORDER BY director, title;