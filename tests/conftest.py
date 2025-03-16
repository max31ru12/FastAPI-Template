from typing import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.database.setup_db import Base
from app.main import app

pytest_plugins = ("anyio",)

TEST_DB_URL = "postgresql+asyncpg://test:test@localhost:5432/test"


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="function")
async def client() -> AsyncClient:
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
def test_engine() -> AsyncEngine:
    return create_async_engine(TEST_DB_URL, echo=True)


@pytest.fixture(scope="session")
def async_session_maker(test_engine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=test_engine, expire_on_commit=False)


@pytest.fixture(scope="function")
async def session(async_session_maker) -> AsyncSession:
    async with async_session_maker() as session:
        yield session
        # Clear data after single test
        await session.rollback()


@pytest.fixture(scope="session", autouse=True)
async def setup_database(test_engine) -> AsyncIterator[None]:
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()
