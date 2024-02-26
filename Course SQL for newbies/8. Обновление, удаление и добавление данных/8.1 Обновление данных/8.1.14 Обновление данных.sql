UPDATE Grades
SET grade = CASE
                WHEN grade = 'A' OR grade = 'B' THEN 'Great'
                WHEN grade = 'C' THEN 'Well'
                WHEN grade = 'D' OR grade = 'E' THEN 'Bad'
    END;