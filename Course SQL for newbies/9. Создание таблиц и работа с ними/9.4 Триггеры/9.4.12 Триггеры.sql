DELIMITER //
CREATE TRIGGER phone_number_formatting_before_update
    BEFORE UPDATE
    ON Users
    FOR EACH ROW
BEGIN
    SET NEW.phone_number = CONCAT('+7', RIGHT(REPLACE(NEW.phone_number, ' ', ''), 10));
END //

CREATE TRIGGER phone_number_formatting_before_insert
    BEFORE INSERT
    ON Users
    FOR EACH ROW
BEGIN
    SET NEW.phone_number = CONCAT('+7', RIGHT(REPLACE(NEW.phone_number, ' ', ''), 10));
END //
DELIMITER ;

# Еще вариант
CREATE TRIGGER formatting_phone_before_update
    BEFORE UPDATE
    ON Users
    FOR EACH ROW
    SET NEW.phone_number = CONCAT('+7', SUBSTRING(REPLACE(NEW.phone_number, ' ', ''), 3));


CREATE TRIGGER formatting_phone_before_insert
    BEFORE INSERT
    ON Users
    FOR EACH ROW
    SET NEW.phone_number = CONCAT('+7', SUBSTRING(REPLACE(NEW.phone_number, ' ', ''), 3))