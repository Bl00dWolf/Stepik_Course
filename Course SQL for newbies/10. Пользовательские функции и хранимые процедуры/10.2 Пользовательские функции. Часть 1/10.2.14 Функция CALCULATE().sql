DELIMITER //
CREATE FUNCTION CALCULATE(a FLOAT, b FLOAT, operation TEXT)
    RETURNS FLOAT
    DETERMINISTIC
BEGIN
    RETURN
        CASE operation
            WHEN '+' THEN a + b
            WHEN '-' THEN a - b
            WHEN '*' THEN a * b
            WHEN '/' THEN a / b
            END;
END //
DELIMITER ;