SELECT CONCAT(LEFT(name, 1), '. ', surname) as director
FROM Directors
ORDER BY LEFT(name, 1), surname;