from sqlalchemy import select

from .database import SessionMaker
from .models import Account


def create_account(email: str, password: str):
    with SessionMaker() as session:
        new_account = Account(email=email, password=password)
        session.add(new_account)
        session.commit()  # DDL/DML в транзакции


def get_account(email: str) -> Account | None:
    with SessionMaker() as session:
        result = session.scalar(select(Account).where(Account.email == email))
        return result


def get_all_accounts() -> list[Account]:
    with SessionMaker() as session:
        result = session.scalars(select(Account)).all()
        return list(result)
