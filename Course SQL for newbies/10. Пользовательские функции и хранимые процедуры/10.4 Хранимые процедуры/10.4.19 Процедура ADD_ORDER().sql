DELIMITER //
CREATE PROCEDURE ADD_ORDER(store_name TEXT, order_amount INT)
BEGIN
    IF store_name IS NULL OR order_amount IS NULL THEN
        SELECT 'Недостаточно данных о заказе' AS Error;
    ELSEIF order_amount <= 0 THEN
        SELECT 'Некорректная сумма заказа' AS Error;
    ELSE
        INSERT INTO Orders (store, amount)
        VALUES (store_name, order_amount);
        SELECT 'Заказ успешно добавлен' AS Success;
    END IF;
END //
DELIMITER ;