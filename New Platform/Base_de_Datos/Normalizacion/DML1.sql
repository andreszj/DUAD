-- SQLite
-- INSERT INTO customers_info (customer_name, customer_phone)
--     VALUES
--     ('Alice',1234567890),
--     ('Bob',9876543210),
--     ('Claire',5551234567);


-- INSERT INTO addresses (address, customer_id)
--     VALUES
--     ('123 Main St',1),
--     ('456 Elm St',2),
--     ('4th Avenue',2),
--     ('789 Oak St',3),
--     ('464 Georgia St',3);

-- INSERT INTO items (item_code,item_name,price)
--     VALUES
--     (101,'Cheeseburger',8),
--     (102,'Fries',3),
--     (103,'Pizza',12),
--     (105,'Salad',6),
--     (106,'Water',1);

-- INSERT INTO special_requests (request)
--     VALUES
--     ('No onions'),
--     ('Extra ketchup'),
--     ('Extra cheese'),
--     ('None'),
--     ('No croutons');

INSERT INTO orders (order_number,address_id,delivery_time)
    VALUES
    (1,1,'2026-06-19 18:00:00'),
    (2,2,'2026-06-19 19:30:00'),
    (2,3,'2026-06-19 19:30:00'),
    (3,4,'2026-06-19 12:00:00'),
    (4,5,'2026-06-19 17:00:00');

-- INSERT INTO order_item (order_id,item_id,quantity,request_id)
--     VALUES 
--     (1,1,2,1),
--     (1,2,1,2),
--     (2,3,1,3),
--     (3,2,2,4),
--     (4,4,1,5),
--     (5,5,1,4);
    