UPDATE Grades
    JOIN Students ON Students.id = Grades.student_id
    JOIN Classes ON Classes.id = Grades.class_id
SET grade = 5
WHERE Classes.name = 'Math'
  AND Students.student = 'Mary Jane';