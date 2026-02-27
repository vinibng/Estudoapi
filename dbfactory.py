from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine ("postgresql://postgres:123@localhost:5432/postgres")
engine.connect()

with engine.connect() as conn:
    print(conn.execute(text("SELECT VERSION()")).fetchall())
