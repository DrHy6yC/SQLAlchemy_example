DELIMITER ;
drop trigger IF EXISTS Example.USERS_BEFORE_UPDATE;
DELIMITER //
CREATE DEFINER = CURRENT_USER TRIGGER Example.USERS_BEFORE_UPDATE BEFORE UPDATE
ON USERS FOR EACH ROW
BEGIN
    SET NEW.user_edit_time = current_timestamp();
END//
DELIMITER ;