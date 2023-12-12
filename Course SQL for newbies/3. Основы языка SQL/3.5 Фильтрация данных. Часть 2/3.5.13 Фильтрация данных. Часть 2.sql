SELECT title, release_year
FROM Films
WHERE release_year in (1999, 2009)
ORDER BY release_year DESC;