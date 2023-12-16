SELECT name,
       surname,
       IF(country = 'England', country, 'Other country') AS country
FROM Directors
ORDER BY name;