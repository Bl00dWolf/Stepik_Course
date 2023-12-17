SELECT COUNT(rating) AS num_of_rated_usa_directors
FROM Directors
WHERE country = 'USA'
  AND rating > 50;