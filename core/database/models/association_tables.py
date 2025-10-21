from .base_model import BaseModel
from sqlalchemy import Table, Column, ForeignKey

book_author_association_table = Table(
    'book_author_association_table',
    BaseModel.metadata,
    Column('book_id', ForeignKey("books.id"), primary_key=True),
    Column('author_id', ForeignKey("authors.id"), primary_key=True),
)
