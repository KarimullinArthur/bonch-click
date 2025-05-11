from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Account(Base):
    __tablename__ = "account"

    email: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]

    def __repr__(self) -> str:
        return f"Address(email_address={self.email!r})"
