from typing import List

from pydantic import BaseModel

from . import AuthorSchema, ReviewSchema
from .base_schemas import BaseSchemaForDB


class BookBase(BaseModel):
    title: str
    year: int
    price: float
    description: str | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    year: int | None = None
    price: float | None = None
    description: str | None = None


class BookSchema(BookBase, BaseSchemaForDB):
    pass


class BookWithDetailsSchema(BookBase, BaseSchemaForDB):
    authors: List[AuthorSchema] = []
    reviews: List[ReviewSchema] = []
