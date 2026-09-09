CREATE TABLE Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Author_Name VARCHAR(25)
    );


CREATE TABLE Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Book_Name VARCHAR(25),
    Author_id INT REFERENCES Authors(id) 
    );

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_Name VARCHAR(25),
    Email VARCHAR(40)
    );

CREATE TABLE Rents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Book_id INT REFERENCES Books(id),
    Customer_id INT REFERENCES Customers(id),
    State VARCHAR(20)
    );
