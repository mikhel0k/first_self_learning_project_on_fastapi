from sqlalchemy import String, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association_tables import book_author_association_table
from .base_model import BaseModel


class Book(BaseModel):
    title: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    reviews: Mapped[list["Review"]] = relationship(back_populates="book.py")  # type: ignore
    authors: Mapped[list["Author"]] = relationship(  # type: ignore
        secondary=book_author_association_table,
        back_populates="books"
    )
