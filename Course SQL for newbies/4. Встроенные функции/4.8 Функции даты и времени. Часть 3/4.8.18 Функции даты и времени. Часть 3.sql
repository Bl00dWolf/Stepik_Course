SELECT name,
       TIMEDIFF(rent_end, rent_start)                              AS rent_time,
       CONCAT(TIMESTAMPDIFF(HOUR, rent_start, rent_end) * 10, '€') AS rent_amount
FROM Rental
WHERE car_brand = 'BMW'
ORDER BY rent_amount, name;