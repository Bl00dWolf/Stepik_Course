SELECT title, director
FROM Films
WHERE title NOT LIKE BINARY '%t%'
ORDER BY title;