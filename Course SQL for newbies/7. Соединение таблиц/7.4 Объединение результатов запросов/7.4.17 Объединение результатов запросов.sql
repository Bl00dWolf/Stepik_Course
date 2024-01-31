SELECT IFNULL(CASE
                  WHEN duration BETWEEN 0 AND 299 THEN '[0-5)'
                  WHEN duration BETWEEN 300 AND 599 THEN '[5-10)'
                  WHEN duration BETWEEN 600 AND 899 THEN '[10-15)'
                  WHEN duration >= 900 THEN '15 or more'
                  END, 0) AS session_duration,
       COUNT(*)           AS total
FROM Sessions
GROUP BY session_duration;


SELECT '[0-5)' AS session_duration, COUNT(*) AS total
FROM Sessions
WHERE duration BETWEEN 0 AND 299
GROUP BY session_duration

UNION

SELECT '[5-10)' AS session_duration, COUNT(*)
FROM Sessions
WHERE duration BETWEEN 300 AND 599
GROUP BY session_duration

UNION

SELECT '[10-15)' AS session_duration, COUNT(*)
FROM Sessions
WHERE duration BETWEEN 600 AND 899
GROUP BY session_duration

UNION

SELECT '15 or more' AS session_duration, COUNT(*)
FROM Sessions
WHERE duration >= 900
GROUP BY session_duration;

SELECT '[5-10)' AS session_duration
FROM Sessions
WHERE duration BETWEEN 300 AND 599;