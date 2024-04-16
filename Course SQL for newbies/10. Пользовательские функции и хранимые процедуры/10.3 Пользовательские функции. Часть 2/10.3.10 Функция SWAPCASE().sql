DELIMITER //
CREATE FUNCTION SWAPCASE(string TEXT)
    RETURNS TEXT
    DETERMINISTIC
BEGIN
    DECLARE result TEXT DEFAULT '';
    WHILE CHAR_LENGTH(string) != 0
        DO
            IF BINARY LEFT(string, 1) = BINARY LEFT(UPPER(string), 1) THEN
                SET result = CONCAT(result, LOWER(LEFT(string, 1)));
            ELSE
                SET result = CONCAT(result, UPPER(LEFT(string, 1)));
            END IF;
            SET string = RIGHT(string, CHAR_LENGTH(string) - 1);
        END WHILE;
    RETURN result;
END //
DELIMITER ;