from .author import AuthorSchema, AuthorCreate, AuthorUpdate, AuthorWithBooksSchema
from .book import BookSchema, BookCreate, BookUpdate
from .review import ReviewSchema, ReviewCreate, ReviewUpdate


__all__ = [
    'AuthorSchema',
    'AuthorCreate',
    'AuthorUpdate',
    'AuthorWithBooksSchema',
    'BookSchema',
    'BookCreate',
    'BookUpdate',
    'ReviewSchema',
    'ReviewCreate',
    'ReviewUpdate',
]