SELECT name,
       surname,
       REPLACE(card_number, '-', '') AS card_number
FROM Clients
WHERE LEFT(surname, 1) = 'S'
ORDER BY surname