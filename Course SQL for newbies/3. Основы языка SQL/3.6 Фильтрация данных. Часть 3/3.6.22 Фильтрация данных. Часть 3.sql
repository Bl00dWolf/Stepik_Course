SELECT title, director
FROM Films
WHERE title NOT LIKE '_% _%'
ORDER BY title;