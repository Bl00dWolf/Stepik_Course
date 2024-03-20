WITH RECURSIVE decdec AS (SELECT DATE('2024-12-31') as day
                          UNION
                          DISTINCT
                          SELECT day - INTERVAL 1 DAY
                          FROM decdec
                          LIMIT 31)

SELECT *
FROM decdec;