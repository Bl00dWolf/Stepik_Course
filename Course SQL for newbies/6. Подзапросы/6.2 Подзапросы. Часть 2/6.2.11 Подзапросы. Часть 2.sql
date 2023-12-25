SELECT name, surname, grade
FROM Math
WHERE grade = (SELECT grade
               FROM Math as Mt
               WHERE Math.id = id - 1)
   OR grade = (SELECT grade
               FROM Math as Mt
               WHERE Math.id = id + 1)
ORDER BY name;

# еще вариант
# SELECT name, surname, grade
# FROM Math AS M
# WHERE grade = ANY (SELECT grade
#                    FROM Math
#                    WHERE id IN (M.id - 1, M.id + 1))
# ORDER BY name