ALTER TABLE Students
    ADD COLUMN hometown VARCHAR(20) NOT NULL DEFAULT 'New York City' AFTER surname;