from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core import db_helper
from core.api.v1.books.crud import bookCRUD
from core.schemas import BookSchema, BookCreate, BookUpdate, BookWithDetailsSchema

router = APIRouter(prefix="/books", tags=["books"])

@router.get(
    "/",
    response_model=List[BookSchema]
)
async def get_all_books(
        session: AsyncSession = Depends(db_helper.get_session)
) -> List[BookSchema]:
    books = await bookCRUD.get_all_books(
        session=session,
    )
    return books

@router.get(
    "/{book_id}/",
    response_model=BookSchema
)
async def get_book_by(
        book_id: int,
        session: AsyncSession = Depends(db_helper.get_session)
) -> BookSchema:
    book = await bookCRUD.get_book_by_id(
        session=session,
        book_id=book_id
    )
    return book

@router.get(
    "/{book_id}/with_info",
    response_model=BookWithDetailsSchema,
)
async def get_book_with_info(
        book_id: int,
        session: AsyncSession = Depends(db_helper.get_session)
) -> BookWithDetailsSchema:
    book = await bookCRUD.get_book_with_info(
        book_id=book_id,
        session=session
    )
    return book

@router.post(
    "/",
    response_model=BookSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_book(
        created_book: BookCreate,
        session: AsyncSession = Depends(db_helper.get_session),
) -> BookSchema:
    book = await bookCRUD.create_book(
        created_book=created_book,
        session=session,
    )
    return book

@router.patch(
    "/{book_id}/",
    response_model=BookSchema,
)
async def update_book(
        book_id: int,
        updated_book: BookUpdate,
        session: AsyncSession = Depends(db_helper.get_session)
) -> BookSchema:
    book = await bookCRUD.update_book(
        book_id=book_id,
        updated_book=updated_book,
        session=session,
    )
    return book

@router.delete(
    "/{book_id}/",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(
        book_id: int,
        session: AsyncSession = Depends(db_helper.get_session),
) -> None:
    await bookCRUD.delete_book(
        book_id=book_id,
        session=session,
    )

@router.post(
    "/{book_id}/author/{author_id}",
    response_model=BookWithDetailsSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_book_author(
        book_id: int,
        author_id: int,
        session: AsyncSession = Depends(db_helper.get_session)
) -> BookWithDetailsSchema:
    book = await bookCRUD.add_author_to_book(
        book_id=book_id,
        author_id=author_id,
        session=session,
    )
    return book

@router.delete(
    "/{book_id}/author/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_author(
        book_id: int,
        author_id: int,
        session: AsyncSession = Depends(db_helper.get_session)
) -> None:
    await bookCRUD.delete_author_from_book(
        book_id=book_id,
        author_id=author_id,
        session=session,
    )
