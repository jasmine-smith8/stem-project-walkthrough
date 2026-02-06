# Task P0.1

# Import necessary modules

def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute() # Write SQL query to select a random fact from the database
        result = cur.fetchone()
        if result:
            return Fact() # Create and return a Fact object using the data from the database result
        else:
            return Fact() # Create and return an empty Fact object if no result is found
