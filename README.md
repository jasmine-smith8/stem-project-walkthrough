# HPE Work Experience Project 2026

## Project Overview

This is a web application that serves as an educational platform for HPE's STEM Work Experience program, which is run twice a year for local year 10-12 students in April and July. The project demonstrates full-stack development concepts through a fact management system where users can:

- **View random facts** from a pre-populated database of facts
- **Create and submit** their own facts to the database
- **Vote** on facts using a like/dislike system
- **Explore** different categories of interesting information

## Educational Purpose

The application is designed to teach work experience students:
- **Web development fundamentals** (HTML, CSS, JavaScript)
- **Backend development** with Python Flask
- **Database operations** using PostgreSQL and SQL
- **REST API concepts** and CRUD operations
- **Testing methodologies** using the Arrange-Act-Assert pattern
- **Project structure** demonstrating best practices

The codebase includes comprehensive worksheets and guides covering database concepts, REST APIs, and unit testing to provide hands-on learning experiences in modern software development practices.

# Development Instructions

## To setup the database
1. Run ```make docker-compose``` to bring up the postgres container.

2. Run ```make setup-db``` to create a facts table in the database and insert some sample data.

3. Run ```make db-shell``` to enter the database shell (useful for debugging purposes).


## To run the app

1. Create a virtual environment:

```python3 -m venv venv```

2. Activate the virtual environment:

```source venv/bin/activate```

3. Install dependencies:

```pip install -r requirements.txt```

4. Run the app:

```python app.py```
