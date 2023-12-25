SELECT name, surname, grade
FROM Math
WHERE grade = (SELECT grade
               FROM Math
               GROUP BY grade
               ORDER BY COUNT(*) DESC
               LIMIT 1)
ORDER BY name;