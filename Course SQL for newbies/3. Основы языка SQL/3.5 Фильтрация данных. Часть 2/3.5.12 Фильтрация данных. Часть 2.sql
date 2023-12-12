SELECT title, director, release_year
FROM Films
WHERE director = 'John Lasseter'
  AND release_year < 2000
ORDER BY release_year;