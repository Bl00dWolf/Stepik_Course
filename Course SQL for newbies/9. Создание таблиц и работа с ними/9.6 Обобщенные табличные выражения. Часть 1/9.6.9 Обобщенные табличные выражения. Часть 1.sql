WITH Grades_Math AS (SELECT CASE grade
                                WHEN 'A' THEN 'Great'
                                WHEN 'B' THEN 'Great'
                                WHEN 'C' THEN 'Well'
                                WHEN 'D' THEN 'Bad'
                                WHEN 'E' THEN 'Bad'
                                END  AS categ,
                            COUNT(*) as num
                     FROM Math
                     GROUP BY categ)

SELECT categ AS result, num AS students
FROM Grades_Math;

# Еще вариант
WITH TextGrades (result) AS (SELECT CASE
                                        WHEN grade IN ('A', 'B') THEN 'Great'
                                        WHEN grade = 'C' THEN 'Well'
                                        ELSE 'Bad'
                                        END
                             FROM Math)

SELECT result, COUNT(*) AS students
FROM TextGrades
GROUP BY result