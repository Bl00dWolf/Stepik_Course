SELECT name,
       surname,
       CONCAT_WS(' ', DAY(birth_date), MONTHNAME(birth_date), YEAR(birth_date)) AS birth_date
FROM Actors
WHERE MONTH(birth_date) BETWEEN 5 AND 7