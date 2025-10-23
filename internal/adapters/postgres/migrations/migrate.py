import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "factsdb"),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "password"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", "5432")
)

with conn:
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE IF EXISTS facts;
            CREATE TABLE IF NOT EXISTS facts (
                id SERIAL PRIMARY KEY,
                fact TEXT NOT NULL,
                category TEXT NOT NULL
            );
        """)
        cur.execute("""
            INSERT INTO facts (fact, category) VALUES
            ('Honey never spoils.', 'food'),
            ('Bananas are berries.', 'food'),
            ('Octopuses have three hearts.', 'animal'),
            ('A group of flamingos is called a "flamboyance".', 'animal'),
            ('The Eiffel Tower can be 15 cm taller during hot days.', 'architecture')
            ON CONFLICT DO NOTHING;
        """)
    print("Migration complete: facts table created and sample data inserted.")

conn.close()
