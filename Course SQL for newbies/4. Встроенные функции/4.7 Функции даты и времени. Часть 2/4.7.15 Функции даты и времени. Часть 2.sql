SELECT name, surname, birth_date
FROM Actors
WHERE YEAR(birth_date) > 1975
  AND QUARTER(birth_date) IN (2, 4)
ORDER BY birth_time DESC;