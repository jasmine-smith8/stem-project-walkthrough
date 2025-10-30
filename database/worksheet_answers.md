# Database/SQL Worksheet Answers

1)	Select all columns from the ‘Customers’ table

    **SELECT * FROM Customers;**


2)	Select the CustomerID, City and Country from the ‘Customers’ table

    **SELECT CustomerID, City, Country FROM Customers;**


3)	Select all columns from the ‘Customers’ table, in alphabetical order of CustomerName

    **SELECT * FROM Customers ORDER BY CustomerName ASC;**


4)	Select the CustomerName from the ‘Customers’ table, returning only the first 3 rows

    **SELECT CustomerName FROM Customers LIMIT 3;**


5)	Add a new row to the ‘Customers’ table, using whatever example data you like

    **INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (6, ‘Christopher Smith’, ‘Chris Smith’, ’24 Hill Road’, ‘Bristol’, ‘BS34555’, ‘England’);**


6)	Update Antonio’s PostalCode to ‘05024’

    **UPDATE Customers SET PostalCode = 05024 WHERE CustomerId = 1**


7)	Delete the row with CustomerID ‘2’  from the ‘Customers’ table

    **DELETE FROM Customers WHERE CustomerID = 2;**
