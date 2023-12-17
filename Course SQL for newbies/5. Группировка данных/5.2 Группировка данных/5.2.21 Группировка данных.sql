SELECT QUARTER(birth_date)          AS quarter,
       GROUP_CONCAT(CONCAT(name, ' ', surname)
                    ORDER BY CONCAT(name, ' ', surname)
                    SEPARATOR ', ') AS directors
FROM Directors
GROUP BY quarter
HAVING COUNT(CONCAT(name, ' ', surname)) > 1;