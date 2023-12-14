SELECT name, surname, birth_time
FROM Actors
WHERE HOUR(birth_time) IN (8, 10, 18)
ORDER BY birth_time;