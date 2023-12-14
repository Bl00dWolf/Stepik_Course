SELECT CONCAT(name, ' ', surname) AS staffer
FROM Staff
WHERE TO_DAYS(LAST_DAY(hire_date)) - TO_DAYS(hire_date) < 15
ORDER BY staffer;