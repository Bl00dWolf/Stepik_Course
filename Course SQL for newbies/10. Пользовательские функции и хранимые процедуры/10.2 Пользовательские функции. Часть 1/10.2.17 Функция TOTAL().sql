DELIMITER //
CREATE FUNCTION TOTAL(store_name TEXT)
    RETURNS INT
    NOT DETERMINISTIC
    READS SQL DATA
BEGIN
    RETURN (SELECT SUM(amount)
            FROM Orders
            WHERE store = store_name);
END //
DELIMITER ;
