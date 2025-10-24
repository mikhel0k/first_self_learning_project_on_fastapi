from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.database import Book, Author
from core.schemas import BookSchema, BookCreate, BookUpdate, BookWithDetailsSchema
from ..dependencies import get_item_by_id


class BookCRUD:
    def __init__(self):
        self.get_item_by_id = get_item_by_id(Book)
        self.get_author_by_id = get_item_by_id(Author)

    async def get_all_books(
            self,
            session: AsyncSession
    ) -> List[BookSchema]:
        stmt = select(Book).order_by(Book.id)
        result = await session.execute(stmt)
        books = result.scalars().all()

        return [BookSchema.model_validate(book) for book in books]

    async def get_book_by_id(
            self,
            session: AsyncSession,
            book_id: int,
    ) -> BookSchema:
        result = await self.get_item_by_id(book_id, session)
        return BookSchema.model_validate(result)

    async def get_book_with_info(
            self,
            session: AsyncSession,
            book_id: int
    ) -> BookWithDetailsSchema:
        stmt = select(Book).options(
            selectinload(Book.authors),
            selectinload(Book.reviews)
        ).where(Book.id == book_id)
        result = await session.execute(stmt)
        book = result.scalar_one_or_none()

        if not book:
            raise HTTPException(
                status_code=404,
                detail=f"Book with {book_id} is does not found"
            )
        return BookWithDetailsSchema.model_validate(book)

    async def create_book(
            self,
            session: AsyncSession,
            created_book: BookCreate
    ) -> BookSchema:
        book = Book(**created_book.dict())

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return BookSchema.model_validate(book)

    async def update_book(
            self,
            session: AsyncSession,
            book_id: int,
            updated_book: BookUpdate,
    ) -> BookSchema:
        book = await self.get_item_by_id(book_id, session)

        updated_book = updated_book.model_dump(exclude_unset=True)
        for key, value in updated_book.items():
            setattr(book, key, value)

        await session.commit()
        await session.refresh(book)
        return BookSchema.model_validate(book)

    async def delete_book(
            self,
            book_id: int,
            session: AsyncSession,
    ) -> None:
        book = await self.get_item_by_id(book_id, session)
        await session.delete(book)
        await session.commit()

    async def add_author_to_book(
            self,
            session: AsyncSession,
            author_id: int,
            book_id: int,
    ) -> BookWithDetailsSchema:
        stmt = select(Book).options(selectinload(Book.authors)).where(Book.id == book_id)
        result = await session.execute(stmt)
        book = result.scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=400,
                detail=f"Book with id {book_id} does not exist"
            )

        author = await self.get_author_by_id(author_id, session)

        if author in book.authors:
            raise HTTPException(
                status_code=400,
                detail="Author already added to this book",
            )

        book.authors.append(author)
        await session.commit()

        return await self.get_book_with_info(session, book_id)

    async def delete_author_from_book(
            self,
            session: AsyncSession,
            author_id: int,
            book_id: int,
    ) -> None:
        stmt = select(Book).options(selectinload(Book.authors)).where(Book.id == book_id)
        result = await session.execute(stmt)
        book = result.scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=400,
                detail=f"Book with id {book_id} does not exist"
            )

        author = await self.get_author_by_id(author_id, session)

        if author not in book.authors:
            raise HTTPException(
                status_code=400,
                detail="Author not in this book"
            )

        book.authors.remove(author)
        await session.commit()


bookCRUD = BookCRUD()