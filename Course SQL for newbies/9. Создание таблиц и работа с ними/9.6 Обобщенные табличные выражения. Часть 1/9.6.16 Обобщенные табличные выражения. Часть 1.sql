WITH Pass_Bus_Time AS (SELECT Passengers.id, Buses.departure_time
                       FROM Passengers
                                JOIN Buses ON Passengers.arrival_time <= Buses.departure_time),
     Pass_Bus_Min_Time AS (SELECT id AS passenger_id, MIN(departure_time) AS dep_time
                           FROM Pass_Bus_Time
                           GROUP BY id)


SELECT Buses.id AS bus_id, COUNT(*) AS passenger_count
FROM Pass_Bus_Min_Time
         JOIN Buses ON Pass_Bus_Min_Time.dep_time = Buses.departure_time
GROUP BY bus_id
ORDER BY bus_id;

# Еще вариант
WITH minPassengersTime AS (SELECT Passengers.id,
                                  MIN(Buses.departure_time) AS arrival_time
                           FROM Passengers,
                                Buses
                           WHERE Passengers.arrival_time <= Buses.departure_time
                           GROUP BY Passengers.id)
SELECT Buses.id,
       COUNT(minPassengersTime.id) AS passenger_count
FROM Buses,
     minPassengersTime
WHERE departure_time = arrival_time
GROUP BY Buses.id
ORDER BY Buses.id;