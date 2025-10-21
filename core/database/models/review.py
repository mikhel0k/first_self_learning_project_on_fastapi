from datetime import datetime

from sqlalchemy import Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Review(BaseModel):
    review: Mapped[str] = mapped_column(Text)
    review_date: Mapped[datetime] = mapped_column(DateTime)
    rating: Mapped[int] = mapped_column(Integer)
    reviewer: Mapped[str] = mapped_column(String(100))

    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    book: Mapped["Book"] = relationship(back_populates="reviews")  # type: ignore
