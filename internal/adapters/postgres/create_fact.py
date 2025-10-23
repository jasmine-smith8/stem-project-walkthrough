from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository
from .provider import PostgresConnectionProvider

class PostgresFactRepository(FactRepository):
    def __init__(self, provider: PostgresConnectionProvider | None = None):
        self.provider = provider or PostgresConnectionProvider()

# TASK
    def create_fact(self, fact_text: str, category: str) -> Fact:
        with self.provider.cursor() as cur:
            cur.execute(
                "INSERT INTO facts (fact, category) VALUES (%s, %s) RETURNING id, fact, category;",
                (fact_text, category)
            )
            result = cur.fetchone()
            self.provider.commit()
            return Fact(id=result[0], fact=result[1], category=result[2])