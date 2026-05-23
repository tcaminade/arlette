from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.postgres_dsn,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)