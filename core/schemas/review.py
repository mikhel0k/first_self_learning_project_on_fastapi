from datetime import datetime

from pydantic import BaseModel

from .base_schemas import BaseSchemaForDB


class ReviewBase(BaseModel):
    review: str
    review_date: datetime
    rating: int
    reviewer: str


class ReviewCreate(ReviewBase):
    book_id: int


class ReviewUpdate(BaseModel):
    review: str | None = None
    review_date: datetime | None = None
    rating: int | None = None
    reviewer: str | None = None


class ReviewSchema(ReviewBase, BaseSchemaForDB):
    book_id: int
