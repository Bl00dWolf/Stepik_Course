DELIMITER //
CREATE FUNCTION IS_DIGIT(string TEXT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    WHILE CHAR_LENGTH(string) != 0
        DO
            IF RIGHT(string, 1) NOT IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') THEN
                RETURN 0;
            END IF;
            SET string = LEFT(string, CHAR_LENGTH(string) - 1);
        end while;
    RETURN 1;
END //
DELIMITER ;