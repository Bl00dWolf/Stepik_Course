SELECT REPEAT('*', CHAR_LENGTH(name)) as name,
       surname
FROM Directors
ORDER BY CHAR_LENGTH(name) DESC, surname;