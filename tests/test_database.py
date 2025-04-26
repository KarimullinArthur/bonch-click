import pytest_asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from database import crud, Account, Base, engine


@pytest_asyncio.fixture(loop_scope="function", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
def mock_session_factory(mocker):
    # мок для session.begin() — async context manager
    begin_cm = MagicMock()
    begin_cm.__aenter__.return_value = AsyncMock()
    begin_cm.__aexit__.return_value = AsyncMock()

    # основной мок сессии
    mock_session = AsyncMock()

    # begin() → async context
    mock_session.begin.return_value = begin_cm

    # любой метод можно мокать дальше, например:
    mock_session.scalar.return_value = None
    mock_session.commit.return_value = None
    mock_session.add.return_value = None

    # session_factory() → async context, отдающий мок-сессию
    @asynccontextmanager
    async def fake_factory():
        yield mock_session

    # ❗ Заменить путь на тот, где используется session_factory
    mocker.patch("database.crud.session_factory", side_effect=fake_factory)

    return mock_session


@pytest.mark.asyncio
async def test_create_account(mock_session_factory):
    await crud.create_account(email="a@b.c", password="123")
    await mock_session.commit()
    mock_session_factory.add.assert_called_once()
    mock_session_factory.commit.assert_called_once()


@pytest.mark.asyncio(loop_scope="function")
async def test_get_account(mock_session_factory):
    mock_account = Account(email="test@example.com", password="secret")
    mock_session_factory.scalar.return_value = mock_account

    result = await crud.get_account(email="test@example.com")

    assert result == mock_account
    mock_session_factory.scalar.assert_called_once()


    mock_session_factory.commit.return_value = None
