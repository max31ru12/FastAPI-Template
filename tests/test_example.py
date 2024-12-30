import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

pytestmark = pytest.mark.anyio


async def test_database_setup(session: AsyncSession):
    result = await session.execute(text("SELECT 1"))
    assert result.scalar() == 1


def test_client_request(client):
    response = client.get("/")
    assert response.status_code == 200
