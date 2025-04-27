from datetime import UTC, datetime
from typing import Annotated

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, mapped_column, sessionmaker

from config import settings

created_at = Annotated[datetime, mapped_column(default=lambda: datetime.now(UTC))]


def get_engine(url: URL | str = settings.database_url):
    return create_engine(
        url,
        echo=settings.debug,
        # pool_size=2  # если нужно ограничить пул
    )


def get_sessionmaker(engine):
    return sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )


engine = get_engine()
SessionMaker = get_sessionmaker(engine)
Base = declarative_base()


def create_table():
    # DDL-операции автокоммитятся, сессия не обязательна
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы.")


def drop_table():
    Base.metadata.drop_all(bind=engine)
    print("Таблицы удалены.")


def init_models():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Модели и таблицы инициализированы.")
