SELECT name, surname, rating
INTO @name, @surname, @rating
FROM Directors
WHERE country = 'USA'
  and rating = (SELECT MIN(rating) FROM Directors WHERE country = 'USA' LIMIT 1);