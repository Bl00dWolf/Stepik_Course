CREATE TABLE Students
(
    id              INT         NOT NULL UNIQUE,
    name            VARCHAR(20) NOT NULL CHECK (CHAR_LENGTH(name) > 0),
    surname         VARCHAR(20) NOT NULL CHECK (CHAR_LENGTH(surname) > 0),
    age             INT  DEFAULT 18 CHECK (age >= 18),
    date_of_receipt DATE DEFAULT (CURDATE()) CHECK (date_of_receipt >= '2023-09-01')
)