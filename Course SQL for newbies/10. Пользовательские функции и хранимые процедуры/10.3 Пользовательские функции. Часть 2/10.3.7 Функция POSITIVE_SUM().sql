DELIMITER //
CREATE FUNCTION POSITIVE_SUM(a INT, b INT, c INT)
    RETURNS INT
    DETERMINISTIC
BEGIN
    IF a < 0 THEN
        SET a = 0;
    end if;

    IF b < 0 THEN
        SET b = 0;
    end if;

    IF c < 0 THEN
        SET c = 0;
    end if;

    RETURN a + b + c;
END //
DELIMITER ;

# еще вариант
DELIMITER //
CREATE FUNCTION POSITIVE_SUM(a INTEGER, b INTEGER, c INTEGER)
    RETURNS INTEGER
    DETERMINISTIC
BEGIN
    RETURN IF(a > 0, a, 0) + IF(b > 0, b, 0) + IF(c > 0, c, 0);
END //
DELIMITER ;