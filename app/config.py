from os import getenv

from dotenv import load_dotenv

load_dotenv()

DEV_MODE: bool = getenv("DEV_MODE", "true") == "true"

DB_HOST: str = getenv("DB_HOST", default="postgres")
DB_PORT: str = getenv("DB_PORT", default="5432")
DB_PASSWORD: str = getenv("DB_PASSWORD", default="test")
DB_USER: str = getenv("DB_USER", default="test")
DB_NAME: str = getenv("DB_NAME", default="test")

DB_URL: str = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
