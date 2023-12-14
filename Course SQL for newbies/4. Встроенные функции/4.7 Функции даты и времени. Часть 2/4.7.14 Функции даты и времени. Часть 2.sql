SELECT name, surname, birth_date
FROM Actors
WHERE WEEKDAY(birth_date) = 2
ORDER BY birth_date;