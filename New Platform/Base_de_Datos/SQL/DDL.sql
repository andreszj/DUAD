-- SQLite

-- CREATE TABLE Products (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Code VARCHAR(5) NOT NULL,
-- Name VARCHAR(25) NOT NULL,
-- Price FLOAT NOT NULL DEFAULT 0,
-- Entry_date DATE NOT NULL,
-- Brand VARCHAR(25) NOT NULL,
-- Stock INT NOT NULL DEFAULT 0
-- );


-- CREATE TABLE Shopping_Carts (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Buyer_Email VARCHAR(254) NOT NULL
-- );

-- CREATE TABLE Invoices (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Invoice_Number INT NOT NULL,
-- Purchase_date DATE NOT NULL,
-- Buyer_Email VARCHAR(254) NOT NULL,
-- Total_Amount FLOAT NOT NULL DEFAULT 0
-- );

-- CREATE TABLE Product_Cart (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Product_id INT REFERENCES Products(id),
-- Shopping_Cart_id INT REFERENCES Shopping_Carts(id)
-- );

-- CREATE TABLE Product_Invoice (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Invoice_id INT REFERENCES Invoices(id),
-- Product_id INT REFERENCES Products(id),
-- Quantity INT NOT NULL DEFAULT 0,
-- Total_Amount FLOAT NOT NULL DEFAULT 0
-- );

-- ALTER TABLE Invoices 
-- ADD Phone BIGINT NOT NULL DEFAULT 0;

-- CREATE TABLE Cashiers (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Name VARCHAR(25) NOT NULL
-- );

-- ALTER TABLE Invoices
-- ADD Cashier_id INT REFERENCES Cashiers(id);

