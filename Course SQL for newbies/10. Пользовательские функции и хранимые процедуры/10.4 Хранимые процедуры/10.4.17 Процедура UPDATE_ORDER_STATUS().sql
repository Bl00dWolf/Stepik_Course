DELIMITER //
CREATE PROCEDURE UPDATE_ORDER_STATUS(IN order_id INT, OUT updated_status TEXT)
BEGIN
    UPDATE Orders
    SET status = CASE status
                     WHEN 'Created' THEN 'Shipped'
                     WHEN 'Shipped' THEN 'Delivered'
                     WHEN 'Delivered' THEN 'Completed'
        END
    WHERE id = order_id;
    SET updated_status = (SELECT status FROM Orders WHERE id = order_id);
END //
DELIMITER ;