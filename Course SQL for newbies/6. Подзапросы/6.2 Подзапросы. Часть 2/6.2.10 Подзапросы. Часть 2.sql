SELECT name, surname, grade
FROM Math
WHERE grade > (SELECT AVG(grade)
               FROM Math as Mth
               WHERE id < Math.id)
ORDER BY grade, name