DELIMITER //
CREATE FUNCTION FACTORIAL(n INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE result INT DEFAULT 1;
    WHILE n != 0
        DO
            SET result = result * n;
            SET n = n - 1;
        END WHILE;
    RETURN result;
END //
DELIMITER ;