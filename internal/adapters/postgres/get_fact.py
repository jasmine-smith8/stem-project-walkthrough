from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository
from .provider import PostgresConnectionProvider

class PostgresFactRepository(FactRepository):
    def __init__(self, provider: PostgresConnectionProvider | None = None):
        self.provider = provider or PostgresConnectionProvider()

# TASK
    def get_fact(self) -> Fact:
        with self.provider.cursor() as cur:
            cur.execute("SELECT id, fact, category FROM facts ORDER BY RANDOM() LIMIT 1;")
            result = cur.fetchone()
            if result:
                return Fact(id=result[0], fact=result[1], category=result[2])
            else:
                return Fact(id=None, fact="No facts found.", category="none")