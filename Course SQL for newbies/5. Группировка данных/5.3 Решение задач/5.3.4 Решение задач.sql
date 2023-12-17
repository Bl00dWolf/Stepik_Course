SELECT id,
       name,
       surname,
       MAX(salary) AS salary
FROM Salary
GROUP BY id, name, surname