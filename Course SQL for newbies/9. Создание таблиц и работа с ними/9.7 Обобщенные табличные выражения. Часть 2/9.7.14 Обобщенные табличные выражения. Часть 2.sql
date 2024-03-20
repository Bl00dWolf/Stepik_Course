WITH RECURSIVE months AS (SELECT DATE('1970-01-01') AS month
                          UNION
                          DISTINCT
                          SELECT month + INTERVAL 1 MONTH
                          FROM months
                          LIMIT 12)

SELECT MONTHNAME(month) AS month
FROM months;

# еще вариант
WITH RECURSIVE Months AS (SELECT CONVERT('January', CHAR(10)) AS month,
                                 '2023-02-01'                 AS current_month
                          UNION
                          SELECT MONTHNAME(current_month), current_month + INTERVAL 1 MONTH
                          FROM Months
                          LIMIT 12)

SELECT month
FROM Months;