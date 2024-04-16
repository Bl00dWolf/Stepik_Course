DELIMITER //
CREATE FUNCTION SUM_OF_FIRST_DIGITS(string TEXT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE result INT DEFAULT 0;
    WHILE LEFT(string, 1) IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        DO
            SET result = result + CAST(LEFT(string, 1) AS UNSIGNED);
            SET string = RIGHT(string, CHAR_LENGTH(string) - 1);
        END WHILE;
    RETURN result;
END //
DELIMITER ;