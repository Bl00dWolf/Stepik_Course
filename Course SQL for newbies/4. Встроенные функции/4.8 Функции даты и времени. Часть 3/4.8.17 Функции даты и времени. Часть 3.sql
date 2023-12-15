SELECT name, surname, birth_date
FROM Actors
WHERE TIMESTAMPDIFF(YEAR, birth_date, '2023-09-12') > 50
ORDER BY birth_date DESC;