# REST API & CRUD Operations Worksheet
## APIs
**API** stands for **Application Programming Interface**. 

Think of it like a waiter in a restaurant:
- **You (the customer)** = Your application/website
- **The kitchen** = The database with all the information
- **The waiter** = The API

You tell the waiter what you want, the waiter goes to the kitchen, and brings back your food, but you never go into the kitchen yourself.
### Real-World API Examples:
- When you check the weather on your phone, it uses a weather API
- When you login with Google/Facebook on another website
- When you see a map on Uber or a food delivery app (Google Maps API)
## REST (Representational State Transfer)
**REST** is a set of rules for how APIs should work that uses standard HTTP methods like **GET, POST, PUT/PATCH, DELETE**: 
### Example REST URL Structure
```
https://api.bookstore.com/books          ← All books
https://api.bookstore.com/books/123      ← Book with ID 123
https://api.bookstore.com/authors        ← All authors
https://api.bookstore.com/authors/5      ← Author with ID 5
```
## CRUD
**CRUD** stands for the four basic operations you can do with data:

| CRUD Operation | What it does         | HTTP Method | Example                            |
| -------------- | -------------------- | ----------- | ---------------------------------- |
| **C**reate     | Add new data         | POST        | Add a new book to the library      |
| **R**ead       | Get/view data        | GET         | See all books or one specific book |
| **U**pdate     | Change existing data | PUT/PATCH   | Update a book's price              |
| **D**elete     | Remove data          | DELETE      | Remove a book from the library     |
## HTTP Methods
**GET** - used to read data
```
GET /books
→ Give me all the books

GET /books/123
→ Give me book number 123
```
**POST** - used to create data
```
POST /books
Body: { "title": "Harry Potter", "author": "J.K. Rowling", "price": 20 }
→ Create a new book with this information
```
**PUT/PATCH** - used to update data
```
PUT /books/123
Body: { "title": "Harry Potter", "author": "J.K. Rowling", "price": 25 }
→ Update book 123 with this new information

PATCH /books/123
Body: { "price": 25 }
→ Update only the price of book 123
```
**DELETE** - used to remove data
```
DELETE /books/123
→ Delete book number 123
```
## Tasks
### Exercise 1
Write the REST API URLs for these operations:
1. Get all books -> GET /books/
2. Get a specific book (ID: 42) GET /books/42
3. Add a new book POST /book/
4. Update book ID 42 PATCH /book/42
5. Delete book ID 42 DELETE /book/42
6. Get all books by a specific author GET /book/author
### Exercise 2
Match each action with the correct HTTP method:

| Action               | HTTP Method (GET/POST/PUT/DELETE) |
| -------------------- | --------------------------------- |
| View your profile    | GET____                           |
| Create a new account | POST___                           |
| Change your password | PATCH__                           |
| Delete your account  | DELETE_                           |
| Search for books     | GET____                           |
