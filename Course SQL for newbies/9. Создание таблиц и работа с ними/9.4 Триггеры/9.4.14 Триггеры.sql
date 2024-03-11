DELIMITER //
CREATE TRIGGER on_new_purchase
    AFTER INSERT
    ON Purchases
    FOR EACH ROW
BEGIN
    UPDATE Users
    SET total_spending = total_spending + (SELECT Films.price
                                           FROM Films
                                                    JOIN Purchases ON Films.id = Purchases.film_id
                                           WHERE NEW.film_id = Films.id
                                             AND NEW.user_id = Purchases.user_id)
    WHERE NEW.user_id = id;
END //
DELIMITER ;

# Еще вариант
CREATE TRIGGER total_spending_updating
    AFTER INSERT
    ON Purchases
    FOR EACH ROW
    UPDATE Users
    SET total_spending = total_spending + (SELECT price
                                           FROM Films
                                           WHERE id = NEW.film_id)
    WHERE id = NEW.user_id
