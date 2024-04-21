DELIMITER //
CREATE FUNCTION SUM_OF_MID_DIGITS(string TEXT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE result INT DEFAULT 0;
    IF CHAR_LENGTH(string) IN (1, 2) THEN
        RETURN 0;
    END IF;
    SET string = LEFT(string, CHAR_LENGTH(string) - 1);
    SET string = RIGHT(string, CHAR_LENGTH(string) - 1);
    WHILE LEFT(string, 1) IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        DO
            SET result = result + CAST(LEFT(string, 1) AS UNSIGNED);
            SET string = RIGHT(string, CHAR_LENGTH(string) - 1);
        END WHILE;
    RETURN result;
END //
DELIMITER ;

# еще вариант
DELIMITER //
CREATE FUNCTION SUM_OF_MID_DIGITS(number INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE total INT DEFAULT 0;
    WHILE number > 99
        DO
            SET number := number DIV 10;
            SET total := total + number % 10;
        END WHILE;
    RETURN total;
END //
DELIMITER ;
