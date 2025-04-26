from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email!r})"
