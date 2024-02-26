DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Students;

-- Создание таблицы Students
CREATE TABLE Students
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    student VARCHAR(40)
);

INSERT INTO Students (student)
VALUES ('Peter Parker'),
       ('Mary Jane'),
       ('Gwen Stacy');

-- Создание таблицы Classes
CREATE TABLE Classes
(
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20)
);

INSERT INTO Classes (name)
VALUES ('Math'),
       ('Chemistry'),
       ('Biology');

-- Создание таблицы Grades
CREATE TABLE Grades
(
    student_id      INT,
    class_id        INT,
    grade           INT,
    date_of_receipt DATE
);

INSERT INTO Grades (student_id, class_id, grade, date_of_receipt)
VALUES (3, 1, 4, '2023-07-28'),
       (1, 1, 5, '2023-07-28'),
       (3, 3, 4, '2023-07-26'),
       (1, 2, 5, '2023-07-27'),
       (2, 1, 3, '2023-07-28'),
       (2, 2, 4, '2023-07-27'),
       (1, 3, 5, '2023-07-26'),
       (2, 3, 3, '2023-07-26'),
       (3, 2, 5, '2023-07-27');

UPDATE Grades
SET grade = 5
WHERE (SELECT )
LIMIT 1;