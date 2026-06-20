-- SQLite
CREATE TABLE customers_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(25) NOT NULL,
    customer_phone BIGINT NOT NULL DEFAULT 0
    );

CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR(30) NOT NULL,
    customer_id INT REFERENCES customers_info(id)
    );

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_code SMALLINT NOT NULL,
    item_name VARCHAR(20) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0
    );

CREATE TABLE special_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request VARCHAR(20) NOT NULL
    );

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_number INT NOT NULL,
    customer_id INT REFERENCES customers_info(id),
    address_id INT REFERENCES addresses(id),
    delivery_time TIMESTAMP NOT NULL
    );

CREATE TABLE order_item(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT REFERENCES orders(id),
    item_id INT REFERENCES items(id),
    quantity SMALLINT NOT NULL DEFAULT 0,
    request_id INT REFERENCES special_requests(id)
    );




