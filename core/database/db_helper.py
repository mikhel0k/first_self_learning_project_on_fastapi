from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from core.config import Settings


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(
            url=Settings.db_url,
            echo=Settings.db_echo,
        )
        self.session_fabrik = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )
