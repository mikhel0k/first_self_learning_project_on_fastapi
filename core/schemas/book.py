from pydantic import BaseModel

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
