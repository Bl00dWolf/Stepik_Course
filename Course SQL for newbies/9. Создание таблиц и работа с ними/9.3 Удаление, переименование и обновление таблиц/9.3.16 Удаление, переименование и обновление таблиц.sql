ALTER TABLE Students
    DROP COLUMN id,
    ADD PRIMARY KEY (name, surname);