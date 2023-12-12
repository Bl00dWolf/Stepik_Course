SELECT name,
       CHAR_LENGTH(name) AS name_length
FROM Directors
ORDER BY name_length, name;