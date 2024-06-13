-- Creates a trigger that reduces the items quantity when a new order added
-- Creats a trigger that reduces the quantity column of the items table by the number value of the orders table new inserted row
DELIMITER $$ ;
CREATE TRIGGER new_order AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantity = (quantity-NEW.number) WHERE items.name=NEW.item_name;
END $$
DELIMITER ; $$
