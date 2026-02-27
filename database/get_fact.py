# Task P0.1, P3.1, P4.1

from fact import Fact
from .provider import PostgresConnectionProvider

def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        # TODO: Write SQL query to select a random fact from the database
        # TODO: (Task P3.1) Add the likes and dislikes counts to the SQL query
        # TODO: (Task P4.1) add the category column to the SQL query
        cur.execute()
        result = cur.fetchone()
        if result:
            # TODO: Create and return a Fact object using the data from the database result
            # TODO: (Task P3.1) Add the likes and dislikes counts to the Fact object
            # TODO: (Task P4.1) add the category information
            return Fact()
        else:
            return Fact() # TODO: Create and return an empty Fact object if no result is found
