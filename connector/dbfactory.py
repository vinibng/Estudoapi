from functools import lru_cache
from sqlalchemy import create_engine

@lru_cache
def get_database_engine():
    return create_engine("postgresql+psycopg2://root:password@localhost:5432/MagicCard")