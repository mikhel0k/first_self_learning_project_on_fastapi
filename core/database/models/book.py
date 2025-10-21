from sqlalchemy import String, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association_tables import book_author_association_table
from .base_model import BaseModel


class Book(BaseModel):
    title: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)

    reviews: Mapped[list["Review"]] = relationship(back_populates="book")  # type: ignore
    authors: Mapped[list["Author"]] = relationship(  # type: ignore
        secondary=book_author_association_table,
        back_populates="books"
    )
