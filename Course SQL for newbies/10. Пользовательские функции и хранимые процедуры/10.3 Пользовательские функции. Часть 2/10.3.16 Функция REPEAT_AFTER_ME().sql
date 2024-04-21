DELIMITER //
CREATE FUNCTION REPEAT_AFTER_ME(delimiter TEXT, n INT)
    RETURNS TEXT
    DETERMINISTIC
BEGIN
    DECLARE anti_N INT DEFAULT 0;
    DECLARE result TEXT DEFAULT '';
    WHILE anti_N < n
        DO
            SET result = CONCAT(result, anti_N, ' ', delimiter, ' ');
            SET anti_N = anti_N + 1;
        END WHILE;
    RETURN CONCAT(result, n);
END //
DELIMITER ;