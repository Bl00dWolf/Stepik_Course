WITH RECURSIVE numm AS (SELECT *
                        FROM Numbers
                        UNION
                        DISTINCT
                        SELECT num + 1
                        FROM numm
                        WHERE num < (SELECT MAX(num) FROM Numbers))

SELECT *
FROM numm
ORDER BY num;