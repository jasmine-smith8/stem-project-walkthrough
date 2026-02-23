# Task P0.1, P4.1

from fact import Fact
from .provider import PostgresConnectionProvider

def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute() # TODO: Write SQL query to select a random fact from the database
        # TODO: (Task P4.1) add the category column to the SQL query
        result = cur.fetchone()
        if result:
            return Fact() # TODO: Create and return a Fact object using the data from the database result
            # TODO: (Task P4.1) add the category information
        else:
            return Fact() # TODO: Create and return an empty Fact object if no result is found
