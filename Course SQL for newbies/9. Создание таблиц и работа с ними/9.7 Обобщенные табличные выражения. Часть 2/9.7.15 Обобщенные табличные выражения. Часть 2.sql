WITH RECURSIVE fact AS (SELECT 1 as number, 1 as factorial
                        UNION
                        DISTINCT
                        SELECT number + 1, (number + 1) * factorial
                        FROM fact
                        WHERE number < 20)
SELECT *
FROM fact;