SELECT name,
       surname,
       status
FROM Clients
ORDER BY CASE status
             WHEN 'Gold' THEN 4
             WHEN 'Silver' THEN 3
             WHEN 'Bronze' THEN 2
             WHEN 'Basic' THEN 1
             ELSE 1
             END DESC,
         name;