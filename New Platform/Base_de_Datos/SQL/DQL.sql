-- SQLite
SELECT *
FROM Products;

SELECT * 
FROM Products
WHERE Price >50000;

-- SELECT *
-- FROM Invoices
-- WHERE id = (SELECT Invoice_id FROM Product_Invoice WHERE Product_Invoice.Product_id =1);

SELECT * 
FROM Invoices
WHERE id IN (SELECT Invoice_id 
FROM Product_Invoice
WHERE Product_id =1
);

-- IN devuelve varias lineas de la consulta 

SELECT id, Product_id, SUM(Quantity), Total_Amount, SUM(Total_Amount)
FROM Product_Invoice
GROUP BY Product_id;

SELECT *
FROM Invoices
WHERE Buyer_Email = 'bn@gmail.com';

SELECT *
FROM Invoices
ORDER BY Total_Amount DESC;

SELECT *
FROM Invoices
WHERE Invoice_Number = 10001;

