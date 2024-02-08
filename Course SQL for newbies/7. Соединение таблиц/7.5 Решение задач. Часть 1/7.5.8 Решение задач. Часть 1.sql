SELECT Departments.name AS department, COUNT(Students.id) AS students_count
FROM Departments
         LEFT JOIN Students ON Departments.id = Students.dept_id
GROUP BY Departments.name
ORDER BY 2 DESC, 1;