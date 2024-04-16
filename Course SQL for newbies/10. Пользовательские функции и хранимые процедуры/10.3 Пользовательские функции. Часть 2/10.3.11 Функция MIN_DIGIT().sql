DELIMITER //
CREATE FUNCTION MIN_DIGIT(number INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE MINVAL INT DEFAULT 9;
    WHILE number != 0
        DO
            IF number MOD 10 < MINVAL THEN
                SET MINVAL = number MOD 10;
            END IF;
            SET number = number DIV 10;
        END WHILE;
    RETURN MINVAL;
END //
DELIMITER ;