DELIMITER //
CREATE FUNCTION LAST_SECOND_DIGIT(number INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE func TEXT;
    SET func = LEFT(RIGHT(CONVERT(number, char), 2), 1);
    RETURN IF(CHAR_LENGTH(CONVERT(number, char)) = 1, NULL, func);
END //
DELIMITER ;

# Еще вариант
DELIMITER //
CREATE FUNCTION LAST_SECOND_DIGIT(number INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    RETURN IF(CHAR_LENGTH(number) > 1, number DIV 10 MOD 10, NULL);
END //
DELIMITER ;