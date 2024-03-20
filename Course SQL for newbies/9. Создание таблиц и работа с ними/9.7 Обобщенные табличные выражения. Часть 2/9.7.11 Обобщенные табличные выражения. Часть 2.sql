#TODO решить

WITH RECURSIVE tabnum AS (SELECT 1 as num,
                                 1 as power
                          UNION ALL
                          SELECT num + 1, power * 2
                          FROM tabnum
                          LIMIT 10)

SELECT *
FROM tabnum;