SELECT name,
       surname,
       COALESCE(rating, 0) AS rating
FROM Directors
ORDER BY 3, name;