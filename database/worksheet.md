# Database/SQL Worksheet

## What is a database?

A database is an organised collection of structured information, or data, stored electronically in a computer system.

## Key Terminology

**Schema**: The blueprint/structure of the database, which defines how data is organised including tables, columns, and the relationships between them.  

**Table**: Fundamental structure for organising data into rows and columns.

**Column (attribute)**: A single piece of data within a table, representing a specific quality/trait of the entity e.g. Name, Email, Colour, Category.

**Row (record)**: A single entry/data item in a table containing all the information for a specific instance e.g. one customer’s details.

**Query**: A request for information from the database.
 
## SQL (Structured Query Language)

SQL is a programming language used for managing and manipulating databases. It can be used to add, modify, query and delete data in a database, as well as managing the structure and security. 

### SQL Basics

Visit https://www.w3schools.com/sql/default.asp to explore the basics of SQL (hint: use the navigation menu on the left hand side to look at descriptions, syntax and examples of specific statements).

## Tasks

Using the following example ‘Customers’ table in the database
 

![Customers Table](../worksheet_images/customers_table.png)

Write queries to:

1)	Select all columns from the ‘Customers’ table
SELECT * FROM Customers

2)	Select the CustomerID, City and Country from the ‘Customers’ table
SELECT CustomerID, City, Country FROM Customers

3)	Select all columns from the ‘Customers’ table, in alphabetical order of CustomerName
SELECT * FROM Customers ORDER BY CustomerName;

4)	Select the CustomerName from the ‘Customers’ table, returning only the first 3 rows
SELECT TOP 3 * FROM Customers ORDER BY CustomerName;

5)	Add a new row to the ‘Customers’ table, using whatever example data you like
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) Values ('Harvey Scott', 'Mike Wazowski', 'Pearson Scott', 'New York', 12345, 'USA');

6)	Update Antonio’s PostalCode to ‘05024’
UPDATE Customers SET PostalCode = 05024 WHERE CustomerID = 3

7)	Delete the row with CustomerID ‘2’  from the ‘Customers’ table
DELETE FROM Customers WHERE CustomerID = 2

## Hint: 

For your random fact generation to work, you will need to include these statements:

- ORDER BY RANDOM() - pick a fact from the database at random
- LIMIT 1 - limit to one fact at a time
