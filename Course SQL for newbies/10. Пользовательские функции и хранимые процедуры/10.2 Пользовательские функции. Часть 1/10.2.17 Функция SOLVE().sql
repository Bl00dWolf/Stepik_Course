DELIMITER //
CREATE FUNCTION SOLVE(a INT, b INT, c INT)
    RETURNS FLOAT
    DETERMINISTIC
BEGIN
    DECLARE D FLOAT;
    DECLARE x1 FLOAT;
    DECLARE x2 FLOAT;
    SET D = SQRT(POW(b, 2) - 4 * a * c);
    SET x1 = (-b + D) / (2 * a);
    SET x2 = (-b - D) / (2 * a);
    RETURN CASE
               WHEN D < 0 THEN NULL
               WHEN D = 0 THEN x1
               WHEN D > 0 THEN LEAST(x1, x2)
        END;
END //
DELIMITER ;