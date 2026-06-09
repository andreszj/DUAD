-- SQLite
-- INSERT INTO Cashiers (Name)
-- VALUES ('Pedro');
-- INSERT INTO Cashiers (Name)
-- VALUES ('Juan');

-- INSERT INTO Products (Code, Name, Price, Entry_date, Brand, Stock)
-- VALUES ('SKU01', 'SMARPHONE', 100.0, '2026-05-30', 'APPLE', 5);

-- INSERT INTO Products (Code, Name, Price, Entry_date, Brand, Stock)
-- VALUES ('SKU02', 'RADIO', 10000.0, '2026-05-31', 'PP', 2);


-- INSERT INTO Products (Code, Name, Price, Entry_date, Brand, Stock)
-- VALUES ('SKU03', 'SMART TV', 120000.0, '2026-05-31', 'SONY', 10);


-- INSERT INTO Products (Code, Name, Price, Entry_date, Brand, Stock)
-- VALUES ('SKU04', 'MICROWAVE', 52000.0, '2026-05-29', 'SAMSUNG', 10);

-- INSERT INTO Shopping_Carts (Buyer_Email)
-- VALUES ('cazuniga02@gmail,com');

-- INSERT INTO Shopping_Carts (Buyer_Email)
-- VALUES ('pedro@gmail,com');

-- INSERT INTO Shopping_Carts (Buyer_Email)
-- VALUES ('juan@gmail,com');

-- INSERT INTO Invoices (Invoice_Number, Purchase_date, Buyer_Email, Phone, Cashier_id)
-- VALUES (10001, '2026-05-31', 'bryan@gmail.com', 89961318, 1)

-- INSERT INTO Invoices (Invoice_Number, Purchase_date, Buyer_Email, Phone, Cashier_id)
-- VALUES (10002, '2026-05-30', 'bn@gmail.com', 88888888, 2)

-- INSERT INTO Product_Invoice (Invoice_id, Product_id, Quantity)
-- VALUES (1,1,1)

-- INSERT INTO Product_Invoice (Invoice_id, Product_id, Quantity)
-- VALUES (2,2,1)

-- INSERT INTO Product_Invoice (Invoice_id, Product_id, Quantity)
-- VALUES (2,1,1)

UPDATE Product_Invoice SET

    Total_Amount = (SELECT Price FROM Products WHERE Products.id = Product_Invoice.Product_id)*Quantity;

UPDATE Invoices SET
    Total_Amount = (SELECT SUM(Total_Amount) FROM Product_Invoice WHERE Product_Invoice.Invoice_id = Invoices.id);