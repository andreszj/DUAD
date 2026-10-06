
CREATE SCHEMA IF NOT EXISTS "Transactions";

DROP TABLE IF EXISTS "Transactions".bill_products;
DROP TABLE IF EXISTS "Transactions".products;
DROP TABLE IF EXISTS "Transactions".bills;
DROP TABLE IF EXISTS "Transactions".users;


CREATE TABLE IF NOT EXISTS "Transactions".users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(35) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(30) NOT NULL,
    address VARCHAR(200) NOT NULL
);


CREATE TABLE IF NOT EXISTS "Transactions".products (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(50) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    qty INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "Transactions".bills (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "Transactions".users(id),
    date DATE NOT NULL DEFAULT CURRENT_DATE,
	total NUMERIC (10,2),
	status VARCHAR(25) NOT NULL
);


CREATE TABLE IF NOT EXISTS "Transactions".bill_products (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bill_id INTEGER NOT NULL REFERENCES "Transactions".bills(id),
	product_id INTEGER NOT NULL REFERENCES "Transactions".products(id),
    qty INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,

    UNIQUE (bill_id, product_id)
);


-- DATOS DE PRUEBA

INSERT INTO "Transactions".users (name, email, phone, address)
VALUES
    ('Carlos Rodríguez', 'carlos@gmail.com', '8888-1111', 'San José, Costa Rica'),
    ('María Fernández', 'maria@gmail.com', '8888-2222', 'Heredia, Costa Rica'),
    ('José Ramírez', 'jose@gmail.com', '8888-3333', 'Alajuela, Costa Rica'),
    ('Ana González', 'ana@gmail.com', '8888-4444', 'Cartago, Costa Rica');


INSERT INTO "Transactions".products (description, price, qty)
VALUES
    ('Laptop Lenovo ThinkPad',       850.00, 10),
    ('Monitor Samsung 27 pulgadas',  280.00, 15),
    ('Teclado Logitech MX Keys',     120.00, 20),
    ('Mouse Logitech MX Master 3S',   95.00, 25),
    ('Audifonos Sony WH-1000XM5',    350.00, 12),
    ('SSD Samsung 1TB',              110.00, 30),
    ('Memoria RAM Kingston 16GB',     75.00, 40),
    ('Webcam Logitech C920',          90.00, 18),
    ('iPad Air',                     650.00,  8),
    ('Samsung Galaxy S25',           900.00,  6);


INSERT INTO "Transactions".bills (user_id, date, total, status)
VALUES
    (1, '2026-09-10', 1040.00, 'PENDING'),
    (2, '2026-09-15',  620.00, 'PENDING'),
    (3, '2026-09-20',  890.00, 'PENDING');


INSERT INTO "Transactions".bill_products (bill_id, product_id, qty, unit_price)
VALUES
    (1, 1, 1, 850.00),  
    (1, 4, 2,  95.00),  
    (2, 2, 1, 280.00),  
    (2, 3, 1, 120.00),  
    (2, 6, 2, 110.00),  
    (3, 9, 1, 650.00),  
    (3, 8, 1,  90.00),  
    (3, 7, 2,  75.00);  