WITH Count AS (SELECT departure_airport AS airport_id, flights_count
               FROM Flights

               UNION ALL

               SELECT arrival_airport AS airport_id, flights_count
               FROM Flights),
     MaxFl AS (SELECT airport_id, SUM(flights_count) as flights
               FROM Count
               GROUP BY airport_id
               ORDER BY 2 DESC
               LIMIT 1),
     Result AS (SELECT airport_id, SUM(flights_count) as flights
                FROM Count
                GROUP BY airport_id
                HAVING flights = (SELECT flights FROM MaxFl)
                ORDER BY 2 DESC)

SELECT airport_id
FROM Result;

# Еще вариант

WITH Airports AS (SELECT airport_id, SUM(flights_count) AS total_flights
                  FROM (SELECT departure_airport AS airport_id, flights_count
                        FROM Flights

                        UNION ALL

                        SELECT arrival_airport AS airport_id, flights_count
                        FROM Flights) AS F
                  GROUP BY airport_id)

SELECT airport_id
FROM Airports
WHERE total_flights = (SELECT MAX(total_flights)
                       FROM Airports)
