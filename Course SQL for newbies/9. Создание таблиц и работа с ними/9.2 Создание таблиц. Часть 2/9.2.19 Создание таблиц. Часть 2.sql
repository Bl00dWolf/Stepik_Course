CREATE TABLE Students
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(20) CHECK (CHAR_LENGTH(name) > 0),
    surname VARCHAR(20) CHECK (CHAR_LENGTH(surname) > 0)
);