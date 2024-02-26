UPDATE Grades
    INNER JOIN Students ON Grades.student_id = Students.id
SET Grades.grade = 5
WHERE Students.student = 'Peter Parker';