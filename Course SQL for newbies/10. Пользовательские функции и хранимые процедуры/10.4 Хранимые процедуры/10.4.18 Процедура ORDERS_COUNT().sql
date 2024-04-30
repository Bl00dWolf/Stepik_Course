DELIMITER //
CREATE PROCEDURE ORDERS_COUNT(store_name TEXT)
BEGIN
    IF store_name IS NULL THEN
        SELECT store, COUNT(*) AS orders_count
        FROM Orders
        GROUP BY store;
    ELSE
        SELECT COUNT(*) AS orders_count
        FROM Orders
        WHERE store = store_name;
    END IF;
END //
DELIMITER ;