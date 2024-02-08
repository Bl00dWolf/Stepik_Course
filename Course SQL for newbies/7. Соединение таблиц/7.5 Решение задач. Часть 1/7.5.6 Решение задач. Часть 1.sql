SELECT Countries.name AS country,
       CASE
           WHEN AVG(Weather.weather_state) <= 15 THEN 'Cold'
           WHEN AVG(Weather.weather_state) >= 25 THEN 'Hot'
           ELSE 'Warm'
           END        AS weather_type
FROM Countries
         INNER JOIN Weather ON Countries.id = Weather.country_id
WHERE MONTH(Weather.day) = 9
  AND YEAR(Weather.day) = 2023
GROUP BY Countries.name;

SELECT Countries.name, Weather.weather_state
FROM Countries
         INNER JOIN Weather ON Countries.id = Weather.country_id
WHERE MONTH(Weather.day) = 9;