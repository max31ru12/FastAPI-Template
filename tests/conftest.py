from typing import AsyncIterator, Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.main import app
from app.models import Base

pytest_plugins = ("anyio",)

TEST_DB_URL = "postgresql+asyncpg://test:test@localhost:5432/test"


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="function")
def client() -> TestClient:
    with TestClient(app) as _client:
        yield _client


@pytest.fixture(scope="session")
def test_engine() -> AsyncEngine:
    return create_async_engine(TEST_DB_URL, echo=True)


@pytest.fixture(scope="session")
def async_session_maker(test_engine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=test_engine, expire_on_commit=False)


@pytest.fixture(scope="function")
async def session(async_session_maker) -> Iterator[AsyncSession]:
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
