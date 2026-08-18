INSERT INTO Authors (Author_Name)
    VALUES
    ("Miguel de Cervantes"),
    ("Dante Alighieri"),
    ("Takehiko Inoue"),
    ("Akira Toriyama"),
    ("Walt Disney");

INSERT INTO Books (Book_Name,Author_id)
    VALUES
    ("Don Quijote",1),
    ("La Divina Comedia",2),
    ("Vagabond 1-3",3),
    ("Dragon Ball 1",4);

INSERT INTO Books (Book_Name)
    VALUES
    ("The Book of the 5 Rings");

INSERT INTO Customers (Customer_Name, Email)
    VALUES
    ("John Doe","j.doe@email.com"),
    ("Jane Doe","jane@doe.com"),
    ("Luke Skywalker","darth.son@email.com");

INSERT INTO Rents (Book_id, Customer_id, State)
    VALUES
    (1,2,"Returned"),
    (2,2,"Returned"),
    (1,1,"On time"),
    (3,1,"On time"),
    (2,2,"Overdue");