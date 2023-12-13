SELECT name,
       surname,
       SUBSTRING_INDEX(email, '@', 1) as local_part,
       SUBSTRING_INDEX(email, '@', -1) as domain
FROM Directors
ORDER BY name;