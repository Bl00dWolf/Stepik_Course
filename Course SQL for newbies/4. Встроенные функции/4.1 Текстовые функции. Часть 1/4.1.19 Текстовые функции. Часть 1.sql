SELECT name,
       surname,
       CONCAT(LPAD(rating, 3, '0'), '%') as rating
FROM Directors
ORDER BY rating;