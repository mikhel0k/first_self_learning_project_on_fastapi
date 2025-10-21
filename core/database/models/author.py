from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association_tables import book_author_association_table
from .base_model import BaseModel


class Author(BaseModel):
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str | None] = mapped_column(String(50), nullable=True)
    age: Mapped[int] = mapped_column(Integer)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    country: Mapped[str | None] = mapped_column(String(30), nullable=True)
    birthday: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    isalive: Mapped[bool] = mapped_column(Boolean, default=True)

    books: Mapped[list["Book"]] = relationship(  # type: ignore
        secondary=book_author_association_table,
        back_populates="authors"
    )
