import pytest
from httpx import ASGITransport, AsyncClient

from api.main import app


@pytest.mark.asyncio
async def test_get_account():
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as client:
        resp = await client.get("accounts", params={"email": "test@test.com"})
        assert resp.status_code == 200


@pytest.mark.asyncio
async def test_create_account():
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as client:
        resp = await client.post(
            "accounts", params={"email": "test@test.com", "password": "password"}
        )
        assert resp.status_code == 201
