DELIMITER //
CREATE TRIGGER em_logging
    AFTER UPDATE
    ON Users
    FOR EACH ROW
BEGIN
    INSERT INTO UsersEmailHistory (user_id, old_email, new_email, updated_on)
    VALUES (OLD.id, OLD.email, NEW.email, CURDATE());
END //
DELIMITER ;

# Еще вариант
CREATE TRIGGER email_logging
    AFTER UPDATE
    ON Users
    FOR EACH ROW
    INSERT INTO UsersEmailHistory (user_id, old_email, new_email, updated_on)
    VALUES (OLD.id, OLD.email, NEW.email, CURDATE())