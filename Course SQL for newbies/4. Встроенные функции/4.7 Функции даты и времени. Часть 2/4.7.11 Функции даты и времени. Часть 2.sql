SELECT id,
       SUBSTRING_INDEX(actor, ' ', 1)  AS name,
       SUBSTRING_INDEX(actor, ' ', -1) AS surname,
       DATE(birth_date)                as birth_date,
       TIME(birth_date)                as birth_time
FROM Actors;