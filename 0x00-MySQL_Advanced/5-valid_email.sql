-- Creates a trigger that resets the email validation if it has been updated
-- Creats a trigger that resets valid_email field if an email has been updated
DELIMITER $$ ;
CREATE TRIGGER new_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF OLD.email != NEW.email
THEN
	SET NEW.valid_email=0;
END IF;
END $$
DELIMITER ; $$
