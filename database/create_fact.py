# Tasks P1.1, P4.2

from fact import Fact
from .provider import PostgresConnectionProvider

# TODO: (Task P1.1) Add fact_test parameter
# TODO: (Task P4.2) Add category parameter
def create_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute() # TODO: (Tasks P1.1 & P4.2) Write SQL query to add new fact to the database
        # TODO: (Task P4.2) Add category to SQL query
        result = cur.fetchone()
        provider.commit()
        return Fact() # TODO: (Task P1.1) Create and return a Fact object using the data from the database result
        # TODO: (Task P4.2) Add category to returned fact