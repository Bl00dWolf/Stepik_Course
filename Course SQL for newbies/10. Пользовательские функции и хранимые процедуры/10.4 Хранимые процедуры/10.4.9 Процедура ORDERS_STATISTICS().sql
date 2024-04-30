DELIMITER //
CREATE PROCEDURE ORDERS_STATISTICS()
BEGIN
    SELECT (SELECT COUNT(id) FROM Orders)   AS orders_count,
           (SELECT AVG(amount) FROM Orders) AS avg_order_amount;
END //
DELIMITER ;