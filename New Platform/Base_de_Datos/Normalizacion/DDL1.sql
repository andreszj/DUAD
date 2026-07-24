-- SQLite
-- CREATE TABLE customers_info (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     customer_name VARCHAR(25) NOT NULL,
--     customer_phone BIGINT NOT NULL DEFAULT 0
--     );



-- DROP TABLE customers_info;

CREATE TABLE customers_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(25) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL
    );

-- TABLE customers_info - 1FN: I used 1FN because the table needs its own PK, and each record contains unique, individual data


CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR(30) NOT NULL,
    customer_id INT REFERENCES customers_info(id)
    );

-- TABLE addresses - 3NF: I used 3FN because the table has its own PK, and each record contains FKS that reference related data in customers_info Table

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_code SMALLINT NOT NULL,
    item_name VARCHAR(20) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0
    );

-- TABLE items - 3FN: I used 3NF because all attributes depend only on the primary key, eliminating redundancy

CREATE TABLE special_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request VARCHAR(20) NOT NULL
    );

-- TABLE special_requests - 1NF: I used 1FN because the table has its own PK, and I standardized the format of special requests to avoid inconsistent data

-- DROP TABLE orders;

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_number INT NOT NULL,
    address_id INT REFERENCES addresses(id),
    delivery_time TIMESTAMP NOT NULL
    );

-- TABLE orders - 3NF: I used 3FN because the table has its own PK, and each record contains FKs that reference related data in the addresses table

CREATE TABLE order_item(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT REFERENCES orders(id),
    item_id INT REFERENCES items(id),
    quantity SMALLINT NOT NULL DEFAULT 0,
    request_id INT REFERENCES special_requests(id)
    );

-- TABLE order_item - 2NF and 3NF: I used 2NF by referencing special_requests with a FK. I used 3NF because the table references related data through FK, reducing redundancy.


