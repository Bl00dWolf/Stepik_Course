DELIMITER //
CREATE PROCEDURE DELETE_UNKNOWN_ORDERS()
BEGIN
    DELETE
    FROM Orders
    WHERE store IS NULL
       OR amount IS NULL;
END //
DELIMITER ;