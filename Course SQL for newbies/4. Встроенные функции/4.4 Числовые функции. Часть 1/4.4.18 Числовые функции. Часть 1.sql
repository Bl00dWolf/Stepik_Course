SELECT CONCAT('[', a, '; ', b, ']')    AS 'range',
       FLOOR(RAND() * (b + 1 - a) + a) AS random_value
FROM Ranges
ORDER BY id;