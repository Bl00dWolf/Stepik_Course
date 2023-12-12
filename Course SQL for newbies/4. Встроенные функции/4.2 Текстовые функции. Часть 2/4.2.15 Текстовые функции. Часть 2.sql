SELECT id,
       name,
       surname,
       CONCAT(
               REPEAT('*', 12),
               RIGHT(REPLACE(card_number, '-', ''), 4)) AS card_number
FROM Clients
LIMIT 5;