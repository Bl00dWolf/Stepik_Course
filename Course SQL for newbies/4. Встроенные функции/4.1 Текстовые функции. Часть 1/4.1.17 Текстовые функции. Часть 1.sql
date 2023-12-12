SELECT name,
       surname,
       UPPER(country) as country
FROM Directors
ORDER BY country, name;