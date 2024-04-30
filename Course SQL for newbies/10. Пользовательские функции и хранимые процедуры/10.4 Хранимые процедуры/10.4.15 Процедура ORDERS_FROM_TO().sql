DELIMITER //
CREATE PROCEDURE ORDERS_FROM_TO(start_date DATE, end_date DATE)
BEGIN
    SELECT *
    FROM Orders
    WHERE order_date BETWEEN start_date AND end_date;
END //
DELIMITER ;