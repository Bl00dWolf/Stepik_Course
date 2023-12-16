SELECT name,
       surname,
       CASE
           WHEN grade IN ('A', 'B') THEN 'Great'
           WHEN grade = 'C' THEN 'Well'
           WHEN grade IN ('D', 'E') THEN 'Bad'
           END AS result
FROM Math
ORDER BY grade, name;