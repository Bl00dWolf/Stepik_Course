SELECT name,
       surname,
       CASE
           WHEN grade BETWEEN 80 AND 100 THEN 5
           WHEN grade BETWEEN 60 AND 79 THEN 4
           WHEN grade BETWEEN 30 AND 59 THEN 3
           WHEN grade BETWEEN 10 AND 29 THEN 2
           WHEN grade BETWEEN 0 AND 9 THEN 1
           END AS grade
FROM Math
ORDER BY grade DESC, name;