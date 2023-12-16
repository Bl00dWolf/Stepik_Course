SELECT COALESCE(name, surname, 'Unknown') AS director,
       rating
FROM Directors
ORDER BY rating DESC;