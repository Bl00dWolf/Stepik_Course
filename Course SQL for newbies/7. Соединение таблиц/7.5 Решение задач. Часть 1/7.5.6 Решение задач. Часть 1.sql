SELECT *
FROM Countries
         INNER JOIN Weather ON Countries.id = Weather.country_id
GROUP BY