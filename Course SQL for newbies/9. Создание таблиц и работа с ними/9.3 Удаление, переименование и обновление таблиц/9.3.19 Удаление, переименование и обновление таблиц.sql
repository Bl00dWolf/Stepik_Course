ALTER TABLE Students
    ADD COLUMN name    VARCHAR(20),
    ADD COLUMN surname VARCHAR(20);

UPDATE Students
SET name = SUBSTRING_INDEX(fullname, ' ', 1);

UPDATE Students
SET surname = SUBSTRING_INDEX(fullname, ' ', -1);

ALTER TABLE Students
    DROP COLUMN fullname;

# Еще вариант
ALTER TABLE Students
    ADD COLUMN name    VARCHAR(20) DEFAULT (SUBSTRING_INDEX(fullname, ' ', 1)),
    ADD COLUMN surname VARCHAR(20) DEFAULT (SUBSTRING_INDEX(fullname, ' ', -1));

ALTER TABLE Students
    ALTER COLUMN name DROP DEFAULT,
    ALTER COLUMN surname DROP DEFAULT,
    DROP COLUMN fullname;