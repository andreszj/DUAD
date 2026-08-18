SELECT books.Book_Name, authors.Author_Name
    FROM Books AS books
    INNER JOIN Authors AS authors
    ON books.Author_id = authors.id;

SELECT books.Book_Name, authors.Author_Name
    FROM Books AS books
    LEFT JOIN Authors AS authors
    ON books.Author_id = authors.id WHERE authors.Author_Name IS NULL;

SELECT authors.Author_Name, books.Book_Name
    FROM Authors AS authors
    LEFT JOIN Books AS books
    ON authors.id = books.Author_id  WHERE books.Book_Name IS NULL;

SELECT books.Book_Name
    FROM Books AS books
    INNER JOIN Rents as rents
    ON books.id = rents.Book_id GROUP BY books.Book_Name;

SELECT books.Book_Name
    FROM Books AS books
    LEFT JOIN Rents as rents
    ON books.id = rents.Book_id WHERE rents.Book_id IS NULL;

SELECT customer.Customer_Name
    FROM Customers AS customer
    LEFT JOIN Rents as rents
    ON customer.id = rents.Customer_id WHERE rents.Customer_id IS NULL;

SELECT books.Book_Name
    FROM Books AS books
    INNER JOIN Rents as rents
    ON books.id = rents.Book_id WHERE rents.State = "Overdue";