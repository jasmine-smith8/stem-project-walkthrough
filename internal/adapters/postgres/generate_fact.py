import psycopg2
import os
from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class PostgresFactRepository(FactRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "factsdb"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )

# TASK
    def get_random_fact(self) -> Fact:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, fact, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;")
            result = cur.fetchone()
            if result:
                return Fact(id=result[0], fact=result[1], likes=result[2], dislikes=result[3])
            else:
                return Fact(id=None, fact="No facts found.", likes=0, dislikes=0)
# TASK
    def add_fact(self, fact_text: str) -> Fact:
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO facts (fact) VALUES (%s) RETURNING id, fact;",
                (fact_text,)
            )
            result = cur.fetchone()
            self.conn.commit()
            return Fact(id=result[0], fact=result[1])
        
    def get_likes_count(self, fact_id: int) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT likes FROM facts WHERE id = %s;",
                (fact_id,)
            )
            result = cur.fetchone()
            return result[0] if result else 0

    def get_dislikes_count(self, fact_id: int) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT dislikes FROM facts WHERE id = %s;",
                (fact_id,)
            )
            result = cur.fetchone()
            return result[0] if result else 0

    def get_fact_by_id(self, fact_id: int) -> Fact:
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT id, fact, likes, dislikes FROM facts WHERE id = %s;",
                (fact_id,)
            )
            result = cur.fetchone()
            if result:
                return Fact(id=result[0], fact=result[1], likes=result[2], dislikes=result[3])
            else:
                raise ValueError(f"Fact with id {fact_id} not found")
            
    def increment_likes(self, fact_id: int) -> None:
            with self.conn.cursor() as cur:
                cur.execute(
                    "UPDATE facts SET likes = likes + 1 WHERE id = %s;",
                    (fact_id,)
                )
                self.conn.commit()

    def increment_dislikes(self, fact_id: int) -> None:
            with self.conn.cursor() as cur:
                cur.execute(
                    "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;",
                    (fact_id,)
                )
                self.conn.commit()
