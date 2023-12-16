SELECT name,
       surname,
       country,
       IF(country = 'USA', IF(rating + 10 > 100, 100, rating + 10), rating) AS rating
FROM Directors
ORDER BY rating DESC, name;