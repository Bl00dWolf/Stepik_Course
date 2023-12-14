SELECT CONCAT(name, ' ', surname)            AS staffer,
       hire_date + INTERVAL '1 6' YEAR_MONTH as hire_date
FROM Staff
ORDER BY 2 DESC;