DROP PROCEDURE IF EXISTS STORE_STATISTICS;

DELIMITER //
CREATE PROCEDURE STORE_STATISTICS(store_name TEXT, OUT avg_order_amount FLOAT, OUT min_order_amount FLOAT,
                                  OUT max_order_amount FLOAT)
BEGIN
    SELECT (SELECT AVG(amount) FROM Orders WHERE store = store_name),
           (SELECT MIN(amount) FROM Orders WHERE store = store_name),
           (SELECT MAX(amount) FROM Orders WHERE store = store_name)
    INTO avg_order_amount, min_order_amount, max_order_amount;
END //
DELIMITER ;

CALL STORE_STATISTICS('Ozon', @avg, @min, @max);
SELECT @avg, @min, @max;
