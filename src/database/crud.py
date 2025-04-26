from sqlalchemy import select

from .database import session_factory
from .models import Account

async def create_account(*args, email: str, password: str):
    async with session_factory() as session:
        async with session.begin():
            new_account = Account(email=email, password=password)
            session.add(new_account)
            await session.commit()

async def get_account(*args, email: str) -> Account | None:
    async with session_factory() as session:
        result = await session.scalar(
            select(Account).where(Account.email == email)
        )
        return result
