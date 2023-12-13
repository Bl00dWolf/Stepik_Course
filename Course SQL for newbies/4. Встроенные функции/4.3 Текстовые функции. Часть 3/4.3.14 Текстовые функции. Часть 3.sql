SELECT CONCAT(UPPER(SUBSTRING(name, 1, 1)), SUBSTRING(name, 2))       AS name,
       CONCAT(UPPER(SUBSTRING(surname, 1, 1)), SUBSTRING(surname, 2)) AS surname
FROM Directors
WHERE BINARY SUBSTRING(name, 1, 1) = LOWER(SUBSTRING(name, 1, 1))
   OR BINARY SUBSTRING(surname, 1, 1) = LOWER(SUBSTRING(surname, 1, 1))
ORDER BY name;