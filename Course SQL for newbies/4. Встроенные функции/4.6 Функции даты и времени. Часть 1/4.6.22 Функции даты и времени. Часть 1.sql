SELECT CONCAT(name, ' ', surname) AS staffer,
       LAST_DAY(hire_date)        AS first_salary
FROM Staff
ORDER BY salary DESC;