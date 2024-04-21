DELIMITER //
CREATE FUNCTION DIGITAL_ROOT(number INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE result INT DEFAULT 0;
    WHILE number > 9
        DO
            WHILE number > 0
                DO
                    SET result = result + number MOD 10;
                    SET number = number DIV 10;
                END WHILE;
            SET number = result;
            SET result = 0;
        END WHILE;
    RETURN number;
END //
DELIMITER ;