SELECT bike_number,
       MAX(end_time) AS last_ride_end
FROM Rides
GROUP BY bike_number
ORDER BY last_ride_end DESC;