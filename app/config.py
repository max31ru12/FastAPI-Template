from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

DEV_MODE: bool = getenv("DEV_MODE", "true").strip().lower() in {"true", "1", "yes"}

BASE_DIR = Path(__file__).parent.parent

CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Settings(BaseSettings):

    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_PASSWORD: str = "test"
    DB_USER: str = "test"
    DB_NAME: str = "test"

    class ConfigDict:
        env: Path = BASE_DIR / ".env"


settings = Settings()

DB_URL: str = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
