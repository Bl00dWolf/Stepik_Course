SELECT MIN(rating) AS min_rating,
       MAX(rating) AS max_rating
FROM Directors
WHERE country = 'USA';