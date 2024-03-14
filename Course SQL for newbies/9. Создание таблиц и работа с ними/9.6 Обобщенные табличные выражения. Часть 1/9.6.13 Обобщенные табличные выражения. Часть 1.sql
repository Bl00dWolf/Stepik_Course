WITH MaxAiro AS (SELECT *
                 FROM Flights AS F1
                          JOIN Flights AS F2 ON F1.departure_airport = F2.arrival_airport)

SELECT *
FROM MaxAiro;

SELECT F1.departure_airport, SUM(F1.flights_count + F2.flights_count)
FROM Flights AS F1
         JOIN Flights AS F2 ON F1.departure_airport = F2.arrival_airport
GROUP BY F1.departure_airport
ORDER BY 2 DESC;