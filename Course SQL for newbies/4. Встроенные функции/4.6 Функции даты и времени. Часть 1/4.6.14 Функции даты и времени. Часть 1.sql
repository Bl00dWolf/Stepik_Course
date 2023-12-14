SELECT CONCAT(name, ' ', surname)    AS staffer,
       MAKEDATE(hire_year, hire_day) AS hire_date
FROM Staff
ORDER BY 2 DESC;