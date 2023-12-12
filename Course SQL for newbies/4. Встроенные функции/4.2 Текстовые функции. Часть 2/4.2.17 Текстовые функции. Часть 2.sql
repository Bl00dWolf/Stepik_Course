SELECT CONCAT(LEFT(name, 1), REPEAT('*', CHAR_LENGTH(name) - 1))       AS name,
       CONCAT(LEFT(surname, 1), REPEAT('*', CHAR_LENGTH(surname) - 1)) AS surname
FROM Directors
ORDER BY LEFT(name, 1), LEFT(surname, 1);