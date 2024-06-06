WITH preseq AS (SELECT *,
                       ROW_NUMBER() over (PARTITION BY passenger_id ORDER BY requested_on) as ride
                FROM Rides)

SELECT passenger_id, amount, requested_on
FROM preseq
WHERE ride = 3;