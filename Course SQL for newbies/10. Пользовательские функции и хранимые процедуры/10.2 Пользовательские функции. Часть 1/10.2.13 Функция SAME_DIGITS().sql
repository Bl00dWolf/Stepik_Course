DELIMITER //
CREATE FUNCTION SAME_DIGITS(number INT)
    RETURNS BOOLEAN
    DETERMINISTIC
BEGIN
    DECLARE cur_digit INT;
    DECLARE len INT;
    SET len := CHAR_LENGTH(CONVERT(number, char));
    SET cur_digit := CONVERT(LEFT(CONVERT(number, char), 1), UNSIGNED);
    RETURN cur_digit * ((POW(10, len) - 1) / (10 - 1)) = number;
end //
DELIMITER ;

# Еще вариант
CREATE FUNCTION SAME_DIGITS(number INT)
    RETURNS INT
    RETURN number = REPEAT(LEFT(number, 1), CHAR_LENGTH(number))

