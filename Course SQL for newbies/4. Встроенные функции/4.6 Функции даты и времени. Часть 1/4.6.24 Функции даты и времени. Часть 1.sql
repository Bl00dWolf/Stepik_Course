SELECT CONCAT(name, ' ', surname) AS staffer
FROM Staff
WHERE TO_DAYS('2023-07-15') - TO_DAYS(hire_date) > 9000
ORDER BY hire_date;
