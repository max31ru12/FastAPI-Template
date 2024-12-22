from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import DB_URL

async_engine = create_async_engine(url=DB_URL, echo=True)
async_session = async_sessionmaker(bind=async_engine)


class Base(DeclarativeBase):
    pass
