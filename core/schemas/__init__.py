from .author import AuthorSchema, AuthorCreate, AuthorUpdate, AuthorWithBooksSchema
from .book import BookSchema, BookCreate, BookUpdate, BookWithDetailsSchema
from .review import ReviewSchema, ReviewCreate, ReviewUpdate


AuthorWithBooksSchema.model_rebuild()
BookWithDetailsSchema.model_rebuild()


__all__ = [
    'AuthorSchema',
    'AuthorCreate',
    'AuthorUpdate',
    'AuthorWithBooksSchema',
    'BookSchema',
    'BookCreate',
    'BookUpdate',
    'BookWithDetailsSchema',
    'ReviewSchema',
    'ReviewCreate',
    'ReviewUpdate',
]