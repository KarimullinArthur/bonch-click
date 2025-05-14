import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from mocks.database import mock_session

from api.main import app
from common.database.models import Account


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        base_url="http://test",
        transport=ASGITransport(app=app)
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_account(client, mock_session):
    resp = await client.get("accounts", params={"email": "test@test.com"})
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_create_account(client, mock_session):
    resp = await client.post(
        "accounts", params={"email": "test@test.com", "password": "password"}
    )
    assert resp.status_code == 201


@pytest.mark.asyncio
async def test_update_account(client, mock_session):
    mock_account = Account(email="test@test.com", password="oldpass")
    mock_session.scalar.return_value = mock_account

    resp = await client.patch(
        "accounts",
        params={
            "email": "test@test.com",
            "new_password": "321",
        },
    )
    assert resp.status_code == 204
    assert mock_account.password == "321"


@pytest.mark.asyncio
async def test_update_nonexitent_account(client, mock_session):
    mock_session.scalar.return_value = None

    resp = await client.patch(
        "accounts",
        params={
            "email": "test@test.com",
            "new_password": "321",
        },
    )
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_delete_account(client, mock_session):
    resp = await client.delete("accounts", params={"email": "test@test.com"})
    assert resp.status_code == 200
