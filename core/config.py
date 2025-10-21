from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = False


settings = Settings()
