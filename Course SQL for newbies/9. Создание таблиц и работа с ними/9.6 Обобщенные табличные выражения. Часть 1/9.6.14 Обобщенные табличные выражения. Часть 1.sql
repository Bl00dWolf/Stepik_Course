WITH MaxSal AS (SELECT company_id,
                       MAX(salary) as MaxSal,
                       CASE
                           WHEN MAX(salary) < 1000 THEN 0
                           WHEN MAX(salary) BETWEEN 1000 AND 10000 THEN 0.24
                           WHEN MAX(salary) > 10000 THEN 0.49
                           END     as TaxRate
                FROM Salaries
                GROUP BY company_id)

SELECT Salaries.employee_id                                        AS id,
       Salaries.employee_name                                      AS name,
       ROUND(Salaries.salary - (Salaries.salary * MaxSal.TaxRate)) AS salary
FROM Salaries
         JOIN MaxSal ON Salaries.company_id = MaxSal.company_id;