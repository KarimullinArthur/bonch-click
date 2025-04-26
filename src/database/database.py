from typing import Annotated
from datetime import datetime
from datetime import UTC

from sqlalchemy import URL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from config import settings


created_at = Annotated[datetime, mapped_column(default=datetime.now(UTC))]


def get_engine(url: URL | str = settings.database_url) -> AsyncEngine:
    return create_async_engine(
        url=url,
        echo=settings.debug,
        # pool_size=2
    )


def get_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


engine = get_engine()
sessionmaker = get_sessionmaker(engine)
session_factory = async_sessionmaker(engine)
Base = declarative_base()


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
