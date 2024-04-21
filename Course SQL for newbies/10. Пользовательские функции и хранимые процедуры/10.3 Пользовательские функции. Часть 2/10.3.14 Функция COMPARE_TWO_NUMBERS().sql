DELIMITER //
CREATE FUNCTION COMPARE_TWO_NUMBERS(a INT, b INT)
    RETURNS TEXT
    DETERMINISTIC
BEGIN
    IF a < b THEN
        RETURN CONCAT(a, ' < ', b);
    ELSEIF a > b THEN
        RETURN CONCAT(a, ' > ', b);
    ELSEIF a = b THEN
        RETURN CONCAT(a, ' = ', b);
    END IF;
END //
DELIMITER ;