UPDATE Grades
    JOIN Classes ON Classes.id = Grades.class_id
    JOIN Students ON Students.id = Classes.id
SET grade = NULL
WHERE Grades.date_of_receipt = '2023-07-26'
  AND Classes.name = 'Biology';