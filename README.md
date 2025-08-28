# HPE Work Experience Project 2026

Work in progress...

# Development Instructions

## To setup the database
1. Run ```make docker-compose``` to bring up the postgres container.

2. Run ``` make setup-db``` to create a facts table in the database and insert some sample data.

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
