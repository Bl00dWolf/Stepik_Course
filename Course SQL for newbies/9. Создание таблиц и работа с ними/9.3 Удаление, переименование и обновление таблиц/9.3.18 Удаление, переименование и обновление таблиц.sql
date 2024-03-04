ALTER TABLE Students
    ADD CHECK (CHAR_LENGTH(name) >= 2),
    ADD CHECK (CHAR_LENGTH(surname) >= 2),
    ADD CHECK (age > 0);