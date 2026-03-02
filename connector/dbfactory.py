from functools import lru_cache
from sqlalchemy import create_engine

@lru_cache
def get_database_engine():
    return create_engine("postgresql://postgres:123@localhost:5432/postgres")