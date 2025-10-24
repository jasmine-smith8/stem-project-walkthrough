from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository
from .provider import PostgresConnectionProvider

class PostgresFactRepository(FactRepository):
    def __init__(self, provider: PostgresConnectionProvider | None = None):
        self.provider = provider or PostgresConnectionProvider()

# TASK
    def vote_fact(self, fact_id: int, vote_type: str) -> Fact:
        with self.provider.cursor() as cur:
            if vote_type == "like":
                cur.execute(
                    "UPDATE facts SET likes = likes + 1 WHERE id = %s;",
                    (fact_id,)
                )
            elif vote_type == "dislike":
                cur.execute(
                    "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;",
                    (fact_id,)
                )
            else:
                raise ValueError("Invalid vote type")

            cur.execute(
                "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = %s;",
                (fact_id,)
            )
            result = cur.fetchone()
            self.provider.commit()
            if result:
                return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4])
            else:
                raise ValueError("Fact not found")