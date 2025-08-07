from internal.domain.entities.fact import Fact

import psycopg2
import os

class RandomFactService:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "factsdb"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )

    def generate(self) -> str:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, fact FROM facts ORDER BY RANDOM() LIMIT 1;")
            result = cur.fetchone()
            if result:
                return Fact(id=result[0], fact=result[1])
            else:
                return Fact(id=None, fact="No facts found.")
