from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import DB_URL, DEV_MODE

async_engine: AsyncEngine = create_async_engine(
    url=DB_URL,
    echo=DEV_MODE,
    pool_size=10,
    max_overflow=20,
)
session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# геттер нужен для использования в FastAPI зависимостях, yield используется для того,
# чтобы после завершения работы с сессией пошло выполнение дальше yield и вызвался метод
# __aexit__ асинхронного контекстного менеджера
async def session_getter() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
