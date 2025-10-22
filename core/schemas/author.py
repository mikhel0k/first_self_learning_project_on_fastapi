from datetime import datetime

from pydantic import BaseModel

from .base_schemas import BaseSchemaForDB


class AuthorBase(BaseModel):
    name: str
    surname: str | None = None
    age: int
    bio: str | None = None
    country: str | None = None
    birthday: datetime | None = None
    isalive: bool = True


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: str | None = None
    surname: str | None = None
    age: int | None = None
    bio: str | None = None
    country: str | None = None
    birthday: datetime | None = None
    isalive: bool | None = None


class Author(AuthorBase, BaseSchemaForDB):
    pass
