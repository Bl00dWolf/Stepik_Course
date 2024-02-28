UPDATE Grades
SET grade = 5
WHERE student_id = (SELECT id FROM Students WHERE student = 'Gwen Stacy')
ORDER BY date_of_receipt
LIMIT 1;