SELECT name,
       surname,
       TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) as age
FROM Actors
ORDER BY age DESC;