from fact import Fact
from .provider import PostgresConnectionProvider

def create_fact(fact_text: str, category: str) -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute(
            "INSERT INTO facts (fact, category) VALUES (%s, %s) RETURNING id, fact, category, likes, dislikes;",
            (fact_text, category)
        )
        result = cur.fetchone()
        provider.commit()
        return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3] or 0, dislikes=result[4] or 0)