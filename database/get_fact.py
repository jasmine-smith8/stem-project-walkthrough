from fact import Fact
from .provider import PostgresConnectionProvider

def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;")
        result = cur.fetchone()
        if result:
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4])
        else:
            return Fact(id=None, fact="No facts found.", category="none", likes=0, dislikes=0)
