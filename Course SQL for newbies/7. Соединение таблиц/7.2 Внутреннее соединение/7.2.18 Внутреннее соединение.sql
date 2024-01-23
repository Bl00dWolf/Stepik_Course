SELECT E1.name
FROM Employees AS E1
         INNER JOIN Employees AS E2 ON E1.manager_id = E2.id
WHERE E1.salary > E2.salary