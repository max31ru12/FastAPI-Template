import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

pytestmark = pytest.mark.anyio


async def test_database_setup(session: AsyncSession):
    result = await session.execute(text("SELECT 1"))
    assert result.scalar() == 1


async def test_client_request(client):
    response = await client.get("/")
    assert response.status_code == 200
