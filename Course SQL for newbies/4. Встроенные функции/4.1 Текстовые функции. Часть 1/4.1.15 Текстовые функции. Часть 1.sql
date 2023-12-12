SELECT name, surname
FROM Directors
WHERE CHAR_LENGTH(name) <= 6
ORDER BY name;