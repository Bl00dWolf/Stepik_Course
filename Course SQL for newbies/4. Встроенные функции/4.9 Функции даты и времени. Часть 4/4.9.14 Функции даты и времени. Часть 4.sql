SELECT name,
       surname,
       STR_TO_DATE(birth_date, '%d %b %Y')               AS birth_date,
       STR_TO_DATE(birth_time, 'Hours: %H, Minutes: %i') AS birth_time
FROM Actors
WHERE MONTH(STR_TO_DATE(birth_date, '%d %b %Y')) = 9;