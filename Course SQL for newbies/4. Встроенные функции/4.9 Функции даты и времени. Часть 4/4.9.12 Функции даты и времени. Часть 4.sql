SELECT name,
       surname,
       DATE_FORMAT(birth_date, '%d.%m.%Y') AS birth_date,
       TIME_FORMAT(birth_time, '%H:%i')    AS birth_time
FROM Actors
WHERE DAYOFMONTH(birth_date) <= 14;